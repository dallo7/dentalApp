from dash import html, dcc
import dash_bootstrap_components as dbc
import terms
import base64


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


landed = dbc.Row([
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.P(["Dental Diagnosis and Treatment Model"],
                           style={'font-family': 'cursive', 'text-decoration': 'underline',
                                  'text-align': 'center', 'color': '2px solid black', 'fontSize': 10}),
                    dbc.CardImg(src=b64_image("img/logo.jpeg"), top=True)
                ]),
                style={"width": "13rem", "margin": "auto", "border": "2px solid green"}
            ),
            width=4,
            id="content",
            style={
                "width": "16rem",
                'background-color': '#90EE90',
                'border-radius': '5px',
                'padding': '20px',
                'box-shadow': '0 6px 14px 0 rgba(0, 0, 0, 0.2)',
                'transition': '0.3s'
            }
        )], justify="center", style={'marginBottom': 20, 'marginTop': 20}),
    html.Hr(),
    html.Br(style={"border": "2px solid green"}),
    dbc.Row([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dcc.Markdown(terms.terms_and_conditions, style={'height': '200px', "width": "auto",
                                                                    'background-color': '#90EE90',
                                                                    'border-radius': '5px',
                                                                    'padding': '20px',
                                                                    'box-shadow': '0 6px 14px 0 rgba(0, 0, 0, 0.2)',
                                                                    'transition': '0.3s', 'overflowY': 'scroll'}),
                    html.Br(),
                    dbc.Checkbox(id='checkbox', value=0),
                    dbc.Label("I agree to the Terms and Conditions", html_for="checkbox"),
                    dbc.Button("Proceed", id='proceed-button', disabled=True, style={'marginLeft': 20}),
                ])
            ])
        ])
    ], className="g-my-2")
], style={'marginBottom': 15, 'marginTop': 5, 'color': 'green', 'fontSize': 14}, justify="center")
