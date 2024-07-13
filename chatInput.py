from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

# Define the app layout
chat = dbc.Row([
    dbc.Row([
        dbc.Col([
            dcc.Textarea(
                id='user-input',
                placeholder='Hi, I am here to assist. Please share how you are feeling',
                style={'width': '100%', 'height': '150px', 'font-family': 'Times New Roman', 'padding': '10px'}
            ),
            dbc.Button(
                "Inference",
                id="submit111",
                className="mr-2",
                style={
                    'color': 'Black',
                    'backgroundColor': 'orange',
                    'boxShadow': '5px 5px 5px grey',
                    'padding': '10px',
                    'margin': '10px'
                }
            ),
            html.Br(),
        ], width=4),
        dbc.Col([
            dbc.Row(
                dcc.Loading(id="ui-container11"),
                id="content11",
                style={
                    'background-color': '#90EE90',
                    'border-radius': '5px',
                    'padding': '20px',
                    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                    'transition': '0.3s'
                }),
            html.Div(
                dcc.Loading(id="ui-container22"),
                id="content22",
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
            dcc.Loading(id="ui-container33"),
            id="content33",
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
            dcc.Loading(id="ui-container44"),
            id="content44",
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

], style={
    'background-color': '#90EE90',
    'border-radius': '5px',
    'padding': '20px',
    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
    'transition': '0.3s'
})


# Define the rules for the chatbot
def chatbot_rules(user_input):
    if user_input.lower():
        return 'Thank you for sharing i am diagnosing your Issue 🚑'
