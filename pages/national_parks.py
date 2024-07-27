from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.Div(children="National Parks Visited", className="wg"),
        html.Br(),
        html.Div("United States 🇺🇸"),
        html.Div("Acadia"),
        html.Div("Indiana Dunes"),
        html.Div("Florida Everglades"),
        html.Div("Lake Tahoe"),
        html.Div("Rocky Mountain"),
        html.Div("Smoky Mountains"),
        html.Div("St. Louis Arch"),
        html.Div("Yosemite"),
        html.Div("Zion"),
        html.Br(),
        html.Div("Chile 🇨🇱"),
        html.Div("Torres del Paine"),
        html.Br(),
        html.Div("Croatia 🇭🇷"),
        html.Div("Plitvice Lakes"),
        html.Br(),
        html.Div("Germany 🇩🇪"),
        html.Div("Jasmund"),
        html.Br(),
        html.Div("Morocco 🇲🇦"),
        html.Div("Ifrane"),
        html.Br(),
        html.Div("Spain 🇪🇸"),
        html.Div("Teide"),
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

