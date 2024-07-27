from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc

# image_path = 'assets/my-image.png'

layout = html.Div([
    html.Div([
        html.Div(children="Nice here... but have you ever been to Dubuque, Iowa?", className="wg"),
        html.Br(),
        html.Div("Germans love stickers. In Germany, anything with a flat surface will be covered in stickers. "
                 "The stickers can be for anything... sports teams, music artists, political parties, breweries, "
                 "you name it. But there is one sticker in particular that is most prevalent in Germany and all "
                 "across the world. It's a big yellow sticker promoting the southwestern German state of "
                 "Baden-Württemberg, home of the fabled Black Forest. In German, it says 'Nice here... "
                 "but have you ever been to Baden-Württemberg?'"),
        html.Br(),
        dbc.Carousel(
        items=[
            {"src": "assets/nice_here/nett_hier_chi.JPG"},
        ],
        interval=2000,
        ride="carousel",
        className="carousel-fade"
    ),
        # html.Div(html.Img(src="assets/nice_here/nett_hier_chi.JPG"), style={'height': '10%', 'width': '10%'}),
        html.Br(),
        html.Div("I have personally seen this sticker everywhere from Berlin to Chicago to Istanbul to Patagonia. "
                 "There are videos on social media of people finding the stickers in the most obscure places on the "
                 "planet, including ____!"),
        html.Br(),
        html.Div("Given the popularity of the Baden-Württemberg sticker, it is now possible to order a custom version "
                 "of the sticker online, and I did just that! Dubuque is my mom's "
                 "hometown, and as part of a fun gift to her, I have (with the help of friends and family) put up the "
                 "custom stickers all over the world! Please enjoy the pictures of the Dubuque sticker below."),
        html.Br(),
    ],
        # className="lead"
    ),
    dbc.Carousel(
        items=[
            {"src": "assets/argentina/ba9.JPG"},
            {"src": "assets/argentina/ba2.JPG"},
        ],
        interval=2000,
        ride="carousel",
        className="carousel-fade"
    ),
    html.Br(), html.Br(),
    html.Div(
        dbc.Button(children='Wandering Griffin Travel Home Page', id='home', href='/'),
    )
    ]
)
