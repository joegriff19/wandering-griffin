from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div([
        html.Div(children="Soccer Stadiums️", className="wg"),
        # html.Div("⚽️🏟"),
        html.Br(),
        html.Div("Argentina 󠁧🇦🇷"),
        html.Div("La Bombonera (Boca Juniors)*"),
        html.Div("Estadio Pedro Bidegain (San Lorenzo)"),
        html.Br(),
        html.Div("England 🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
        html.Div("Emirates (Arsenal FC)"),
        html.Div("Loftus Road Stadium (QPR)"),
        html.Br(),
        html.Div("Germany 🇩🇪"),
        html.Div("Frankfurt (Eintracht Frankfurt)"),
        html.Div("Holstein-Stadion (Holstein Kiel)"),
        html.Div("Olympiastadion (Hertha Berlin)"),
        html.Div("Red Bull Arena (RB Leipzig)"),
        html.Div("Stadion an der Alten Försterei (Union Berlin)"),
        html.Div("Signal Iduna Park (Borussia Dortmund)"),
        html.Br(),
        html.Div("Hungary 🇭🇺󠁧"),
        html.Div("Ferencváros Stadion (Ferencváros)"),
        html.Br(),
        html.Div("Italy 🇮🇹"),
        html.Div("San Siro (AC Milan / Inter Milan)*"),
        html.Br(),
        html.Div("Spain 🇪🇸"),
        html.Div("Camp Nou (FC Barcelona)"),
        html.Div("Estadi Montilivi (Girona FC)*"),
        html.Div("La Mestalla (Valencia CF)*"),
        html.Div("Metropolitano (Club Atlético de Madrid)"),
        html.Div("Santiago Bernabéu (Real Madrid CF)*"),
        html.Br(),
        html.Div("Turkey 🇹🇷󠁧"),
        html.Div("Beşiktaş Stadium (Beşiktaş)"),
        html.Br(),
        html.Div("USA 🇺🇸"),
        html.Div("Toyota Park (Chicago Fire FC)"),
        html.Div("Soldier Field (Chicago Fire FC)"),
        html.Br(),
        html.Div("* indicates I did not see a game there, but rather just viewed / toured the stadium"),
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

