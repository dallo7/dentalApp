from dash import html, dcc
import dash_bootstrap_components as dbc
import base64
import conditionImg


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


questionnaire = dbc.Row([
    dbc.Row([
        html.Div([html.P(['Dental Diagnosis and Treatment Model'],
                         style={'marginBottom': 15, 'marginTop': 15, 'text-align': 'center', 'color': 'Green',
                                'fontSize': 20})]),
        dbc.Col([

            html.P(['Are you currently experiencing these symptoms related to tooth damage and sensitivity?'],
                   style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
            dcc.Dropdown(conditionImg.toothdamage
                         , multi=False, placeholder="symptoms",
                         clearable=True, optionHeight=60,
                         style={'color': '#F71AF7', 'fontSize': 14}, id="drp"),

            html.P(['Are you currently experiencing these symptoms related to gum issues?'],
                   style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
            dcc.Dropdown(conditionImg.gumIssues
                         , multi=False, placeholder="symptoms",
                         clearable=True, optionHeight=60,
                         style={'color': 'LimeGreen', 'fontSize': 14,}, id="drp1"),

            html.P(['Are you currently experiencing these symptoms related to oral infections and abnormalities?'],
                   style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
            dcc.Dropdown(conditionImg.oralInfectionsAbnormalities
                         , multi=False, placeholder="symptoms",
                         clearable=True, optionHeight=60,
                         style={'color': '#0EE3D1', 'fontSize': 14, }, id="drp2"),

            html.P(['Are you currently experiencing these symptoms related to tooth eruption and alignment?'],
                   style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
            dcc.Dropdown(conditionImg.toothEruptionAlignment
                         , multi=False, placeholder="symptoms",
                         clearable=True, optionHeight=60,
                         style={'color': '#FF11F1', 'fontSize': 14, }, id="drp3"),

            html.P(['Are you currently experiencing these symptoms related to jaw issues and teeth grinding?'],
                   style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
            dcc.Dropdown(conditionImg.jawIssuesTeethGrinding
                         , multi=False, placeholder="symptoms",
                         clearable=True, optionHeight=60,
                         style={'color': '#F40C0F', 'fontSize': 14, }, id="drp4"),

            html.P(['Are you currently experiencing these symptoms related to mouth sores and difficulty swallowing?'],
                   style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
            dcc.Dropdown(conditionImg.mouthSoresDifficultySwallowing
                         , multi=False, placeholder="symptoms",
                         clearable=True, optionHeight=60,
                         style={'color': '#0C34F4', 'fontSize': 14, }, id="drp5"),
            dbc.Button(
                "Inference",
                id="btn",
                className="mr-2",
                style={
                    'color': 'Black',
                    'backgroundColor': 'orange',
                    'boxShadow': '5px 5px 5px grey',
                    'padding': '10px',
                    'margin': '10px'
                }
            )
        ], style={'fontSize': 14, 'border': '1px Green', 'marginRight': '`10px'}, width=4),
        dbc.Col([
            dbc.Row(
                dcc.Loading(id="ui-container1"),
                id="content1",
                style={
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }),
            dbc.Row(
                dcc.Loading(id="ui-container2"),
                id="content2",
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
            dcc.Loading(id="ui-container3"),
            id="content3",
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
            dcc.Loading(id="ui-container4"),
            id="content4",
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
])
