from dash import html, dcc
from dash_recording_components import AudioRecorder
import dash_bootstrap_components as dbc
import base64


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


audioRec = dbc.Row([
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Row([
                    dbc.Card(
                        dbc.CardBody([
                            html.P(["Audio to Text Input Tool"],
                                   style={'font-family': 'Times New Roman', 'text-decoration': 'underline',
                                          'text-align': 'center', 'color': '#006400', 'fontSize': 10}),
                            html.Br(),
                            dbc.CardImg(src=b64_image("img/logo1.jpeg"))]
                        ),
                        style={"width": "10rem", "margin": "0 auto", "border": "2px solid #006400"}
                    )], style={
                    "margin": "5px",
                    "text-align": "center"}, justify="center"),
                html.Div([
                    dbc.Button("Record", id="record-button",
                               style={"background-color": "#90EE90", "margin": "10px"}),

                    dbc.Button("Stop", id="stop-button", n_clicks=0,
                               style={"background-color": "#90EE90", "margin": "10px"}),

                    dbc.Button("Play", id="play-button", style={"background-color": "#90EE90", "margin": "10px"})
                ])
            ], style={"margin": "5px", "text-align": "center", "padding": "10px"}),

            dbc.Row(id="audio-output", style={
                "margin": "10px",
                "text-align": "center",
            }, justify="center"),

            html.P(id="live-update-text", style={
                "margin": "20px",
                "border": "1px solid #006400",
                "text-align": "center",
            }),
            # html.Br(),
            html.Div(id="dummy-output", style={"display": "none", "margin": "10px",
                                               "border": "1px solid #006400"}),
            # html.Br(),
            AudioRecorder(id="audio-recorder")
        ], width=4),
        dbc.Col([
            dbc.Row(
                dcc.Loading(id="ui-container12"),
                id="content12",
                style={
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }),
            dbc.Row(
                dcc.Loading(id="ui-container21"),
                id="content21",
                style={
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }
            )
        ], style={'marginLeft': '20px', 'marginRight': '10px'}),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Loading(id="ui-container31"),
            id="content31",
            width=8,
            style={
                'background-color': '#90EE90',
                'border-radius': '5px',
                'padding': '20px',
                'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                'transition': '0.3s'
            }
        ),
        dbc.Col(
            dcc.Loading(id="ui-container41"),
            id="content41",
            width=4,
            style={
                'background-color': '#90EE90',
                'border-radius': '5px',
                'padding': '20px',
                'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                'transition': '0.3s'
            }
        )
    ], style={'marginBottom': 10, 'marginTop': 25})
], justify="center", style={
    'marginLeft': 20,
    'background-color': '#90EE90',
    'border-radius': '5px',
    'padding': '20px',
    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
    'transition': '0.3s'
})
