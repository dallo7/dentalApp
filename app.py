import time
from dash import html, dcc, dash_table, callback, Output, Input, State
import dash_bootstrap_components as dbc
import dash
import chatInput
import landingPage
import questionniare
import verbsNouns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import dash_auth
import inputTool
import audio
import Dashauth
import soundfile as sf
import io
import requests
import base64
import numpy as np
import wave
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import modelsDisease
import modelforTreatment

vectorizer = CountVectorizer()

app = dash.Dash(__name__, title="Dash - Community Dentals", external_stylesheets=[dbc.themes.SPACELAB],
                suppress_callback_exceptions=True)

auth = dash_auth.BasicAuth(
    app,
    Dashauth.VALID_USERNAME_PASSWORD_PAIRS
)


# Define the rules for the chatbot
def chatbot_rules(user_input):
    if 'hello' or 'hi' in user_input.lower():
        return 'Hello! How can I assist you today?'
    else:
        return 'Please share how you are feeling and i shall help to diagnose and recommend Treatment'


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


app.layout = dbc.Container([
    dbc.Row([
        html.P("Welcome to Dash - Community, an AI powered Dental Diagnosis and Treatment Tool",
               style={'font-family': 'Times New Roman', 'text-align': 'center', 'color': '#006400', 'fontSize': 20})
    ], style={
        'margin-bottom': '20px',
        'background-color': '#90EE90',
        'border-radius': '5px',
        'padding': '20px',
        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
        'transition': '0.3s'
    }),
    dbc.Row([
        landingPage.landed
    ], id="all", justify="center", align="center", style={
        'margin-bottom': '20px',
        'background-color': '#90EE90',
        'border-radius': '5px',
        'padding': '20px',
        'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
        'transition': '0.3s'
    })

], id="container", style={'margin': 'auto', 'margin-bottom': '50px', 'margin-top': '50px'})


@app.callback(
    Output('proceed-button', 'disabled'),
    [Input('checkbox', 'value')]
)
def update_button(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output('all', 'children'),
    [Input('proceed-button', 'n_clicks')]
)
def update_button(n_clicks):
    if n_clicks:
        return inputTool.inputTool
    else:
        return landingPage.landed


