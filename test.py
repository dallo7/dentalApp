# audio_samples = []
#
#
# def convert_wav_flac(audio):
#     data, samplerate = sf.read(audio)
#     flac = sf.write('output.flac', data, samplerate)
#     return flac
#
#
# @app.callback(
#     Output("audio-recorder", "recording"),
#     Input("record-button", "n_clicks"),
#     Input("stop-button", "n_clicks"),
#     State("audio-recorder", "recording"),
#     prevent_initial_call=True
# )
# def control_recording(record_clicks, stop_clicks, recording):
#     return record_clicks > stop_clicks
#
#
# @app.callback(
#     Output("audio-output", "children"),
#     Output("live-update-text", "children"),
#     Input("play-button", "n_clicks"),
#     prevent_initial_call=True
# )
# def play_audio(play_clicks):
#     if play_clicks:
#
#         if audio_samples:
#             audio_array = np.array(audio_samples)
#
#             with io.BytesIO() as wav_buffer:
#                 sf.write(wav_buffer, audio_array, 16000, format="WAV")
#                 wav_bytes = wav_buffer.getvalue()
#                 wav_base64 = base64.b64encode(wav_bytes).decode()
#                 audio_src = f"data:audio/wav;base64,{wav_base64}"
#
#                 wavFile = "output.wav"
#
#                 # Your bytearray data
#                 bytearray_data = bytearray(audio_array)
#
#                 # Open a .wav file in write binary mode
#                 with wave.open(wavFile, 'wb') as wf:
#                     # Set audio parameters
#                     wf.setnchannels(1)  # mono
#                     wf.setsampwidth(2)  # number of bytes
#                     wf.setframerate(16000)  # sample rate
#
#                     # Write frames to .wav file
#                     wf.writeframes(bytearray_data)
#
#                 convert_wav_flac(wavFile)
#
#                 flacFile = "output.flac"
#
#                 API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
#                 headers = {"Authorization": "Bearer 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"}
#
#                 def query(filename):
#                     with open(filename, "rb") as f:
#                         info = f.read()
#                     response = requests.post(API_URL, headers=headers, data=info)
#                     return response.json()
#
#                 sentence = query(flacFile)["text"]
#
#                 print(sentence)
#
#                 return html.Audio(src=audio_src, controls=True, autoPlay=True, style={
#                     "margin": "30px", "text-align": "center",
#                 }), sentence
#     return dash.no_update
#
#
# @app.callback(
#     Output("dummy-output", "children"),
#     Input("audio-recorder", "audio"),
#     prevent_initial_call=True
# )
# def update_audio(audio):
#     global audio_samples
#     if audio is not None:
#         audio_samples += list(audio.values())
#     return dash.no_update
import dash
from dash import dcc, html, Input, Output

# import dash
# from dash import dcc, html, Input, Output, State
# import dash_bootstrap_components as dbc
#
# # Define your three UIs as separate divs
# ui1 = dbc.Col([html.H1("UI 1 Content")])  # Replace with your UI 1 elements
# ui2 = dbc.Col([html.H1("UI 2 Content")])  # Replace with your UI 2 elements
# ui3 = dbc.Col([html.H1("UI 3 Content")])  # Replace with your UI 3 elements
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# app.layout = dbc.Container(
#     [
#
#         # Use dcc.Loading for a visual cue while UI changes
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dcc.Loading(id="ui-container", children=ui1),
#                     width=12,
#                 )
#             ]
#         ),
#     ]
# )
#
#
# @app.callback(
#     Output("ui-container", "children"),
#     Input("ui-selector", "value"),  # Or Input("ui-switch", "value")
# )
# def update_ui(selected_ui):
#     if selected_ui == 1:
#         return ui1
#     elif selected_ui == 2:
#         return ui2
#     else:
#         return ui3
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)

