from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc
import city_list
import visited_countries

country_count = len(city_list.all_options.keys())
country_pct = int(country_count / 195 * 100)

continent_count = 0
if len(visited_countries.af_countries) > 0:
    continent_count = continent_count + 1
if len(visited_countries.as_countries) > 0:
    continent_count = continent_count + 1
if len(visited_countries.eu_countries) > 0:
    continent_count = continent_count + 1
if len(visited_countries.na_countries) > 0:
    continent_count = continent_count + 1
if len(visited_countries.oc_countries) > 0:
    continent_count = continent_count + 1
if len(visited_countries.sa_countries) > 0:
    continent_count = continent_count + 1
if len(visited_countries.an_countries) > 0:
    continent_count = continent_count + 1

country_count_af = len(visited_countries.af_countries)
country_count_as = len(visited_countries.as_countries)
country_count_eu = len(visited_countries.eu_countries)
country_count_na = len(visited_countries.na_countries)
country_count_oc = len(visited_countries.oc_countries)
country_count_sa = len(visited_countries.sa_countries)
country_count_an = len(visited_countries.an_countries)

layout = html.Div([
    html.Div([
        html.Div(children="Country Statistics", className="wg"),
        html.Br(),
        html.Div("Countries Visited"),
        html.Div(str(country_count) + " / 195"),
        html.Div(str(country_pct) + "%"),
        html.Br(),
        html.Div("Continents"),
        html.Div(str(continent_count) + " / 7"),
        html.Div(str((int(continent_count / 7 * 100))) + "%"),
        html.Br(),
        html.Div("Africa"),
        html.Div(str(country_count_af) + " / 54"),
        html.Div((str(int(country_count_af / 54 * 100))) + "%"),
        html.Br(),
        html.Div("Asia"),
        html.Div(str(country_count_as) + " / 48"),
        html.Div((str(int(country_count_as / 48 * 100))) + "%"),
        html.Br(),
        html.Div("Europe"),
        html.Div(str(country_count_eu) + " / 46"),
        html.Div((str(int(country_count_eu / 46 * 100))) + "%"),
        html.Br(),
        html.Div("North America"),
        html.Div(str(country_count_na) + " / 23"),
        html.Div((str(int(country_count_na / 23 * 100))) + "%"),
        html.Br(),
        html.Div("Oceania"),
        html.Div(str(country_count_oc) + " / 14"),
        html.Div((str(int(country_count_oc / 14 * 100))) + "%"),
        html.Br(),
        html.Div("South America"),
        html.Div(str(country_count_sa) + " / 12"),
        html.Div((str(int(country_count_sa / 12 * 100))) + "%"),
        html.Br(),
        html.Div("Antarctica"),
        html.Div(str(country_count_an) + " / 2"),
        html.Div((str(int(country_count_an / 2 * 100))) + "%"),
        html.Br(),
    ],
        # className="lead"
    ),
    html.Div(
        dbc.Button(children='Wandering Griffin Travel Home Page', id='home', href='/'),
    )
    ]
)