@app.callback(
    Output('chat-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('user-input', 'value')]
)
def update_output(n_clicks, user_input):
    if n_clicks > 0:
        return chatInput.chatbot_rules(user_input)


audio_samples = []


def convert_wav_flac(audio):
    data, samplerate = sf.read(audio)
    flac = sf.write('output.flac', data, samplerate)
    return flac


@app.callback(
    Output("audio-recorder", "recording"),
    Input("record-button", "n_clicks"),
    Input("stop-button", "n_clicks"),
    State("audio-recorder", "recording"),
    prevent_initial_call=True
)
def control_recording(record_clicks, stop_clicks, recording):
    return record_clicks > stop_clicks


# Audio component module
@app.callback(
    Output("content12", "children"),
    Output("content21", "children"),
    Output("content31", "children"),
    Output("content41", "children"),
    Output("audio-output", "children"),
    Output("live-update-text", "children"),
    Input("play-button", "n_clicks"),
    prevent_initial_call=True
)
def play_audio(play_clicks):
    if play_clicks:
        if audio_samples:
            audio_array = np.array(audio_samples)
            with io.BytesIO() as wav_buffer:
                sf.write(wav_buffer, audio_array, 16000, format="WAV")
                wav_bytes = wav_buffer.getvalue()
                wav_base64 = base64.b64encode(wav_bytes).decode()
                audio_src = f"data:audio/wav;base64,{wav_base64}"
                wavFile = "output.wav"
                bytearray_data = bytearray(audio_array)
                with wave.open(wavFile, 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(16000)
                    wf.writeframes(bytearray_data)
                convert_wav_flac(wavFile)
                flacFile = "output.flac"
                API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
                headers = {"Authorization": "Bearer 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"}

                def query(filename):
                    with open(filename, "rb") as f:
                        info = f.read()
                    response = requests.post(API_URL, headers=headers, data=info)
                    return response.json()

                sentence = query(flacFile)["text"]
                summerizedInput = verbsNouns.formatInput(sentence)
                disease = modelsDisease.models(summerizedInput)
                treatment = modelforTreatment.modelTreament(disease)
                outputLLama = modelsDisease.queryFlan(disease)
                outputLLama = outputLLama[0].values()
                outputLLama = list(outputLLama)[0]
                diagnose = dbc.Row([
                    dbc.Col([
                        html.Label("Patient Diagnosis",
                                   style={'font-family': 'cursive', 'text-decoration': 'underline',
                                          'font-weight': 'bold',
                                          'text-align': 'center', 'color': '2px solid black', 'fontSize': 20}),
                        html.P(disease, style={'marginTop': '20px', 'marginBottom': '20px'})
                    ],
                        id="content",
                        style={
                            'text-align': 'center',
                            'background-color': '#90EE90',
                            'border-radius': '5px',
                            'padding': '20px',
                            'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                            'transition': '0.3s'
                        }
                    )
                ], justify="center", style={'marginBottom': 20, 'marginTop': 20})
                treatment = html.Div([
                    dbc.Col([
                        html.Label("Treatment plan and the Medication",
                                   style={'font-family': 'cursive', 'text-decoration': 'underline',
                                          'font-weight': 'bold',
                                          'text-align': 'center', 'color': '2px solid black', 'fontSize': 20}),
                        html.P(treatment, style={'marginTop': '20px', 'marginBottom': '20px'}),
                        html.P(outputLLama,
                               style={'marginTop': '20px', 'marginBottom': '20px', 'color': 'orange',
                                      'animation': 'fadeIn 2s'})
                    ],
                        id="content",
                        style={
                            'text-align': 'center',
                            'background-color': '#90EE90',
                            'border-radius': '5px',
                            'padding': '20px',
                            'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                            'transition': '0.3s'
                        }
                    )
                ], style={'marginBottom': 20, 'marginTop': 20})
                """Track Inference and Analysis"""
                dictInference = {"Tooth Damage": summerizedInput}
                graphPd = pd.DataFrame(dictInference, index=[15])
                graphPd1 = pd.DataFrame([disease], columns=['Disease'], index=[15])
                graphPd2 = pd.DataFrame([outputLLama], columns=['Treatment'], index=[15])
                gra = pd.concat([graphPd, graphPd1, graphPd2], axis=1)
                """Save all the Prompts and the corresponding Recommendations.
                write the dataframe to a csv file row by row"""
                gra.to_csv('reco2.csv', index=False, mode='a', header=False)
                reco2 = pd.read_csv("reco2.csv")
                dashTable = html.Div([
                    html.Label("Monitoring Inference for HF",
                               style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                                      'text-align': 'center', 'marginBottom': '10px', 'color': '2px solid black',
                                      'fontSize': 15}),
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i, "renamable": True, "hideable": True} for i in reco2.columns],
                        data=reco2.to_dict('records'),
                        style_table={'overflowX': 'auto'},
                        export_format='xlsx',
                        editable=True,
                        include_headers_on_copy_paste=True,
                        sort_action='native',
                        page_action="native",
                        page_size=1,
                        style_cell={
                            'height': 'auto',
                            'minWidth': '140px', 'width': '150px', 'maxWidth': '180px',
                            'whiteSpace': 'normal'
                        },
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'color': 'black'
                        },
                        style_data={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'color': 'black'
                        }
                    )
                ], style={'text-align': 'center'})
                """Word cloud Analysis"""
                wordString = reco2.copy()
                wordString = wordString.to_string()
                """Generate a word cloud image"""
                wordcloud = WordCloud(width=1200, height=800).generate(wordString)
                """Display the generated image"""
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                plt.savefig("test.jpeg")
                wordCloud = b64_image("test.jpeg")
                wordcloud = dbc.Row([
                    html.P("Analysis of common Symptoms&Diagnosis",
                           style={'font-family': 'cursive', 'text-decoration': 'underline',
                                  'font-weight': 'bold',
                                  'text-align': 'center', 'color': '2px solid black', 'fontSize': 15}),
                    html.Img(src=wordCloud, id="wordcloud", style={'width': '100%', 'height': 'auto'})
                ])

                return diagnose, treatment, dashTable, wordcloud, html.Audio(src=audio_src, controls=True,
                                                                             autoPlay=True,
                                                                             style={"margin": "30px",
                                                                                    "text-align": "center"}), sentence
        else:
            return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    else:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update


@app.callback(
    Output("dummy-output", "children"),
    Input("audio-recorder", "audio"),
    prevent_initial_call=True
)
def update_audio(audi):
    global audio_samples
    if audi is not None:
        # Update the audio samples with the new audio
        audio_samples += list(audi.values())
    return dash.no_update


