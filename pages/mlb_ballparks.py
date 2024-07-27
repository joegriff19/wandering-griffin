from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.Div(children="MLB Ballparks", className="wg"),
        # html.Div("⚾️🏟️"),
        html.Br(),
        html.Div("National League"),
        html.Div("AT&T Park (San Francisco Giants)"),
        html.Div("(Old) Busch Stadium (STL Cardinals)"),
        html.Div("Citizens Bank Park (Philadelphia Phillies)"),
        html.Div("Coors Field (Colorado Rockies)"),
        html.Div("Miller Park (Milwaukee Brewers)"),
        html.Div("PetCo Park (San Diego Padres)"),
        html.Div("Wrigley Field (Chicago Cubs)"),
        html.Div("___ (LA Dodgers)"),
        html.Br(),
        html.Div("American League"),
        html.Div("Coliseum (Oakland A's)"),
        html.Div("US Cellular Field (Chicago White Sox)"),
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