#
# import dash
# from dash import dcc, html, Input, Output
# import dash_bootstrap_components as dbc
#
# # Green color theme (adjust to your preference)
# primary_green = "#2ECC71"  # Emerald green
# secondary_green = "#00897B"  # Darker green
# text_color = "#333333"     # Dark gray text
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         # Center label with margin-bottom
#                         dbc.Label(
#                             "Select Your Preferred Input Method:",
#                             className="text-center mb-3",
#                             style={"color": text_color},
#                         ),
#                         # RadioItems with custom styling and spacing
#                         dcc.RadioItems(
#                             id="ui-selector",
#                             options=[
#                                 {"label": "Audio Input", "value": 1},
#                                 {"label": "Text Input", "value": 2},
#                                 {"label": "Questionnaire", "value": 3},
#                             ],
#                             value=1,
#                             className="radio-group",
#                             style={
#                                 "display": "flex",
#                                 "flex-direction": "column",
#                                 "gap": "10px",  # Spacing between options
#                                 "color": text_color,
#                             },
#                         ),
#                     ],
#                     # Adjust column width for better layout
#                     width=4,
#                     # Style the column with green background and padding
#                     style={
#                         "background-color": secondary_green,
#                         "color": text_color,
#                         "padding": "20px",
#                         "border-radius": "5px",
#                     },
#                 )
#             ],
#             # Center the column horizontally
#             justify="center",
#         )
#     ]
# )
#
# # ... rest of your app code
#
# if __name__ == "__main__":
# #     app.run_server(debug=True)
# from sklearn.feature_extraction.text import CountVectorizer
# import pickle
# import pandas as pd
# from scipy.sparse import csr_matrix
# #
# # # # Create a sparse matrix of all zeros
# # # zero_matrix = csr_matrix((50, 145), dtype=int)
# # # print(zero_matrix)
# #
# vectorizer = CountVectorizer()
# #
# dictOutOfSample = {70: "Xerostomia (Dry Mouth)"}
# seriesDictOutOfSample = pd.Series(dictOutOfSample, name='Symptoms')
# # print(type(seriesDictOutOfSample))
#
# outOfSample = vectorizer.fit_transform(seriesDictOutOfSample)
# print(type(outOfSample))
#
# data = outOfSample.data.tolist()  # Non-zero values
# col_inds = [i for i, length in enumerate(outOfSample.indptr[1:]) for _ in range(length)]  # Row indices
# row_inds = outOfSample.indices.tolist()
#
# vector_matrix = csr_matrix((data, (row_inds, col_inds)), shape=(50, 65))
#
# print(vector_matrix.shape)
#
# # Load the model from the file
# with open('models for Treatment/rf_classifier.pkl', 'rb') as f:
#     model = pickle.load(f)
# #
# model = model.predict(vector_matrix)
# print(seriesDictOutOfSample)
# print(model)

# with open('models for Treatment/naive_bayes_classifier (1).pkl', 'rb') as f:
#     model = pickle.load(f)
# #
# model = model.predict(vector_matrix)
# print(seriesDictOutOfSample)
# print(model)

#
# with open('models for Treatment/Decision_clf.pkl', 'rb') as f:
#     model = pickle.load(f)
# #
# model = model.predict(vector_matrix)
# print(seriesDictOutOfSample)
# print(model)


# with open('models for Treatment/svm_classifier.pkl', 'rb') as f:
#     model = pickle.load(f)
# #
# model = model.predict(vector_matrix)
# print(seriesDictOutOfSample)
# print(model)

# from collections import Counter
#
# # Sample list of strings
# diagnoses = ['Oral Cancer', 'Tooth Decay (Cavities)', 'Gum Disease'] * 10  # Repeat elements for demonstration
#
# # Count the occurrences of each string
# diagnosis_counts = Counter(diagnoses)
#
# # Find the most frequent string and its count
# most_frequent, count = diagnosis_counts.most_common(1)[0]
#
# # Print the result
# print(most_frequent)
#
# from collections import Counter
#
# # Sample list of strings
# diagnoses = ['Oral Cancer', 'Oral Cancer', 'Tooth Decay (Cavities)', 'Gum Disease'] * 10  # Repeat elements for demonstration
#
# # Count the occurrences of each string
# diagnosis_counts = Counter(diagnoses)
#
# # Find the most frequent string and its count
# most_frequent, count = diagnosis_counts.most_common(1)[0]


# import requests
# from bs4 import BeautifulSoup
# 
# 
# def search(query):
#     url = f"https://duckduckgo.com/html/?q={query}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
# 
#     # Find the first search result
#     result = soup.find('a', class_='result__url').get_text(strip=True)
#     return result
# 
# 
# print(search("where is Nairobi?"))

# from huggingface_hub import InferenceClient
#
# client = InferenceClient(
#     "microsoft/Phi-3-mini-128k-instruct",
#     token="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",
# )
#
# for message in client.chat_completion(
#         messages=[{"role": "user", "content": "What is the capital of France?"}],
#         max_tokens=500,
#         stream=True,
# ):
#     print(message.choices[0].delta.content, end="")


# import requests
#
# API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-9b"
# headers = {"Authorization": "Bearer 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"}
#
#
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
#
#
# output = query({
#     "inputs": "Can you please let us know more details about your ",
# })
#
# print(output)


# import requests
# import time
#
# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
# headers = {"Authorization": "Bearer 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"}
#
#
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     time.sleep(5)
#     return response.json()
#
#
# output = query({
#     "inputs": "The answer to the universe is",
# })
#
# print(output)