# Select the UI input method
@app.callback(
    Output("ui-container", "children"),
    Input("ui-selector", "value")
)
def update_ui(selected_ui):
    if selected_ui == 1:
        return audio.audioRec
    elif selected_ui == 2:
        return chatInput.chat
    else:
        return questionniare.questionnaire


# Questionnaire

@app.callback(
    Output("content1", "children"),
    Output("content2", "children"),
    Output("content3", "children"),
    Output("content4", "children"),
    [
        Input("btn", "n_clicks"),
        Input("drp", "value"),
        Input("drp1", "value"),
        Input("drp2", "value"),
        Input("drp3", "value"),
        Input("drp4", "value"),
        Input("drp5", "value"),
    ],
    prevent_initial_call=True
)
def control_recording(n_clicks, drp, drp1, drp2, drp3, drp4, drp5):
    if n_clicks:
        """Diagnosis and Treatment"""
        lists = f"{drp}, {drp1}, {drp2}, {drp3}, {drp4}, {drp5}"
        words = lists.split(", ")
        filtered_words = [word for word in words if word != "None"]
        result = ", ".join(filtered_words)
        disease = modelsDisease.models(result)
        treatment = modelforTreatment.modelTreament(disease)
        outputLLama = modelsDisease.queryFlan(disease)
        outputLLama = outputLLama[0]["generated_text"]
        outputLLama = modelsDisease.filter_text(outputLLama)
        diagnose = dbc.Row([
            dbc.Col([
                html.Label("Patient diagnosis",
                           style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                                  'text-align': 'center', 'color': '2px solid black', 'fontSize': 20}),
                html.P(disease, style={'marginTop': '20px', 'marginBottom': '20px'})
            ], width=4,
                id="content",
                style={
                    'text-align': 'center',
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }
            )
        ], justify="center", style={'marginBottom': 20, 'marginTop': 20})
        treatment = dbc.Row([
            dbc.Col([
                html.Label("Treatment plan and the Medication",
                           style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                                  'text-align': 'center', 'color': '2px solid black', 'fontSize': 20}),
                html.P(treatment, style={'marginTop': '20px', 'marginBottom': '20px'}),
                html.P(outputLLama,
                       style={'marginTop': '20px', 'marginBottom': '20px', 'color': 'purple', 'animation': 'fadeIn 2s'})
            ],
                id="content",
                style={
                    'text-align': 'center',
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }
            )
        ], justify="center", style={'marginBottom': 20, 'marginTop': 20})
        """Track Inference and Analysis"""
        dictInference = {"Tooth Damage": drp, "Gum Issues": drp1, "Oral Infections Abnormalities": drp2,
                         "Tooth Eruption Alignment": drp3, "Jaws Issues TeethGrinding": drp4,
                         "Mouth Sores Difficulty Swallowing": drp5}
        graphPd = pd.DataFrame(dictInference, index=[15])
        graphPd1 = pd.DataFrame([disease], columns=['Disease'], index=[15])
        graphPd2 = pd.DataFrame([outputLLama], columns=['Treatment'], index=[15])
        gra = pd.concat([graphPd, graphPd1, graphPd2], axis=1)
        # Save all the Prompts and the corresponding Recommendations.
        # write the dataframe to a csv file row by row
        gra.to_csv('reco.csv', index=False, mode='a', header=False)
        reco = pd.read_csv("reco.csv")
        dashTable = html.Div([
            html.Label("Monitoring Inference for HF",
                       style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                              'text-align': 'center', 'marginBottom': '10px', 'color': '2px solid black',
                              'fontSize': 15}),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i, "renamable": True, "hideable": True} for i in reco.columns],
                data=reco.to_dict('records'),
                style_table={'overflowX': 'auto'},
                export_format='xlsx',
                editable=True,
                include_headers_on_copy_paste=True,
                sort_action='native',
                page_action="native",
                page_size=1,
                style_cell={
                    'height': 'auto',
                    'minWidth': '140px', 'width': '150px', 'maxWidth': '180px',
                    'whiteSpace': 'normal'
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'black'
                },
                style_data={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'black'
                }
            )
        ], style={'text-align': 'center'})

        """Word cloud Analysis"""
        wordString = reco.copy()
        wordString = wordString.to_string()
        # Generate a word cloud image
        wordcloud = WordCloud(width=1200, height=800).generate(wordString)
        # Display the generated image
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig("test.jpeg")
        wordCloud = b64_image("test.jpeg")
        wordcloud = dbc.Row([
            html.P("Analysis of common Symptoms&Diagnosis",
                   style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                          'text-align': 'center', 'color': '2px solid black', 'fontSize': 15}),
            html.Img(src=wordCloud, id="wordcloud", style={'width': '100%', 'height': 'auto'})
        ])
        return diagnose, treatment, dashTable, wordcloud
    else:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update


