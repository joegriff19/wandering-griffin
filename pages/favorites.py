from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.Div("I have grouped all of the countries I have visited into 4 different tiers. "
                 "Within each tier, the countries are in no particular order. Remember these rankings are simply "
                 "based on my personal experience and opinion!"),
        html.Br(),
        html.Br(),
        html.Div("Top"),
        html.Div("Argentina, Belgium, Chile, Croatia, Czechia, Germany, Iceland, Ireland, Italy, Mexico, Spain"),
        html.Br(),
        html.Div("Great"),
        html.Div("Andorra, Austria, Bahamas, Ecuador, England, Hungary, Montenegro, Morocco, Peru, Poland, Portugal, Slovenia, Sweden, Turkey"),
        html.Br(),
        html.Div("Good"),
        html.Div("Bulgaria, Canada, Denmark, Netherlands, North Macedonia, Norway, Slovakia"),
        html.Br(),
        html.Div("Okay"),
        html.Div("Bosnia, Bolivia, France"),
        html.Br(),
        html.Div("Bad"),
        html.Div("None! I have yet to visit a country and have a bad experience overall."),
        html.Br(),
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

