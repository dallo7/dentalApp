from dash import dcc
import dash_bootstrap_components as dbc

inputTool = dbc.Row([
    dbc.Row([
        dbc.Col(
            [
                dbc.Label("Select You Preferred Input Method:", style={'font-weight': 'bold', 'color': '#006400'}),
                dcc.RadioItems(
                    id="ui-selector",
                    options=[
                        {"label": "Audio Input", "value": 1},
                        {"label": "Text Input", "value": 2},
                        {"label": "Questionnaire", "value": 3},
                    ],
                    value=3,
                    style={'color': '#006400'}
                ),
            ],
            width=2,
            style={
                'background-color': '#90EE90',
                'border-radius': '5px',
                'padding': '20px',
                'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                'transition': '0.3s'
            }
        ),
        dbc.Col(
            dcc.Loading(id="ui-container"),
            id="content",
            width=12,
            style={
                'background-color': '#90EE90',
                'border-radius': '5px',
                'padding': '20px',
                'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                'transition': '0.3s'
            }
        )
    ])
])