# Chat call back

@app.callback(
    Output("content11", "children"),
    Output("content22", "children"),
    Output("content33", "children"),
    Output("content44", "children"),
    [Input("submit111", "n_clicks"),
     Input("user-input", "value")],
    prevent_initial_call=True
)
def update_audio(nclicks, val):
    if nclicks:
        summerizedInput = verbsNouns.formatInput(val)
        disease = modelsDisease.models(summerizedInput)
        treatment = modelforTreatment.modelTreament(disease)
        outputLLama = modelsDisease.queryFlan(disease)
        outputLLama = outputLLama[0].values()
        outputLLama = list(outputLLama)[0]
        diagnose = dbc.Row([
            dbc.Col([
                html.Label("Patient diagnosis",
                           style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                                  'text-align': 'center', 'color': '2px solid black', 'fontSize': 20}),
                html.P(disease, style={'marginTop': '20px', 'marginBottom': '20px'})
            ], width=4,
                id="content",
                style={
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }
            )
        ], justify="center", style={'marginBottom': 20, 'marginTop': 20})
        treatment = html.Div([
            dbc.Col([
                html.Label("Treatment plan and the Medication",
                           style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                                  'text-align': 'center', 'color': '2px solid black', 'fontSize': 20}),
                html.P(treatment, style={'marginTop': '20px', 'marginBottom': '20px'}),
                html.P(modelsDisease.filter_text(outputLLama),
                       style={'marginTop': '20px', 'marginBottom': '20px', 'color': 'orange', 'animation': 'fadeIn 2s'})
            ],
                id="content",
                style={
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }
            )
        ], style={'marginBottom': 20, 'marginTop': 20})
        """Track Inference and Analysis"""
        dictInference = {"Tooth Damage": summerizedInput}
        graphPd = pd.DataFrame(dictInference, index=[15])
        graphPd1 = pd.DataFrame([disease], columns=['Disease'], index=[15])
        graphPd2 = pd.DataFrame([outputLLama], columns=['Treatment'], index=[15])
        gra = pd.concat([graphPd, graphPd1, graphPd2], axis=1)
        # Save all the Prompts and the corresponding Recommendations.
        # write the dataframe to a csv file row by row
        gra.to_csv('reco1.csv', index=False, mode='a', header=False)
        reco1 = pd.read_csv("reco1.csv")
        dashTable = html.Div([
            html.Label("Monitoring Inference for HF",
                       style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                              'text-align': 'center', 'marginBottom': '10px', 'color': '2px solid black',
                              'fontSize': 15}),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i, "renamable": True, "hideable": True} for i in reco1.columns],
                data=reco1.to_dict('records'),
                style_table={'overflowX': 'auto'},
                export_format='xlsx',
                editable=True,
                include_headers_on_copy_paste=True,
                sort_action='native',
                page_action="native",
                page_size=1,
                style_cell={
                    'height': 'auto',
                    'minWidth': '140px', 'width': '150px', 'maxWidth': '180px',
                    'whiteSpace': 'normal'
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'black'
                },
                style_data={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'color': 'black'
                }
            )
        ], style={'text-align': 'center'})

        """Analysis"""
        wordString = reco1.copy()
        wordString = wordString.to_string()
        # Generate a word cloud image
        wordcloud = WordCloud(width=1200, height=800).generate(wordString)
        # Display the generated image
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig("test.jpeg")
        wordCloud = b64_image("test.jpeg")
        wordcloud = dbc.Row([
            html.P("Analysis of common Symptoms&Diagnosis",
                   style={'font-family': 'cursive', 'text-decoration': 'underline', 'font-weight': 'bold',
                          'text-align': 'center', 'color': '2px solid black', 'fontSize': 15}),
            html.Img(src=wordCloud, id="wordcloud", style={'width': '100%', 'height': 'auto'})
        ])
        time.sleep(8)
        return diagnose, treatment, dashTable, wordcloud
    else:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True, port=8987)
