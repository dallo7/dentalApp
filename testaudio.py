import dash
from dash import html
from dash.dependencies import Input, Output, State
from dash_recording_components import AudioRecorder
import soundfile as sf
import dash_bootstrap_components as dbc
import io
import requests
import base64
import numpy as np
import wave

testAudio = dbc.Row([
    dbc.Row([dbc.Card(
        dbc.CardBody([
            html.P(["Researcher's Transcriptions Tool"],
                   style={'font-family': 'cursive', 'text-decoration': 'underline',
                          'text-align': 'center', 'color': '2px solid black', 'fontSize': 10}),
            html.Br(),
            dbc.CardImg(src="/assets/logoA.png", top=True, style={"width": "100%", "height": "100%"}, )]
        ),
        style={"width": "10rem", "margin": "0 auto", "border": "2px solid green"}
    )], style={
        "margin": "20px",
        "text-align": "center"}, justify="center"),

    html.Br(style={
        "border": "1px solid purple"
    }),
    dbc.Row([
        dbc.Button("Record", id="record-button", style={"background-color": "#ccffee", "margin": "10px"}),

        dbc.Button("Stop Recording", id="stop-button", n_clicks=0,
                   style={"background-color": "#ffb3b3", "margin": "10px"}),

        dbc.Button("Play", id="play-button", style={"background-color": "#00cc44", "margin": "10px"})

    ], style={"margin": "20px", "text-align": "center", "padding": "10px"}),

    dbc.Row(id="audio-output", style={
        "margin": "10px",
        "text-align": "center",
    }, justify="center"),

    html.P(id="live-update-text", style={
        "margin": "20px",
        "border": "1px solid green",
        "text-align": "center",
    }),
    html.Br(style={
        "border": "1px solid purple"
    }),
    html.Div(id="dummy-output", style={"display": "none", "margin": "10px",
                                       "border": "1px solid green"}),
    html.Br(style={
        "border": "1px solid purple"
    }),
    AudioRecorder(id="audio-recorder")
], justify="center")
