from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.Div(children="US States Visited", className="wg"),
        html.Br(),
        html.Div("California"),
        html.Div("Colorado"),
        html.Div("Florida"),
        html.Div("Illinois"),
        html.Div("Indiana"),
        html.Div("Iowa"),
        html.Div("Kentucky"),
        html.Div("Maine"),
        html.Div("Massachusetts"),
        html.Div("Michigan"),
        html.Div("Montana"),
        html.Div("Nebraska"),
        html.Div("New Hampshire"),
        html.Div("New York"),
        html.Div("Ohio"),
        html.Div("Pennsylvania"),
        html.Div("Rhode Island"),
        html.Div("Utah"),
        html.Div("Vermont"),
        html.Div("Washington"),
        html.Div("Washington DC"),
        html.Div("West Virginia"),
        html.Br(),
        html.Div("Last update: July 2024"),
        html.Br(),
    ],
        # className="lead"
    ),
    html.Div(
        dbc.Button(children='Wandering Griffin Travel Home Page', id='home', href='/'),
    )
    ]
)

