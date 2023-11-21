# Import Packages and other files for app
import index
from app import app, server  # NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html, clientside_callback, State
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import warnings
from datetime import date
import dash_player as dp
import dash_leaflet as dl
import coordinates
import globe
import city_list
today = date.today()
warnings.simplefilter(action='ignore', category=FutureWarning)

# padding for the page content
CONTENT_STYLE = {
   "margin-left": "2rem",
   "margin-right": "2rem",
   "padding": "2rem 1rem",
}

# Index Page Layout
colors = {
    # 'background': '#ffffff',
    'text': '#0000CD'
}

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)
lon_deg = -50

# define sidebar layout
app.layout = html.Div([
   dcc.Location(id="url"),
   content,
])

# index page layout
index_layout = html.Div(
    children=[
            html.Header(
                children=[
                    html.Div(children="Wandering Griffin Travel", className="wg"),
                    html.Br(),
                    dcc.Interval(id='update-rotation', interval=500, n_intervals=0),
                    dcc.Graph(
                        id='rotating-globe',
                        # animate=True,
                        responsive=False,
                        style={
                            # 'width': '20vh',
                            'height': '40vh',
                            'padding-left': '10%', 'padding-right': '10%'
                        },
                        config={
                            'displayModeBar': False,
                            'scrollZoom': False,
                            'doubleClick': False,
                        },
                    ),
                    # html.Br(),
                    html.Div(children="I can't do everything but I can try!", className="powered"),
                    html.Div(children=" ", style={"fontSize": "75px"}),
                    html.Br(),
                ],
                style={
                    'textAlign': 'center',
                    # 'justify': 'center',
                    'color': colors['text'],
                    "padding": "0px",
                    "margin": "0px"
                }
            ),
            html.Div([
                "Select a country",
                dcc.Dropdown(
                    list(city_list.all_options.keys()),
                    clearable=False,
                    searchable=False,
                    id='countries-dd'
                ),
                html.Br(),
                html.Div("Select a city / place"),
                dcc.Dropdown(id='cities-dd', options=[], searchable=False, clearable=False),
                html.Br(),
            ], style={
                'textAlign': 'center',
                # 'margin-left': '100px', 'margin-right': '100px',
                'color': 'black',
                # "display": "flex",
                'max-width': '500px',
                'margin': 'auto'
                # 'verticalAlign': 'middle',
                # 'align-items': 'center',
                # 'justify-content': 'center'
                # 'justify': 'center'
            }
            ),
            html.Div([
                html.Div(id='city_info'),
                html.Br(),
                html.Div(children="If this was helpful, please consider buying me a beverage! Thank you!",
                         className="beverage"),
                html.Div(children="🍻", style={"fontSize": "35px"}),
                dbc.Button(children='My Venmo',
                           color="primary",
                           outline=True,  # more lightweight format
                           href="https://venmo.com/u/joegriff19")
            ], style={'textAlign': 'center',
                      'max-width': '900px',
                      'margin': 'auto',
                      # 'margin-left': '100px', 'margin-right': '100px',
                      'color': 'black',
                      # 'width': '50%',
                      # 'verticalAlign': 'middle'
                      # 'align-items': 'center', 'justify-content': 'center'
                      }
            ),
    ])

# page callbacks


@app.callback(
    Output('rotating-globe', 'figure'),
    [Input('update-rotation', 'n_intervals')]
)
def rotate_globe(_):
    index.lon_deg = index.lon_deg + 1
    x = index.lon_deg
    return globe.fig.update_layout(geo=dict(center_lon=x, projection_rotation_lon=x))


@app.callback(
    Output('page-content', 'children',),
    [Input('url', 'pathname',)]
)
def render_page_content(pathname):
    if pathname == '/':
        return index_layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
       [
           html.H1("404: Not found", className="text-danger"),
           html.Hr(),
           html.P(f"The pathname {pathname} was not recognized..."),
       ]
    )


@app.callback(
    # Output('cities-dd', 'children'),
    Output('cities-dd', 'options'),
    Input('countries-dd', 'value'),
    prevent_initial_call=True
)
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in city_list.all_options[selected_country]]


@app.callback(
    Output('city_info', 'children'),
    Input('cities-dd', 'value')
)
def set_display_children(value):
# Andorra
    if value == 'Pal Arinsal':
        return 'Go skiing! Pyrenees mountains are beautiful and very affordable compared to the US. ' \
               'Only ~3-4 hour drive from Barcelona. The skiing is great and the ski town is very fun as well.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/andorra/Andorra-44.JPG"},
                    {"src": "assets/andorra/Andorra-4.JPG"},
                    {"src": "assets/andorra/Andorra-10.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.pal_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Argentina
    if value == 'Buenos Aires':
        return "The capital of Argentina! One of the most fun weekend trips of my life. Be sure to eat lots " \
               "of ‘parilla’ (grilled meat). The ‘choripan’ is a classic and is so good - a grilled chorizo sandwich " \
               "with a chimichurri sauce. You can (and should) enjoy delicious steak dinners for pretty cheap. " \
               "Everything gets especially cheap if you take advantage of the ‘blue dollars.’ Argentinian pesos have " \
               "continued to decline in value, and because of this many Argentinians would rather store their " \
               "savings in USD rather than pesos. Thus, they are willing to trade you almost twice the current " \
               "exchange rate for your American dollars. This is very common and open on ‘Calle Florida.’ As soon as " \
               "you walk down the street you will here people saying ‘cambio’ (‘change’ in English). Do this as soon " \
               "as you get to Argentina and pay with cash for everything. By doing this everything in the country " \
               "essentially becomes 50% off! Even without this ‘discount,’ Airbnbs are still very cheap. Next — " \
               "absolutely go to a soccer game while you are here. The atmosphere is insane. There are 5 top league " \
               "teams in Buenos Aires, the biggest being Boca Juniors and River Plate. The Boca Juniors stadium, " \
               "called La Bombonera, is many soccer fans’ holy grail of soccer stadiums. We did not go to a " \
               "game there unfortunately, but we went to a San Lorenzo (Pope Francis’ team) game " \
               "and the atmosphere was still like nothing I had ever seen before. You can be sure to get legitimate " \
               "tickets by booking through this website: ", \
               html.A("https://landingpadba.com/", href="https://landingpadba.com/"), \
               html.Br(), html.Br(), \
               "Santiago is the name of the guy who runs the company. He is from " \
               "Argentina and loves football. You will meet him and any others going to the game at a famous pizza " \
               "place. Buenos Aires has a huge Italian population and here you can try the super cheesy " \
               "Argentinian pizza. Be sure to try the most famous one, the fugazza " \
               "(loads of cheese and grilled onions). After some pizza and beer, " \
               "you will take a private bus to the stadium. The pizza and beer at the restaurant, and the " \
               "transportation to and from the game, are included in your football ticket package. Although we did " \
               "not see a game at La Bombonera, we were still able to do a stadium visit. There was a very big " \
               "game while we were there though — the league game between Boca Juniors and River Plate, " \
               "known as the Súperclasico. These two teams are known to have perhaps the fiercest rivalry of " \
               "any two sports teams on the planet. Every bar in the city was packed for game, and Boca " \
               "ended up winning. The streets near the stadium proceeded to celebrate all night long. We grabbed a " \
               "couple beers and joined the celebrations. This was one of the most fun experiences of my life!'", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/argentina/ba9.JPG"},
                    {"src": "assets/argentina/ba2.JPG"},
                    {"src": "assets/argentina/ba3.JPG"},
                    {"src": "assets/argentina/ba4.JPG"},
                    {"src": "assets/argentina/ba5.JPG"},
                    {"src": "assets/argentina/ba6.JPG"},
                    {"src": "assets/argentina/ba7.JPG"},
                    {"src": "assets/argentina/ba8.JPG"},
                    {"src": "assets/argentina/ba.JPG"},
                    {"src": "assets/argentina/ba1.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.ba_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Austria
    if value == 'Dornbirn':
        return 'Home of the Rhombergs! My great-great grandpa, Franz Martin Rhomberg, came to the US ' \
               'from this small city in Austria. There are so many stores and other signs with the name Rhomberg ' \
               'still to this day — it was crazy to see! The other big Rhomberg highlight was seeing the ' \
               'old ‘Kirchenbuch,’ the ‘church book’ (since church and state used to be the same) ' \
               'with my Rhomberg ancestors’ names written by hand all the way back to the 1400s. ' \
               'This was amazing to see. There are beautiful mountain views all over the city as it is ' \
               'surrounded by the Alps. For an amazing view of the city, go up the cable car to ' \
               '_____. There is a cool restaurant up here called _____. For a really cool old tavern down ' \
               'in the city, the Rothaus is awesome. In winter, there is also great skiing nearby. ' \
               'I did a trip for a couple days to Steffisalp and the views were incredible. ', \
               html.Br(), html.Br(), html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.dornbirn_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Vienna':
        return 'A very grand city! The capital of Austria is very impressive. The Hofburg Palace and the main ' \
               'cathedral on Stephansplatz are the big ' \
               'highlights, but there is so much more to see! Even beyond the main sightseeing spots, ' \
               'there are so many beautiful buildings that I feel could be the main tourist attraction ' \
               'in many other cities. However, there are just so many of these beautiful buildings that many ' \
               'don’t get the attention they probably deserve.', \
               html.Br(), html.Br(), \
               'The cafe scene is huge here. There are many ' \
               'cafes all over the city — it is a very popular activity to stop at a cafe for coffee and a ' \
               'piece of cake (or one of many other pastries / dishes). These cafes range from very casual to ' \
               'quite grand with high ceilings and ornate decorations. The cafe scene ties in with the artsy side ' \
               'of the city. There is a lot of history here with music and with theatre. Mozart lived here much ' \
               'of his life and had a huge influence on the city. It is highly recommended to visit the opera house ' \
               'to see a show if possible.', \
               html.Br(), html.Br(), \
               'There is a lot of great food in Vienna. Be sure to try Wiener Schnitzel and Kaiserschmarrn (little ' \
               'pancake bites served with an apple sauce). Other favorites include goulasch, sausage (great street ' \
               'food), and pumpkin soup (in the fall). There is plenty to do in a few days in Vienna, ' \
               'but for a really fun day trip option, go to Bratislava, the capital of Slovakia! ' \
               'It is very close, less than an hour away by train or bus. I loved doing a full day trip here.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/austria/vienna.JPG"},
                    {"src": "assets/austria/vienna1.JPG"},
                    {"src": "assets/austria/vienna2.JPG"},
                    {"src": "assets/austria/vienna3.JPG"},
                    {"src": "assets/austria/vienna4.JPG"},
                    {"src": "assets/austria/vienna5.JPG"},
                    {"src": "assets/austria/vienna6.JPG"},
                    {"src": "assets/austria/vienna7.JPG"},
                    {"src": "assets/austria/vienna8.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.vienna_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Bahamas
    if value == 'Eleuthera':
        return 'ready for an epic sailing trip??', html.Br(), html.Br(), \
           html.Div(
               style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                      "margin": "auto"},
               # style={"width": "55%", "padding": "0px", 'margin': 'auto'},
               children=[
                   dp.DashPlayer(
                       id="player",
                       url="https://youtu.be/x5OY6N37BNM",
                       controls=True,
                       width="100%",
                       height="200px",
                   )
               ]
           ), html.Br(), \
           html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.eleuthera_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'New Providence (where Nassau is located)':
        return 'explore Nassau, eat conch, go to the beach, and listen to Bob', html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.nassau_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Belgium
    if value == 'Antwerp':
        return 'Beware of the Long Wapper! more to come!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/belgium/antwerp.JPG"},
                    {"src": "assets/belgium/antwerp1.JPG"},
                    {"src": "assets/belgium/antwerp2.JPG"},
                    {"src": "assets/belgium/antwerp3.JPG"},
                    {"src": "assets/belgium/antwerp4.JPG"},
                    {"src": "assets/belgium/antwerp5.JPG"},
                    {"src": "assets/belgium/antwerp6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.antwerp_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Brussels':
        # image_path = 'assets/andrea_delirium.gif'
        return 'It is often suggested to skip Brussels (Band visit other Belgian cities such as Ghent or Antwerp... ' \
               'and while I love these smaller cities of Belgium, I definitely would NOT recommend immediately ' \
               'skipping Brussels for other cities in Belgium. The center of Brussels is really nice. The town hall ' \
               'of Brussels is amazing. There are more than 300 little statues on the exterior depicting saints ' \
               'and other historical figures. In addition to the town hall, the Grand Square (Grand Place in French) ' \
               'has a number of other buildings that are much more stunning in person than in pictures, especially ' \
               'because all the gold accents -- they really stand out in person. I would highly recommend restaurant ' \
               'Fin de Siècle (amazing Flemish Carbonnade) and Le Bistro - Porte de Hal (amazing oyster buckets ' \
               'and beer selection here). There are also a couple really nice cafes in the Parc de Bruxelles park in ' \
               'front of the Brussels Palace, called Kiosk Radio and Woodpecker Parc Royal. ' \
               'Would definitely recommend coming for a beverage and  / or some food when the weather is nice. ' \
               'It is also absolutely necessary to try the Belgian waffles (in the Liege style, they are somewhat ' \
               "circular in shape). The best ones are from the yellow food trucks called 'Gaufres Chaudes.' You can " \
               "find one (or two) in front of the palace, and another one next to the Ferris wheel. Don't forget the " \
               'Delirium Village -- it is really fun and gets quite lively in the evenings! Lastly, a couple of the ' \
               "funniest and weirdest statues are the 'manneken pis' (peeing boy) and 'het zinneke' (peeing dog).", \
                html.Br(), html.Br(), dbc.Carousel(
                    items=[
                        {"src": "assets/belgium/brussels.JPG"},
                        {"src": "assets/belgium/brussels7.JPG"},
                        {"src": "assets/belgium/brussels3.JPG"},
                        {"src": "assets/belgium/brussels1.JPG"},
                        {"src": "assets/belgium/brussels2.JPG"},
                        {"src": "assets/belgium/brussels4.JPG"},
                        {"src": "assets/belgium/brussels5.JPG"},
                        {"src": "assets/belgium/brussels6.JPG"},
                    ],
                    interval=2000,
                    ride="carousel",
                    className="carousel-fade"
                    ), html.Br(), \
                        html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.brussels_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Leuven':
        return 'What a fun little town really close to Brussels. It is easily accessible via the train system;' \
               'the ride takes less than 30 minutes from Brussels. The main attraction in Leuven is the Town Hall, ' \
               'and wow it is actually quite stunning. There are 236 little statues on the exterior depicting saints ' \
               'and other historical figures. Be sure to also check out the other main plaza, Oude Markt.' \
               'Enjoy some Stella Artois -- it is brewed here! You can actually visit the brewery, it is not far ' \
               'at all from the center of the city or the main train station. Be sure to book a tour ahead of ' \
               'time though as the time slots fill up.', \
               html.Br(), html.Br(), dbc.Carousel(
                    items=[
                        {"src": "assets/belgium/leuven2.JPG"},
                        {"src": "assets/belgium/leuven.JPG"},
                        {"src": "assets/belgium/leuven1.JPG"},
                        {"src": "assets/belgium/leuven3.JPG"},
                        {"src": "assets/belgium/leuven4.JPG"},

                    ],
                    interval=2000,
                    ride="carousel",
                    className="carousel-fade"
                    ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.leuven_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Ghent':
        return 'I absolutely loved my time here. It is such a cute little city. The main area of the city feels like ' \
               'something out of a Harry Potter movie! The canal lined with classic Belgian architecture houses, ' \
               'the bridge, the castle (Gravensteen), and the grand churches all make for really stunning and ' \
               "impressive views. Be sure to walk across St. Michael's Bridge and walk along the canal (Korenlei) " \
               "to get the best views." \
               'On top of all this -- the beer here is amazing! There is a very ' \
               'One of the best beers in the world (Delirium Tremens) is made ' \
               'just outside of Ghent. If you have a few hours, definitely make the little trip to visit -- the ' \
               'brewery that makes Delirium is called Huyghe. It is still family-owned and I even got to meet and ' \
               'have a beer with the CEO!', \
               html.Br(), html.Br(), \
               'Back in the city of Ghent, be sure to also visit ' \
               "the 'Friday Market Square' -- a nice plaza surrounded by beautiful buildings in the classic Belgian" \
               "/ Dutch style, and also where one of the coolest breweries / beer bars can be found! They have a " \
               "fun / funny ny tradition where if you order their house blonde beer (which is insanely good) " \
               "in the 1.5 liter pour, you have to give the barman a shoe as a deposit for the science experiment-" \
               "looking beer glass! Not only that, but the shoes then go in a basket which is raised to the " \
               "ceiling and it rings a bell. Enjoy the picture below!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/belgium/ghent.JPG"},
                    {"src": "assets/belgium/ghent1.JPG"},
                    {"src": "assets/belgium/ghent2.JPG"},
                    {"src": "assets/belgium/ghent3.JPG"},
                    {"src": "assets/belgium/ghent4.JPG"},
                    {"src": "assets/belgium/ghent5.JPG"},
                    {"src": "assets/belgium/ghent6.JPG"},
                    {"src": "assets/belgium/ghent7.JPG"},
                    {"src": "assets/belgium/ghent8.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.ghent_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Bolivia
    if value == 'Cliza':
        return 'A very small town outside of Cochabamba, this was the destination for the Solidarity Bridge ' \
               'mission trip where I joined as a Spanish interpreter. This is quite far off the beaten path and ' \
               'I would not recommend for tourism purposes, but this will always be a special place for me!', \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/Hhw77jS-VgE?si=mNlKwhH0KNP4ubUt",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/bolivia/cliza.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.cliza_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Cochabamba':
        return 'El Cristo más grande! More to come!', \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/Hhw77jS-VgE?si=mNlKwhH0KNP4ubUt",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/bolivia/cochabamba.JPG"},
                    {"src": "assets/bolivia/cochabamba1.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.cocha_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Bosnia & Herzegovina
    if value == 'Medjugorje':
        return 'Very small city in B&H where a miracle happened around 30 years ago -- five children saw a vision ' \
               'of the Blessed Mother. Even with many people suspicious of the vision, the stories of the ' \
               'children all align perfectly. One of the children (now an adult) still has her vision daily and ' \
               'has devoted her life to sharing her experiences with Catholics who make the journey or pilgrimage ' \
               'to visit Medjugorje. It was quite the moving experience. This is an easy day trip from Mostar. ', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/bosnia/medj.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.medj_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Mostar':
        return 'more info coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/bosnia/mostar2.JPG"},
                    {"src": "assets/bosnia/mostar1.JPG"},
                    {"src": "assets/bosnia/mostar3.JPG"},
                    {"src": "assets/bosnia/mostar.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.mostar_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Bulgaria
    if value == 'Sofia':
        return 'The Bulgarian capital! The history here is really interesting. People have inhabited modern-day ' \
               'Sofia for some 6000 years. Rather than an old town, here you have different layers of the city. ' \
               'In the center of the city you can find a number of Roman ruins below the current level of the city. ' \
               'There is also a Catholic Church, an Orthodox Church, a Mosque, and a synagogue all around the main ' \
               'square as well. Bulgaria is the only country that never ended up losing any of their Jewish ' \
               'population in WW2. They continued to delay their deportation to concentration camps until the ' \
               'Nazis became too occupied with the war itself as they began to lose the war. The history here is ' \
               'cool but the center is honestly quite dirty and not too aesthetically pleasing. The main park of ' \
               'the city is quite nice though, with the national theater. Close by here there are two other really ' \
               'beautiful orthodox churches, one of them being the main one that is likely the most famous landmark ' \
               'in Sofia. The food is quite good — go to ___ for a casual but delicious and cheap meal. Get the ' \
               'kebapcha (caseless sausages with actually some of the best potatoes I’ve ever had).', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/bulgaria/sofia.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.sofia_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Varna':
        return "I would so highly recommend this little gem of a city on the Black Sea. Enjoy the beaches and the " \
               "cheap prices. This is probably the cheapest place I’ve ever been in Europe. The most expensive " \
               "beers I saw were at a craft brewery — and they were just 2.50 Euros! The beach is beautiful. Go to " \
               "the beach club called ’Moonlight.’ You can get all-day access to the club for just 5 euros. You get " \
               "to use the beach chairs, umbrellas, pool (with natural hot spring water), a 1.5L bottle of water, " \
               "and a beer! Absolutely crazy. You can " \
               "eat here or there are a number of other cafes and bars on the beach. Walk around the port as well. " \
               "‘Craft Beer and Meats’ is on the water at the port. I got to watch a Bulgarian soccer game on TV " \
               "while enjoying sea bass, calamari, and a really good NEIPA (I don’t know what it is about IPAs in " \
               "the Balkans but I really like them — also technically Bulgaria is not in the Balkans but close " \
               "and the taste was similar). You can also stroll through the park area by the beach and down " \
               "the main tourist / shopping street, it’s very nice as well. The main cathedral of the city " \
               "is also really impressive. Lastly, as mentioned with the hot spring water pool above, Varna " \
               "had been settled by the Romans long ago precisely because of the natural hot springs here. " \
               "There are still remains from Roman baths here, and there are several places you can still bathe " \
               "in the hot spring water.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/bulgaria/varna.JPG"},
                    {"src": "assets/bulgaria/varna1.JPG"},
                    {"src": "assets/bulgaria/varna2.JPG"},
                    {"src": "assets/bulgaria/varna7.JPG"},
                    {"src": "assets/bulgaria/varna3.JPG"},
                    {"src": "assets/bulgaria/varna4.JPG"},
                    {"src": "assets/bulgaria/varna5.JPG"},
                    {"src": "assets/bulgaria/varna6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.varna_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Canada
    if value == 'Banff':
        return 'The color of the lake is really stunning! More to come!', \
                html.Br(), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.banff_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Calgary':
        return 'Cool, clean city! More to come!', \
                html.Br(), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.calgary_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Chile
    if value == 'Puerto Natales (Patagonia)':
        return 'One of the southernmost cities in the world! If you are going to Torres del Paine National Park,' \
                'you will likely fly here and stop here before (and after) your time in the park. ' \
                'The airport is quick and cheap 10 minute ride to / from the city. The park is farther, ' \
                'about a 1.5-2 hour drive from Puerto Natales, but there are multiple bus options for this. ' \
                'In Puerto Natales, we stayed in the Lili Patagónicos hostel and very much enjoyed it. ' \
                'They offered had hiking and climbing equipment rentals, as well as luggage storage. ', \
               html.Br(), html.Br(), \
                'It’s not a big city, but it has everything you could want and it is very walkable. ' \
                'There is a full grocery store where you can stock up on snacks for your hike, ' \
                'really nice restaurants, and lovely views here as well. Be sure to walk along the water ' \
                'and see the  Monumento al Milodón, the Monumento de la Mano, the Monumento al Viento, ' \
                'and the beautiful mountains in the distance over the water. We really enjoyed the Restaurante el ' \
                'Bote and Mesita Grande restaurants. Be sure to try a couple unique local foods: the guanaco ' \
                'and the centolla crab. Chilean sea bass is also amazing! Lastly, be sure to try the Austral ' \
                'Calafate beer! It is a delicious local beer made with local calafate berries ' \
                '(similar to blueberries).', \
                html.Br(), html.Br(), dbc.Carousel(
                 items=[
                    {"src": "assets/chile/puertonat.JPG"},
                    {"src": "assets/chile/puertonat1.JPG"},
                    {"src": "assets/chile/puertonat2.JPG"},
                    {"src": "assets/chile/puertonat3.JPG"},
                    {"src": "assets/chile/puertonat4.JPG"},
                    {"src": "assets/chile/puertonat5.JPG"},
                    {"src": "assets/chile/puertonat6.JPG"},
                 ],
                 interval=2000,
                 ride="carousel",
                 className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.puertonat_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Santiago':
        return 'The capital of Chile! An absolutely beautiful city with the stunning backdrop of the Andes ' \
               'mountains everywhere you look. Be sure to eat lots of ‘parilla’ (grilled meat). You can (and ' \
               'should) enjoy delicious steak dinners for pretty cheap. Also be sure to drink lots of pisco sours… ' \
               'they are so delicious. Pisco is a local liquor invented in Chile (unless you ask a Peruvian). ' \
               'Airbnbs are also very cheap. Definitely go up to ___ to get some stunning views of the city and ' \
               'the mountains. You can take a funicular to get up, and I’d recommend walking down. When walking ' \
               'down, you will come to a big ‘Chile’ sign that is a great photo op with the city in the background, ' \
               'and the large __ tower right in the center. This is the tallest building in South America. I would ' \
               'also recommend going to the top of this building. You get pretty stunning 360 degree views of the ' \
               'city. Cultural appropriation is also encouraged with some traditional Chilean outfits as a photo op! ' \
               'Please let me know if you go — a professor I almost worked for would love to host you for a Chilean ' \
               '‘parilla’ dinner! Dr. Juan Calderón studied in the US and really enjoyed his time there. ' \
               'He hosted my friends and I when we went and it was really lovely. He is a really great guy and ' \
               'he also speaks fluent English. If you are looking for nightlife, I don’t think you will find it. ' \
               'Santiago is lovely but is a bit of a ‘sleepy’ city. Lastly, I would highly recommend a day trip ' \
               'to the coast (Valparaíso / Viña del Mar) and to nearby wine country. Skiing is also a fantastic ' \
               'option if you are there in winter.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/chile/stgo7.JPG"},
                    {"src": "assets/chile/stgo8.JPG"},
                    {"src": "assets/chile/stgo.JPG"},
                    {"src": "assets/chile/stgo2.JPG"},
                    {"src": "assets/chile/stgo6.JPG"},
                    {"src": "assets/chile/stgo4.JPG"},
                    {"src": "assets/chile/stgo1.JPG"},
                    {"src": "assets/chile/stgo5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.sant_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Torres del Paine NP (Patagonia)':
        return '"The W" trail was stunning from start to finish. The Torres on the last morning was an amazing end. ' \
               'About 50 miles in 4 days. The refugios are really fun to stay in. We stayed at Francés the first ' \
               'two nights and then Chileno on the last night. Breakfast and dinner ' \
               'there is a bit expensive but worth it for the convenience. You can bring snacks as lunch and to get ' \
               'you through the day until dinner. There are tons of rivers and streams with freshly melted glacier ' \
               "water that you can drink, so you don't need to bring any water with you. This was really nice. " \
               "End of September was a good time to go as it wasn't too hot as winter just ended and " \
               "there weren't too many tourists yet. You can also catch the end of ski season in the Andes as well! " \
               "Also the southern-most game of beer die ever was played in this park in Sept 2022.", \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   # style={"width": "55%", "padding": "0px", 'margin': 'auto'},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/eQe3kmo47b8",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), html.Br(), \
               dbc.Carousel(
                   items=[
                       {"src": "assets/chile/patagonia9.JPG"},
                       {"src": "assets/chile/patagonia.JPG"},
                       {"src": "assets/chile/patagonia2.JPG"},
                       {"src": "assets/chile/patagonia1.JPG"},
                       {"src": "assets/chile/patagonia5.JPG"},
                       {"src": "assets/chile/patagonia6.JPG"},
                       {"src": "assets/chile/patagonia7.JPG"},
                       {"src": "assets/chile/patagonia8.JPG"},
                       {"src": "assets/chile/patagonia3.JPG"},
                       {"src": "assets/chile/patagonia10.JPG"},
                   ],
                   interval=2000,
                   ride="carousel",
                   className="carousel-fade"
               ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.torres_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Valparaíso / Viña del Mar':
        return 'Enjoy the beautiful coastline and eat the fresh ceviche from the oceanside marketplace. WOW !!!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/chile/valpo3.JPG"},
                    {"src": "assets/chile/valpo1.JPG"},
                    {"src": "assets/chile/valpo2.JPG"},
                    {"src": "assets/chile/valpo4.JPG"},
                    {"src": "assets/chile/valpo5.JPG"},
                    {"src": "assets/chile/valpo6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.valpa_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Valle Nevado':
        return 'Stunning views of the Andes mountains! Remember that the seasons in the southern hemisphere are ' \
                'flipped, so ski season goes ' \
               'from maybe May to September. We were able to ski Valle Nevado resort for free as it is on ' \
                'the Ikon pass! A lot of people ' \
               'come up from Santiago just for the day to ski (via shuttle), ' \
               'but there are some pretty cheap Airbnbs on ' \
               'the mountain as well. We saw one of the most incredible sunsets our one night on the mountain. ' \
               'If you are going to stay a night or two on the mountain, make sure your Airbnb is accessible ' \
               'from the resort where you are skiing! There are multiple resorts on the Valle Nevado mountain ' \
               'and there is really no way to get from one side of the mountain to the other ' \
               'as there are no Ubers / taxis on the mountain.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/chile/vn.JPG"},
                    {"src": "assets/chile/vn1.JPG"},
                    {"src": "assets/chile/vn2.JPG"},
                    {"src": "assets/chile/vn3.JPG"},
                    {"src": "assets/chile/vn4.JPG"},
                    # {"src": "assets/chile/vn5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.valle_nevado_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Croatia
    if value == 'Dubrovnik':
        return 'One of the coolest cities I have ever been to. Stay near or in the old town. The old city walls of ' \
               'the old town look straight out of a movie (and they are -- there has been a lot of filming here in ' \
               'recent years, including Game of Thrones and The Last Jedi). Construction of the walls began way ' \
               'back in the 7th century and still look epic with the big draw bridge in the front and the sea port ' \
               'in the back. Be sure to also climb (there is also a funicular) to the top of the city to see the ' \
               'old town from above and to see a stunning sunset over the water. There are also multiple spots ' \
               'to go swimming! Summer is great for swimming and boating, but shoulder season ' \
               '(I went in mid-October) still offers lovely warm (but not hot) temperatures and many fewer tourists ' \
               'as there are fewer flights.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/dubrovnik.JPG"},
                    {"src": "assets/croatia/dubrovnik1.JPG"},
                    {"src": "assets/croatia/dubrovnik2.JPG"},
                    {"src": "assets/croatia/dubrovnik3.JPG"},
                    {"src": "assets/croatia/dubrovnik6.JPG"},
                    {"src": "assets/croatia/dubrovnik7.JPG"},
                    {"src": "assets/croatia/dubrovnik8.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.dubrovnik_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Plitvice Lakes National Park':
        return 'Really beautiful. It provides a nice contrast to the coastal cities you will likely in Croatia.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/np.JPG"},
                    # {"src": "assets/croatia/np5.JPG"},
                    # {"src": "assets/croatia/np6.JPG"},
                    # {"src": "assets/croatia/np7.JPG"},
                    # {"src": "assets/croatia/np8.JPG"},
                    # {"src": "assets/croatia/np9.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.plitvice_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Pula':
        return "Definitely worth a stop. There's a very old Roman arena and nice little port. There are some cool" \
               "shops and restaurants as well. The view of the city " \
               "from the water / parking lot when you enter the city is beautiful as well. This peninsula (called " \
               "Istria) is so " \
               "fertile and provides great conditions for grapes, olives, and black truffles. Sample frequently!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/pula2.JPG"},
                    {"src": "assets/croatia/pula3.JPG"},
                    {"src": "assets/croatia/pula4.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.pula_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Motovun':
        return "What a fun, unique experience. Would definitely recommend truffle hunting with a local and their " \
               "dogs! Often times, truffle hunting has run in a family for generations as it takes a lot of effort " \
               " to train the dogs -- it is best when they are trained since birth and there is another already " \
               "trained dog in the house to learn from. We had a great guide and the truffle-focused meal we had " \
               "afterwards was incredible.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/truffles4.JPG"},
                    {"src": "assets/croatia/truffles5.JPG"},
                    {"src": "assets/croatia/truffles7.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.motovun_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Vodnjan':
        return "Olivessss! more to come!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/olives.JPG"},
                    {"src": "assets/croatia/olives4.JPG"},
                    {"src": "assets/croatia/olives3.JPG"},
                    {"src": "assets/croatia/olives2.JPG"},
                    {"src": "assets/croatia/olives1.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),
    if value == 'Opatija':
        return "Just made a quick stop here to watch the sunset, walk by the water, and have a wonderful dinner " \
               "at Valle Losca Tavern. Amazing sunset and amazing meal! I had stingray for dinner and wow it was " \
               "really good. Very cute small town on the water. ", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    # {"src": "assets/croatia/opa.JPG"},
                    # {"src": "assets/croatia/opa2.JPG"},
                    {"src": "assets/croatia/opa3.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.opatija_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Rovinj':
        return "One of the most picturesque towns I've ever seen, especially from the port. The view of the city " \
               "from the water / parking lot when you enter the city is beautiful as well. This peninsula is so " \
               "fertile and provides great conditions for grapes, olives, and black truffles. Sample frequently.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/rov4.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),
    if value == 'Zagreb':
        return 'Cool to see the Croatian capital with more of the Germanic influences, compared to the more Italian ' \
               'feel on the coast.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/croatia/zagreb.JPG"},
                    {"src": "assets/croatia/zagreb1.JPG"},
                    {"src": "assets/croatia/zagreb2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.zagreb_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Czechia
    if value == 'Prague':
        return 'One of my favorite cities! It is relatively cheap compared to more western European capital cities ' \
               "definitely has a different feel. Stay near the old town. The city is very walkable and you shouldn't " \
               "really need any taxis or public transport to get around. Your first stop should be " \
               "the main square in the old town, with the world's oldest functioning astrological clock and a really " \
               "cool gothic church called the Church of Our Lady Before Tyn. There is also a really nice Christmas " \
               "market here in the winter. The next main attraction is the " \
               "Charles Bridge. After crossing the bridge, climb up to the Prague Castle and explore the castle " \
               "grounds. A boat ride on the river is also a fantastic idea any time of year. ", \
               html.Br(), html.Br(), \
               "The Czech Republic is very well known for their beer. The Czechs drink by far the most " \
               "beer in the world -- approximately 500 12-ounce beers per person per year! No other country " \
               "drinks more than one beer per person per day! There are a few beers you will commonly see " \
               "throughout the city. First, Pilsner Urquell -- this is the original pilsner-style beer, " \
               "and the name of the style itself comes from the Czech city where this beer was brewed, called Plzen. " \
               "BE SURE to try a fresh Pilsner Urquell on draft from a bronze tank -- you will thank me later!" \
               "Next is Staropramen -- also a good beer. Be sure to try the Staropramen Unfiltered! Then there is " \
               "Budweiser -- no, not from St Louis. Someone from Anheuser Busch came to the Czech Republic to " \
               "learn more about brewing and tried the original Budweiser. The guy liked the name and found " \
               "out that the brewery, despite having brewed beer for nearly a thousand years, had never " \
               "filed a patent on the " \
               "name. He naturally then filed a patent and gave the same name to the St. Louis Budweiser. So -- " \
               "be sure to try the real Budweiser!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/czechia/prg.JPG"},
                    {"src": "assets/czechia/prg1.JPG"},
                    {"src": "assets/czechia/prg2.JPG"},
                    {"src": "assets/czechia/prg3.JPG"},
                    {"src": "assets/czechia/prg4.JPG"},
                    {"src": "assets/czechia/prg5.JPG"},
                    {"src": "assets/czechia/prg6.JPG"},
                    {"src": "assets/czechia/prg7.JPG"},
                    {"src": "assets/czechia/prg8.JPG"},
                    {"src": "assets/czechia/prg9.JPG"},
                    {"src": "assets/czechia/prg10.JPG"},
                    {"src": "assets/czechia/prg11.JPG"},

                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.prague_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Denmark
    if value == 'Copenhagen':
        return ('The capital of Denmark! It is very fun to walk or bike around this city as it is full of parks '
                'and waterways. My mom and I really enjoyed a bike tour of the city! '
                'Be sure to walk around Nyhaven and see the most famous view of the city! '
                'Perhaps the next most famous sight to see is The Little Mermaid statue. '
                'The statue itself is actually quite small, but it is still fun to see. A visit to the '
                'Carlsberg brewery is very fun. Don’t be alarmed by the swastikas on the elephants as you '
                'enter the brewery — they have been there long before WW2! The swastika is an ancient '
                'symbol of good fortune, not something created by Nazi Germany. Very close by to Carlsberg are '
                'the beautiful Frederiksberg Gardens -- beautiful, massive city park with the Frederiksberg Palace. '
                'Be sure to also see the Christiansborg Palace, the Rosenborg Castle, and the Amalienborg Castle -- '
                "this is the residence of the Danish Royal Family to this day! It's fun to see the guards dressed "
                'up in uniform outside guarding the palace. The Tivoli Garden is also '
                'worth a visit, and they decorate it depending on the season. It is a theme / amusement park, with '
                'tons of food, drink, shopping, and even rollercoaster options inside. '
                'We saw it in fall / Halloween theme! Lastly, '
                'a great casual place for food and drink and board games is the Bastard Cafe.'), \
                html.Br(), html.Br(), \
               ('I visited from Kiel, and I loved my train ride here! The train from Germany goes across '
                'the German island of Fehmarn and drives onto a ferry, which then crosses the Baltic Sea to '
                'reach Denmark! While on the ferry, you can get off the train and enjoy the views from the '
                'boat deck — just don’t forget to get back on the train before it drives off the boat! I was '
                'enjoying the views as we approached Denmark and almost didn’t get back on in time! '), \
                html.Br(), html.Br(), \
               ('(Note: an underwater tunnel is actually being built right now, so soon the train will '
                'make this journey via this tunnel rather than via ferry)'), \
                html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/denmark/cop.JPG"},
                    {"src": "assets/denmark/cop1.JPG"},
                    {"src": "assets/denmark/cop2.JPG"},
                    {"src": "assets/denmark/cop11.JPG"},
                    {"src": "assets/denmark/cop4.JPG"},
                    {"src": "assets/denmark/cop5.JPG"},
                    {"src": "assets/denmark/cop6.JPG"},
                    {"src": "assets/denmark/cop7.JPG"},
                    {"src": "assets/denmark/cop8.JPG"},
                    {"src": "assets/denmark/cop12.JPG"},
                    {"src": "assets/denmark/cop9.JPG"},
                    {"src": "assets/denmark/cop3.JPG"},
                    {"src": "assets/denmark/cop10.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.copen_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Ecuador
    if value == 'Quito':
        return 'more info to come!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.quito_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Galapagos Islands':
        return "Maybe the coolest place I've ever been. Week-long cruise with daily snorkeling. We saw penguins, " \
               "sea lions, sting rays, sharks, and more sea turtles than you could ever imagine.", \
                html.Br(), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.galapagos_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# England
    if value == 'London':
        return "Yes it can be expensive but it is a really great city. Tons of history and of course... " \
               "the world mecca for football. Currently (2023-24), 7 of the 20 teams in the English Premier League " \
               "(the best league in the world) are in London. The atmosphere at second league (called " \
               "The Championship) games is also really fun and a lot cheaper than Premier League games. QPR is a " \
               "second league team in London -- their games are so fun! It's a completely different feel than a  " \
               "top league game as the stadium is much smaller and there are very few tourists at the games." \
               "During the season or in summer, also consider doing a stadium tour of a Premier League team. My " \
               "biased opinion would be Arsenal's Emirates Stadium (GO GUNNERS !) ", \
               html.Br(), html.Br(), \
               "Beyond football, be sure to go to Big Ben, Buckingham Palace, Harrod's (try a meat pie), " \
               "and Tower Bridge. Many people think that Tower Bridge is London Bridge, but no -- the famous pic is " \
               "from the south side of the River Thames between London Bridge and Tower Bridge. Be sure to walk " \
               "across the Tower Bridge as well." \
               "Also enjoy Hyde Park (a bike ride here is great). One of the best areas in the city is " \
               "Camden Market. The area is cute with some little canals, and there are tons of " \
               "stands / vendors. You can find just about any cuisine here. Enjoy some food and drinks here. ", \
               html.Br(), html.Br(), \
               "There is a lot of great beer in London. There are lots of awesome " \
               "old-timey pubs: The Toucan, The Cross Keys, The Harp, The Seven Stars, The Blackfriar, and more. " \
               "Hop Locker is also a sweet beer bar by the river. " \
               "Many pubs and bars will also have a good fish & chips. Make sure to try some cask ales / real ales. " \
               "They are known as Britain's national drink. It's a unique beer style to the UK. But be warned, " \
               "the beers are not served very cold. The idea is so you can taste " \
               "the flavors more (which is scientifically true). If you like Guinness, " \
               "try the London Black beer -- it's a modern take on an old English style dark porter. If you have " \
               "time, there is a whole strip of breweries (Brew by Numbers, Anspach & Hobday, and more) all right " \
               "under the train, it's a cool setup. ", \
               html.Br(), html.Br(), \
               "So... lots to do here. I could definitely live here!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/england/london.JPG"},
                    # {"src": "assets/england/london6.JPG"},
                    {"src": "assets/england/london7.JPG"},
                    {"src": "assets/england/london3.JPG"},
                    # {"src": "assets/england/london4.JPG"},
                    {"src": "assets/england/london1.JPG"},
                    {"src": "assets/england/london8.JPG"},
                    # {"src": "assets/england/london5.JPG"},
                    {"src": "assets/england/london2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                    html.Div(
                        dl.Map([dl.TileLayer(),
                                dl.GeoJSON(data=coordinates.london_geojson)],
                               style={'height': '35vh', 'max-width': "400px", "margin": "auto"},
                               center=[25, -40], zoom=1))

# France
    if value == 'Colmar':
        return 'Colmar may be small but it really goes all out for Christmas. It is a really cute little city, and ' \
               'it is wild how many tourists come to visit the Christmas markets. If you have the time, it ' \
               'is definitely worth a day trip from Strasbourg. The French architect that designed the Statue of ' \
               'Liberty is from here, and there is actually a small replica of the statue that welcomes you as ' \
               'you enter the city!', \
               html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.colmar_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Paris':
        return 'It is expensive and many people prefer other parts of France... but worth it to see Messi! JK ' \
               'there is also plenty to do besides see Messi. Of course visit the Eiffel Tour -- catch some great ' \
               "views from train line 6. Also be prepared for the little 'light show' that happens " \
               "on the hour after the sun goes down. Also visit Arc de Triomphe (go to the top " \
               "on a clear day for awesome views), the Champs-Élysées street for " \
               "shopping, and the Louvre (where Mona Lisa lives). You could " \
               'spend days in the Louvre so have an idea of what you want to see. Definitely explore the Montmarte ' \
               'neighborhood. Go to the Sacré-Cœur Basilica. The steps in front are a great place to sit with some ' \
               'wine and enjoy a sunset. The area right next to the basilica also has a really unique vibe, almost ' \
               'like a ski town. The rest of Montmarte below the basilica is also really nice. Eat a crepe at one ' \
               "the Breizh Cafes. Also get a crepe on the street at some point. Stop by little cafes for awesome " \
               "croissants and other baked goods as well. " \
               "And most important of all... go to Le Relais de l'Entrecote for amazing " \
               "steak frites. There are no reservations. As you can see below, the line can legitimately be an " \
               "hour plus sometimes so get " \
               "there early. Consider also going for lunch (or right when they open) to avoid lines. Lastly, Cafe de " \
               "Flore (pictured below) is a famous spot -- but be aware it is very expensive. A picture outside " \
               "and eating somewhere " \
               "else may do the trick!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/france/paris1.JPG"},
                    {"src": "assets/france/paris8.JPG"},
                    {"src": "assets/france/paris.JPG"},
                    {"src": "assets/france/paris3.JPG"},
                    {"src": "assets/france/paris2.JPG"},
                    {"src": "assets/france/paris4.JPG"},
                    {"src": "assets/france/paris6.JPG"},
                    {"src": "assets/france/paris7.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.paris_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Strasbourg':
        return 'Known as the ‘Capital of Christmas,’ Strasbourg is quite magical for Christmas. There are so many ' \
               'lights and markets all over the city. Christmas season or not, be sure to walk around the ‘Petite ' \
               'Paris’ area. It is really cute. More recs to come___. A day trip to Colmar is also a great idea, ' \
               'especially during Christmas time.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/france/strasbourg.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.stras_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Germany
    if value == 'Berlin':
        return "'Poor but sexy' has become the city's motto after the mayor said this back in 2003. " \
               "There is never a dull moment in Berlin. It's a very creative, unique, fun, and often quirky city " \
               "with lots of history. " \
               "There is so much to see, especially the Brandenburg Gate, the Berliner Dom (cathedral), the " \
               "Reichstag (national parliament), the Fernsehturm (TV tower), the Memorial to the Murdered Jews of " \
               "Europe, and the East Side Gallery (section of Berlin wall with famous murals). There are many " \
               "famous museums as well, many are right in the center of the city on Museum Island.", \
               html.Br(), html.Br(), \
               "For the artistic side of the city -- the club scene (especially techno) is world famous. Berghain " \
               "is the most famous club in Berlin (and maybe the world). It opens Friday " \
               "night and does not close until noon on Monday. If you want to go, be prepared " \
               "to wait a long time in line and know that there is a good chance you will not be let in -- it's part " \
               "of the funky culture that preserves the hype and exclusive aura of the club. For other club " \
               "options, try Watergate, Tresor, Club der Visionäre, or Ritter Butzke. For a really fun bar that " \
               "isn't exactly a club, go to Minimal bar. ", \
               html.Br(), html.Br(), \
               "Beyond the clubs, " \
               "there are tons of concerts here every day and there are always " \
               "people playing music on the streets (especially on the Admiralbrücke and around Museum Island). " \
               "Lots of fun bars as well -- there's an amazing rooftop at Klunkerkranich. Find great craft beer and " \
               "a good time at Kaschk, Muted Horn, Hops & Barley, Protokoll, and Straßenbräu. Berlin (randomly) " \
               "has so many beaches -- there are many sand volleyball courts and beach bars in parks and on " \
               "on the rivers around the city. However, " \
               "to get to a proper beach you need to travel out of the city a bit -- the Wannsee has maybe the " \
               "best beach. There are so many parks, including maybe the coolest park ever, which is an old airport " \
               "that has now become a massive park right in the city. Other great parks include Treptower Park, " \
               "Park am Gleisdreieck, Viktoriapark, and Körnerpark. " \
               "There are lots of sports here as well (to watch and play). The pro " \
               "basketball (Alba), soccer (2 teams: Hertha and Union), handball (Füchse), and ice hockey (Eisbären) " \
               "games all provide a very fun atmosphere. ", \
               html.Br(), html.Br(), \
               "Be sure to eat a döner kebab (a variation of a Turkish " \
               "kebab that originated in Berlin -- the best place is Nefi's), currywurst (Curry 36 is great), and " \
               "vietnamese food (the duck at New Day is crazy good). For German food, 'Max & Moritz' is a " \
               "really cool restaurant with great food and beers. There is also the Hofbräuhaus Berlin for very " \
               "fun and festive Bavarian food, beers, live music, and good vibes. There is also a lot of " \
               "great middle eastern food, especially yemenite food at the 'Jemenitisches Restaurant' " \
               "and Syrian food at the 'Aleppo Supper Club.' And last but definitely not least -- Christmas " \
               "time is magical here! There are tons of Christmas markets all over the city, and mulled wine " \
               "(Glühwein) also available all over the city.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/berlin10.JPG"},
                    {"src": "assets/germany/berlin.JPG"},
                    {"src": "assets/germany/berlin2.JPG"},
                    {"src": "assets/germany/berlin3.JPG"},
                    {"src": "assets/germany/berlin1.JPG"},
                    {"src": "assets/germany/berlin5.JPG"},
                    {"src": "assets/germany/berlin6.JPG"},
                    {"src": "assets/germany/berlin7.JPG"},
                    {"src": "assets/germany/berlin4.JPG"},
                    {"src": "assets/germany/berlin8.JPG"},
                    {"src": "assets/germany/berlin9.JPG"},
                    {"src": "assets/germany/berlin11.JPG"},
                    {"src": "assets/germany/berlin12.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.ber_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1)),
    if value == 'Cologne':
        return "Known officially as Köln in German -- and known unofficially as the 'Carnaval city,' " \
               "I would have guessed it was February if I didn't know any better! (I went in September) " \
               "There were so many bachelor / bachelorette parties happening, and so many people " \
               "dressed in all kinds of costumes. I had really nice summer weather when I went, and the entire " \
               "city was full of people, especially in the old town, which was originally established by the " \
               "Romans. There are several huge gates to the old city that still stand today. " \
               "Right in the center of the city, you'll see the very famous, very big " \
               "gothic-style Cologne Cathedral (Kölner Dom in German). Entry is free! It is really impressive.", \
               html.Br(), html.Br(), \
               "Also in the center of the city, there are several famous Cologne beer halls / taverns, serving " \
               "the light, easy-drinking Cologne-style beer (Kölsch). There is really great atmosphere and culture " \
               "inside, especially in Brauhaus Früh am Dom, Peters Brauhaus, Brauhaus Zum Prinzen, " \
               "and Brauerei zur Malzmühle. For the most lively atmosphere, go to Gaffel am Dom!" \
               "Kölsch beer is always served in small glasses, and the waiters come by " \
               "each table frequently with more fresh beers to replace the empty glasses. When you've had enough, " \
               "be sure to put your coaster on top of your glass, otherwise the waiter will keep bringing you more!", \
               html.Br(), html.Br(), \
               "Be sure to also enjoy the waterfront along the Rhine river (Rhein in German). There is a nice cafe " \
               "where you can find a beer or coffee overlooking the river, called Hafenterasse. Be sure to also " \
               "make your way to the other side of the river, where you will get an amazing view of the city with " \
               "the cathedral towering over it. Lastly, there is also a nice park with a small lake called Hiroshima-" \
               "Nagasaki-Park. On a nice day you will find plenty of people at the 'Biergarten am Aachener Weiher!'", \
                html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/koln.JPG"},
                    {"src": "assets/germany/koln7.JPG"},
                    {"src": "assets/germany/koln1.JPG"},
                    {"src": "assets/germany/koln2.JPG"},
                    {"src": "assets/germany/koln3.JPG"},
                    {"src": "assets/germany/koln4.JPG"},
                    {"src": "assets/germany/koln5.JPG"},
                    {"src": "assets/germany/koln6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.koln_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1)),
    if value == 'Düsseldorf':
        return "I was only here briefly, but the center of the city was very lively with many bars and restaurants! " \
               "The waterfront along the Rhine river (Rhein in German) was also nicely developed with a number of " \
               "bars and restaurants overlooking the water.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/duss.JPG"},
                    {"src": "assets/germany/duss1.JPG"},
                    {"src": "assets/germany/duss2.JPG"},
                    {"src": "assets/germany/duss3.JPG"},
                    {"src": "assets/germany/duss4.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.duss_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1)),
    if value == 'Dortmund':
        return "Home to Borussia Dortmund! Go to a football game. It's known to be one of the best game atmospheres " \
               "in the world. I have been lucky to see Dortmund and the German national team play here! Both games " \
               "were so much fun, especially since both resulted in wins for the home team! At the Westfalenstadion," \
               "they also have the coolest 'Herrenhandtasche,' literally 'man's handbag' in English (picture below).", \
               html.Br(), html.Br(), \
               "The Christmas market is also amazing! It is one of the biggest Christmas markets in the world, " \
               "and actually has the largest natural Christmas 'tree' in the world. I say 'tree' because " \
               "it's actually some 1,700 trees put together to make one tree that is over 150 feet tall! ", \
               html.Br(), html.Br(), \
               "The main plaza in the city, Hansaplatz, has some great restaurants and bars, including Wenkers " \
               "am Markt." \
               "Lastly, there is a newly developed area of the city called Phoenix that is so nice! It used to be " \
               "an industrial area before being completely transformed. There is a lake in the middle of this " \
               "neighborhood that is surrounded by bars, restaurants, cafes, and impressive houses. There is also " \
               "a walking and biking path that goes around the lake. Lastly, there is a large hill that you can " \
               "climb to get a great view of the sunset, the neighborhood, the city of Dortmund, and of the " \
               "Westfalenstadion!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/dor1.JPG"},
                    {"src": "assets/germany/dor6.JPG"},
                    {"src": "assets/germany/dor.JPG"},
                    {"src": "assets/germany/dor7.JPG"},
                    {"src": "assets/germany/dor5.JPG"},
                    {"src": "assets/germany/dor2.JPG"},
                    {"src": "assets/germany/dor3.JPG"},
                    {"src": "assets/germany/dor8.JPG"},
                    {"src": "assets/germany/dor9.JPG"},
                    {"src": "assets/germany/dor4.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.dort_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1)),
    if value == 'Dresden':
        return 'Home to one of the biggest and most amazing Christmas markets in the world. The medieval Christmas' \
               "market is also really cool. Be sure to try the 'Handbrot.' A famous dessert from here " \
               "during Christmas is Stollen (sometimes called Christstollen). The one with marzipan in the " \
               "middle is sooo good. You can come here on a day trip from Berlin.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/dresden_new.JPG"},
                    {"src": "assets/germany/dresden.JPG"},
                    {"src": "assets/germany/dresden2.JPG"},
                    {"src": "assets/germany/dresden3.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.dresden_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Flensburg':
        return 'Really cute port city just south of the Denmark border. Also home to the Flensburger brewery! ' \
                'The tour is really cheap (was only 10 euros in 2017!) and you get ' \
               "a lot of food and beer afterwards! They have the best marketing ever.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/flens.JPG"},
                    {"src": "assets/germany/flens1.JPG"},
                    {"src": "assets/germany/flens2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),  html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.flens_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Gengenbach':
        return 'Largest advent calendar in the world! Really nice small town in the middle of the Black Forest. ' \
               'Absolutely worth a stop during Christmas time.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/gengenbach.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.geng_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Hamburg':
        return 'A beautiful city in the north of Germany. The port of Hamburg is bigger than the entire city of ' \
               'Copenhagen. There are also more bridges than Amsterdam, Venice, and London combined! If you like ' \
               'seafood you are in luck, the fresh fish sandwiches (Fischbrötchen) are so good -- go to Brücke 37 ' \
               'at the port. Also at the port you will see the iconic new concert hall called the Elbphilharmonie, ' \
               'with its roof resembling and reflecting the waves of the water below. Go up to the top of the ' \
               'nearby church, ____ to get great views of the port and of the concert hall. Be sure to walk ' \
               'through the Speicherstadt, the beautiful storage area for all incoming goods coming by boat ' \
               'to the city. Have a drink at the little castle in this area, called the Wasserschloss. Also be sure ' \
               'to visit the Hamburger version of the Amsterdam red light district, St. Pauli. ' \
               'Different than Amsterdam though in that this was formerly the outside of the city of Hamburg ' \
               'and thus became the more expressive and creative area, with music, art, and bars ' \
               '(and also prostitution). There are tons of fun bars and clubs' \
               'here. The Beatles wrote their first album here and have actually played more shows in ' \
               'St. Pauli than anywhere else in the world. The football team has also gained a cult ' \
               'following worldwide as they really represent the ' \
               'neighborhood well -- as a foil to the historically much more successful Hamburger SV, supporting the ' \
               'LGBTQ community by wearing a rainbow captain armband, and by often making demonstrations for various ' \
               'human rights issues. I had so much fun at the game I went to, and you can see in the picture below ' \
               'there was a big sign saying "Kein Mensch ist illegal," or in english "No person is illegal." ' \
               'Go to a game if you can!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/ham.JPG"},
                    {"src": "assets/germany/ham1.JPG"},
                    {"src": "assets/germany/ham2.JPG"},
                    {"src": "assets/germany/ham3.JPG"},
                    {"src": "assets/germany/ham4.JPG"},
                    {"src": "assets/germany/ham5.JPG"},
                    {"src": "assets/germany/ham6.JPG"},
                    {"src": "assets/germany/ham7.JPG"},
                    {"src": "assets/germany/ham8.JPG"},
                    {"src": "assets/germany/ham9.JPG"},
                    {"src": "assets/germany/ham10.JPG"},
                    {"src": "assets/germany/ham11.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.ham_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Kiel':
        return 'My home on the coast of the Baltic Sea for a about a half a year after college! ' \
               'Definitely not the most happening city in Germany ' \
               'in terms of bars / restaurants / clubs, but wow that could not be farther from the truth ' \
               'during Kiel Week (Kieler Woche) in the summer. This 10 day festival is one of the coolest events ' \
               "I've ever seen -- what started as (and still is) an international sailing festival has become " \
               "a city wide celebration and their biggest parties of the year. The coast is lined with bars and " \
               "DJ stages, there is a big international market on the main square of the city in front of the " \
               "town hall (Rathaus) with with each stand/hut serving food and drinks from a different " \
               "country from all over the world. There are also sailing competitions, boat cruises," \
               " hot air balloons, hot air balloon light shows, and incredible fresh fish sandwiches " \
               "(Fischbrötchen) everywhere you go. The rest of the year, Kiel is definitely calmer " \
               "but there are some nice beaches and it is a really" \
               "nice, cute little city. Lastly (and randomly), Kiel has one of the most " \
               "successful handball teams in the world. The handball games are actually pretty electric.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/kiel13.JPG"},
                    {"src": "assets/germany/kiel.JPG"},
                    {"src": "assets/germany/kiel2.JPG"},
                    {"src": "assets/germany/kiel3.JPG"},
                    {"src": "assets/germany/kiel11.JPG"},
                    {"src": "assets/germany/kiel12.JPG"},
                    {"src": "assets/germany/kiel4.JPG"},
                    {"src": "assets/germany/kiel5.JPG"},
                    {"src": "assets/germany/kiel6.JPG"},
                    {"src": "assets/germany/kiel7.JPG"},
                    {"src": "assets/germany/kiel8.JPG"},
                    {"src": "assets/germany/kiel1.JPG"},
                    {"src": "assets/germany/kiel9.JPG"},
                    {"src": "assets/germany/kiel10.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.kiel_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Leipzig':
        return 'Both the new and old Rathaus (town hall) are really cool. ', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/leipzig.JPG"},
                    {"src": "assets/germany/leipzig2.JPG"},
                    {"src": "assets/germany/leipzig1.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.leip_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Lübeck':
        return 'Home to some of the best marzipan in the world. I actually only played a basketball game here ' \
               "(we won). It's supposed to be very cute and have a really nice Christmas market.", \
                html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.lub_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Munich':
        return 'If you like to have fun and drink beer then Oktoberfest is ' \
               'a must at some point. Munich is where the one true Oktoberfest is held (cash only FYI). ' \
               'There are other celebrations around Germany but nothing compares to the real deal. ' \
               'I would absolutely recommend going once! Each tent holds thousands of people, ' \
               'and with all the people, music, food, and beer it really is quite the amazing and unique experience.', \
               html.Br(), html.Br(), \
               'Beyond Oktoberfest -- it is ' \
               'the capital of Bavaria. Very pretty city. Bavaria is home to some beautiful mountains (the Alps), ' \
               'the fairytale-like castle called Neuschwanstein that inspired the Disney castle, one of the ' \
               'most successful (but annoying) football teams in the world in Bayern Munich, ' \
               'and also home to some of the best beers in the world. ' \
               "Some of Bavaria's most delicious " \
               '(and most unique) beers are the wheat beers (Weissbier / Weißbier / Hefeweizen). ', \
               html.Br(), html.Br(), \
               'There are some absolutely beautiful lakes ' \
               'up in the Alps that are easy day trips from Munich (especially if you rent a car). ' \
               'Jochberg is an awesome hike with stunning views of the Alps, Kochelsee lake, and Walchensee lake ' \
               '(photo below). Back in Munich, '\
               'the Englischer Garten park is beautiful -- ' \
               "it's fun to watch people surf here on a little artificial wave canal and there " \
               "is a really cool beer garden at the base of the Chinese Tower. You have to visit " \
               "the Hofbräuhaus as well - the most iconic beer hall in the world. There is always " \
               "live music and the vibes are immaculate. " \
               "It was originally founded as the royal brewery and for hundreds of " \
               "years it has been the primary gathering place in the city, even for political matters. The Nazi " \
               "party was actually officially established here, and not long after Hitler was officially named " \
               "the leader of the Nazi party here as well. A couple other great traditional beer halls are " \
               "Augustiner (there are a few locations) and Schneider Bräuhaus. Nearly all of these traditional beer " \
               "halls will offer the wonderful traditional Bavarian breakfast, weißwurst (Bavarian white sausages) " \
               "with pretzels, sweet mustard, and of course a helles beer! Another very traditional Munich food is " \
               "the Schweinshaxe (ham hock). It is a huge piece of pork that is incredibly tender -- definitely " \
               "try it! ", \
               html.Br(), html.Br(), \
               "Lastly, there is some nice shopping " \
               "(and strolling) along Maximilianstraße and Kaufingerstraße near the " \
               "famous and beautiful main square of the city, Marienplatz, where the town hall (Rathaus) is.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/munich10.JPG"},
                    {"src": "assets/germany/munich.JPG"},
                    {"src": "assets/germany/munich1.JPG"},
                    {"src": "assets/germany/munich2.JPG"},
                    {"src": "assets/germany/munich3.JPG"},
                    {"src": "assets/germany/munich4.JPG"},
                    {"src": "assets/germany/munich5.JPG"},
                    {"src": "assets/germany/munich6.JPG"},
                    {"src": "assets/germany/munich7.JPG"},
                    {"src": "assets/germany/munich8.JPG"},
                    {"src": "assets/germany/munich9.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.munich_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Nuremberg':
        return "I really enjoyed this city (spelled Nürnberg in German FYI) in the north of Bavaria! " \
               "Important to note though that this was not always part of Bavaria -- Nuremberg used to be the main " \
               "city of the region of Franconia. You will notice all of the city flags and details around the city " \
               "are red rather than the typical Bavarian blue. Nuremberg holds great significance throughout history " \
               "-- in the Holy Roman Empire and in Nazi Germany. The massive 'Nuremberg rallies' were held just " \
               "outside the city at the Zepellinfeld, which is an easy visit (20 minute bus/tram or 10 minute S-Bahn " \
               "train ride) from Nuremberg. Following WW2, the 'Nuremberg trials' were held here. There is a really " \
               "cool memorial, called the Street of Human Rights, that has big pillars with the Universal " \
               "Declaration of Human Rights written in tons of different languages from across the globe inscribed " \
               "on each. Much of the city was ultimately bombed, but there were relatively very " \
               "few people who died here -- thanks to beer! A large underground cellar and tunnel complex had been " \
               "in use since the 14th century to brew and store beer, and many citizens took shelter here during " \
               "WW2. I took a tour of the complex and really enjoyed it.", \
               html.Br(), html.Br(), \
               "The traditional style of buildings is really " \
               "nice -- the Albrecht-Dürer-Straße is especially picturesque! Besides this, be sure to see the main " \
               "cathedral, the Handwerkerhof (made to resemble medieval Nuremberg)," \
               "the Schöner Brunnen fountain, and climb up to the 11th century castle complex.", \
               html.Br(), html.Br(), \
               "There is a lot of really great food and beer here. First, you have to try the Nürnberger Bratwurst. " \
               "They are quite small in size so you can definitely eat a few at least. Go to this traditional " \
               "bratwurst restaurant -- 'Bratwursthäusle bei St. Sebald.' " \
               "Obviously try the bratwurst, and round out the meal with sauerkraut, a pretzel, and a beer! " \
               "It is also quite common around the city to be able to get three little bratwurst in a roll with " \
               "mustard, this is known as 'drei im Weggla.' These are also really good and only cost a few euros. " \
               "Another part of the friendly rivalry between Franconia and traditional Bavaria -- which part of " \
               "the pig leg is the local delicacy. In Franconia, it is the Schäufele (shoulder), and in Bavaria " \
               "it is the ham hock (Schweinshaxe). Both are great -- but try the Schäufele when you're here! " \
               "I had an absolutely delicious sampler plate (that included it) at Hütt'n. Right next door, join in " \
               "on a very fun tradition in the city -- people gather and sit on the sloped road in front of Cafe " \
               "Wanderer to enjoy a beer around happy hour every evening. Lastly, be sure to try the local " \
               "Lebkuchen (gingerbread) at Wicklein, the world's oldest gingerbread store -- they have been making " \
               "gingerbread since 1615!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/germany/nur.JPG"},
                    {"src": "assets/germany/nur1.JPG"},
                    {"src": "assets/germany/nur2.JPG"},
                    {"src": "assets/germany/nur3.JPG"},
                    {"src": "assets/germany/nur4.JPG"},
                    {"src": "assets/germany/nur5.JPG"},
                    {"src": "assets/germany/nur6.JPG"},
                    {"src": "assets/germany/nur7.JPG"},
                    {"src": "assets/germany/nur8.JPG"},
                    {"src": "assets/germany/nur9.JPG"},
                    {"src": "assets/germany/nur10.JPG"},
                    {"src": "assets/germany/nur11.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.nur_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Oranienburg':
        return 'The remains of the Sachsenhausen concentration camp can be found here. It has been converted into ' \
               'a memorial / museum and it is really well done.' \
               'There is so much to read, see, and learn here. It is naturally difficult to learn about all the ' \
               'atrocities that occurred here, but I would recommend a visit.' \
               'It is an easy day trip from Berlin.', \
                html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.oran_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Potsdam':
        return 'Home to many castles! Easy day trip (or fun bike trip) from Berlin!', \
                html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.pots_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Rügen':
        return "The biggest island of Germany! ", \
                "(Yes Germany has islands, almost 100 actually!) Located in the Baltic Sea, ", \
                "Rügen is just off the northern coast of Germany, the closest city on the mainland being Stralsund. ", \
                html.Br(), html.Br(), \
                "Rügen is famous for its steep chalk cliffs along the water — and they are indeed quite stunning! ", \
                "There are two national parks on the island, the more famous being Jasmund. This is where the ", \
                "famous ‘Königsstuhl’ can be found. You can drive here, but I would definitely recommend taking a ", \
                "bike around the island! The cliffs are an easy bike ride from the nearby city of Sassnitz. ", \
                "Sassnitz is a really nice little city with nice cafes and restaurants. There is also a big, ", \
                "long pier with a cool little green lighthouse at the end. There aren’t any beaches here though — ", \
                "the best place for beaches and swimming is Binz. This is the main hotel / resort area of the ", \
                "island. We didn’t end up making it here but this would certainly be a lovely place to stay.", \
                html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.rugen_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Stralsund':
        return 'Cool little port city on the Baltic sea. Home to the great Störtebeker brewery! The brewery was ' \
               'named after the legendary pirate Klaus Störtebeker, who was born just outside Stralsund.', \
               'If you are visiting Rügen, Stralsund is definitely worth a stop. It is also a great option to ', \
               'stay in Stralsund and explore Rügen during the day. There are really good train connections ', \
               'from the main train station in Stralsund to the different parts of the island of Rügen.', \
                html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.stral_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Stuttgart':
        return 'Was only here briefly but the main Christmas market was nice', \
                html.Br(), html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.stutt_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Hungary
    if value == 'Budapest':
        return 'Coolest parliament building in the world? The ruin pubs (makeshift pubs out of buildings ' \
               'that were damaged in WW2 and then abandoned) are really quirky, creative, and fun. ' \
               'Be absolutely sure to climb up the citadel to see the Liberty Statue ' \
               '(formerly the "Communism Statue"). The view of the river and the city ' \
               'down below is amazing. Definitely go to the famous Széchenyi bath too.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/hungary/bud.JPG"},
                    {"src": "assets/hungary/bud4.JPG"},
                    {"src": "assets/hungary/bud6.JPG"},
                    {"src": "assets/hungary/bud7.JPG"},
                    {"src": "assets/hungary/bud5.JPG"},
                    {"src": "assets/hungary/bud8.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.budapest_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Iceland
    if value == 'Reykjavik':
        return "Cool city but don't stay too long -- get out and explore the nature in the 'Land of Fire and Ice.'" \
               "There are some unique foods here that are really good and you should try." \
               "Go to Íslenski Barinn restaurant. They had an amazing whale fin steak and a crazy " \
               "good reindeer burger. We didn't see puffin on a menu but it is also eaten here." \
               "See the rainbow road. Check out the Viking church and go to the top of it. Bæjarins Beztu Pylsur is " \
               "also a fun hot dog spot made famous by Bill Clinton -- Forbes called it the world's most " \
               "famous hot dog vendor! They're made of lamb and definitely worth a try!", \
                html.Br(), \
                html.Div(
                    dl.Map([dl.TileLayer(),
                            dl.GeoJSON(data=coordinates.reykjavik_geojson)],
                           style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Southern half of island':
        return 'so much to see in not enough time -- lots more to come!', \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/6cJNYYk1n3I",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/iceland/hotspring.JPG"},
                    {"src": "assets/iceland/hottub.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.vik_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Ireland
    if value == 'Cliffs of Moher':
        return 'Awesome (big) day trip from Dublin. They are amazing. My trip also included cool little stops at ' \
               'castles ___ and ___.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/ireland/moher.JPG"},
                    {"src": "assets/ireland/moher1.JPG"},
                    {"src": "assets/ireland/moher2.JPG"},
                    {"src": "assets/ireland/moher3.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.cliffs_of_moher_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Dingle':
        return ('This peninsula on the west coast of Ireland is absolutely stunning! The cliffs and coastline here '
                'are similar to the Cliffs of Moher (not quite as dramatic though to be fair), not too far up the '
                'coast from Dingle. The views from Inch Beach are really nice, but the views from our hike on the '
                'northern coast of the peninsula were incredible. Also on the northern coast, you can find a beautiful '
                'golf course called Castlegregory. The hole that runs along the massive beach was amazing!'), \
                html.Br(), html.Br(), \
                ('The city of Dingle is quite small and quite lovely! There are a number of fun pubs, including ____. '
                 "Murphy's is a great local ice cream shop. "
                 "Lastly, a little boat trip out of Dingle to see "
                 "the nearby cliffs and caves from the water is also a great idea! This was very reasonably priced "
                 "for a group as we paid for the entire boat, rather than per person."), \
                html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/ireland/dingle.JPG"},
                    {"src": "assets/ireland/dingle1.JPG"},
                    {"src": "assets/ireland/dingle2.JPG"},
                    {"src": "assets/ireland/dingle4.JPG"},
                    {"src": "assets/ireland/dingle5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.dingle_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Dublin':
        return ('There is just such a special charm to this city! It was amazing to finally do a full Griffin family '
                "trip here in October 2023. Dublin is not the biggest city and you don't need a ton of time here -- "
                "but the more the better! Enjoy a walk along the River Liffey, through St. Stephens Green park, and "
                "around the Trinity College campus. Here you can also see the Book of Kells!"
                "Other things to see include the Dublin castle complex and St. Patrick's Cathedral, and of course "
                "do the Guinness tour! The view from "
                "the new Gravity Bar at the top of St. James' Gate (Guinness brewery) is beautiful. Additionally, "
                "the Irish Whiskey Museum is also a great option -- the guy who led the tour was so good! "
                "There is great craic (Irish word for fun!) at all the pubs. The live music "
                "and Irish dancing is so fun. You can find plenty of lively bars and pubs (and the Molly Malone "
                "statue) in the Temple Bar area, but be aware this is the most touristy area and prices are a bit "
                "high. Definitely walk through though to see the atmosphere and all the Irish-themed decorations "
                "and details! Some other good spots include Arthur's (down the street from "
                "St. James's Gate) and the Brazen Head (arguably the oldest pub in the world, almost 1,000 years!)"
                "Sláinte!"), \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/ireland/dublin.JPG"},
                    {"src": "assets/ireland/dublin1.JPG"},
                    {"src": "assets/ireland/dublin2.JPG"},
                    {"src": "assets/ireland/dublin3.JPG"},
                    {"src": "assets/ireland/dublin4.JPG"},
                    {"src": "assets/ireland/dublin5.JPG"},
                    {"src": "assets/ireland/dublin6.JPG"},
                    {"src": "assets/ireland/dublin7.JPG"},
                    {"src": "assets/ireland/dublin8.JPG"},
                    {"src": "assets/ireland/dublin9.JPG"},
                    {"src": "assets/ireland/dublin10.JPG"},
                    {"src": "assets/ireland/dublin11.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.dingle_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Tralee':
        return ('The hometown of my Grandpa Séan! Tralee is the largest city in County Kerry, but it still pretty '
                'small with just ___ people. The mountains of Kerry in the backdrop of the city are quite impressive! '
                "I didn't realize they were so big! See the main square called An Chearnóg and the main street called"
                "The Mall. Enjoy the local shops, bakeries, and pubs!"), \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/ireland/tralee.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.tralee_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Italy
    if value == 'Bergamo':
        return 'DO NOT immediately overlook Bergamo in favor of Milan. A lot of budget airlines that ' \
               'fly to "Milan" ' \
               'actually fly to the nearby city of Bergamo. It is a really cute city and they invented ' \
               'Stracciatella gelato. Take the little cable car up to the high part of the city and walk ' \
               'around the ' \
               'fortress area. There is a great view to the south of the city right when you get off ' \
               'the cable car. ' \
               'There is also a restaurant / cafe right there as well with really nice views. ' \
               'Climb the rest of the ' \
               'way up and you can also get the view the opposite direction (north), where you can ' \
               'actually see the ' \
               'mountains of Switzerland not too far away! Circolino is a great restaurant -- you can ' \
               'get a 3 course ' \
               'meal with wine for just 15 euros (as of 2023). Be sure to have some risotto, ' \
               'more traditional than pasta in the north of Italy.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/bergamo.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.bergamo_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Florence':
        return 'Such a lovely city. The Arno river runs right through the city and the sun sets ' \
               'beautifully over it (at least in April when I went!). DO NOT come here without ' \
               "visiting the world famous sandwich shop All'Antico at least once... I would recommend coming " \
               "multiple times! For just 5 " \
               "euros (in 2017) you can get a huge sandwich on lovely bread topped high with the freshest " \
               "mozzarella, tomatoes, and prosciutto, finished with this black truffle sauce that is " \
               "just too good. There will likely be a line but trust me it is so worth it!" \
               "Definitely visit the cathedral. You can also go up the tower for some great views. " \
               "Also next to the cathedral is another great spot for more great sandwiches and food -- there is a " \
               "very nice little cafe here called Panini Toscani. Also be sure to climb up to the " \
               "Michelangelo plaza with a bottle of wine to get beautiful views of the whole city, " \
               "with the cathedral taking center stage. For a fun bar, go to Red Garter. Lastly, you are " \
               "in Tuscany, so a day trip to visit vineyards is also a great idea. There are a number of " \
               "options for this, just look online on Viator or Airbnb Experiences.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/flo.JPG"},
                    {"src": "assets/italy/flo1.JPG"},
                    {"src": "assets/italy/flo2.JPG"},
                    {"src": "assets/italy/flo7.JPG"},
                    {"src": "assets/italy/flo3.JPG"},
                    {"src": "assets/italy/flo4.JPG"},
                    {"src": "assets/italy/flo8.JPG"},
                    {"src": "assets/italy/flo9.JPG"},
                    {"src": "assets/italy/flo5.JPG"},

                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.florence_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Genoa':
        return "The birthplace of Christopher Columbus and pesto! Also make sure you try panissa!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/gen6.JPG"},
                    {"src": "assets/italy/gen.JPG"},
                    {"src": "assets/italy/gen1.JPG"},
                    {"src": "assets/italy/gen2.JPG"},
                    {"src": "assets/italy/gen3.JPG"},
                    {"src": "assets/italy/gen4.JPG"},
                    {"src": "assets/italy/gen5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.genoa_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Lecco':
        return 'Lovely day trip from Bergamo', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    # {"src": "assets/italy/lecco.JPG"}, # different photo size
                    # {"src": "assets/italy/lecco1.JPG"}, # different photo size
                    {"src": "assets/italy/lecco2.JPG"},
                    {"src": "assets/italy/lecco3.JPG"},
                    {"src": "assets/italy/lecco4.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.lecco_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Milan':
        return 'The center of the city with the cathedral (duomo in Italian) and the arcade to the left of ' \
               'the duomo are really nice. In the south of the city the Navigli district is awesome -- ' \
               'along a river/canal, there are tons of restaurants with massive buffets that offer really good ' \
               'all you can eat happy hour ' \
               'deals. Go to this fun bar with weirdly-shaped beer glasses called La Fontanella. ' \
               'Be sure to have some ' \
               'risotto, more traditional than pasta in the north of Italy. The city is also home to the ' \
               'legendary San Siro stadium where both of the very successful football teams, AC Milan and ' \
               'Internazionale (Inter for short) Milan, play. However, beyond this, Milan feels like ' \
               'more of a place to shop luxury brands and eat fancy meals.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/milan.JPG"},
                    {"src": "assets/italy/milan7.JPG"},
                    {"src": "assets/italy/milan3.JPG"},
                    {"src": "assets/italy/milan4.JPG"},
                    {"src": "assets/italy/milan2.JPG"},
                    {"src": "assets/italy/milan5.JPG"},
                    {"src": "assets/italy/milan6.JPG"},
                    {"src": "assets/italy/milan8.JPG"},
                    {"src": "assets/italy/milan1.JPG"},

                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.milan_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Portofino':
        return 'more info coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/pf1.JPG"},
                    {"src": "assets/italy/pf.JPG"},
                    {"src": "assets/italy/pf2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.portofino_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Rome':
        return 'So much fascinating history here. The food scene is also incredible. Be sure to visit the coliseum, ' \
               'the old Roman ruins, visit the Vatican(separate Italy page for this), and get your Lizzie McGuire ' \
               'on at the Trevi Fountain! The city is quite big with so many different neighborhoods, ' \
               'all deserving of some time being spent there. Trastevere is probably the most beloved neighborhood ' \
               '-- beautiful and with many great restaurants and bars. One very famous bar is Bar San Calisto. ' \
               'Know that there are some Italian foods that are specifically Roman in origin and are best eaten in ' \
               'Rome. The traditional cheese here is pecorino romano rather than parmigiano reggiano. There are ' \
               'four classic Roman pastas that are all very connected, just with slight variations in ingredients -- ' \
               "cacio e pepe (pecorino and pepper), pasta alla gricia (pecorino, pepper, and  guanciale), " \
               "carbonara (pecorino, pepper, egg, and  guanciale), and pasta all'amatriciana " \
               "(pecorino, pepper, tomatoes, and  guanciale). Hopefully you have time to try all of these!" \
               "Unlike Neopolitan pizza, Roman pizza styles can actually vary quite a bit. " \
               "Bonci Pizzarium is the most famous -- you will probably recognize the logo. Bonci Pizzarium is " \
               "an easy stop before or after visiting the Vatican. Piccolo Buco is " \
               "an easy stop before or after visiting the Trevi Fountain. Other great pizza spots include Sbanco " \
               "(serving Birrificio del Ducato craft beers!), Tonda, and Trapizzino (multiple locations).", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/rome.JPG"},
                    {"src": "assets/italy/rome1.JPG"},
                    {"src": "assets/italy/rome2.JPG"},
                    {"src": "assets/italy/rome3.JPG"},
                    {"src": "assets/italy/rome4.JPG"},
                    {"src": "assets/italy/rome5.JPG"},
                    {"src": "assets/italy/rome6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.rome_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Vatican 🇻🇦':
        return 'Definitely worth some time on your visit to Rome, especially as a Catholic. The main plaza (St. ' \
               "Peter's Square) with St. Peter's Basilica is " \
               'really nice, but also be sure to see the Sistine Chapel (famous for Michelangelo painting on ' \
               'ceiling of God and Adam reaching out to each other, picture below) and check out some of the museums ' \
               'as well. Be sure to make a stop at Bonci Pizzarium before or after your visit. They are world famous ' \
               '(you will probably recognize the logo) for their pizza but they have other food options as well. ' \
               'There will likely be a line but it will be worth the wait!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/vat.JPG"},
                    {"src": "assets/italy/vat1.JPG"},
                    {"src": "assets/italy/vat2.JPG"},
                    {"src": "assets/italy/vat6.JPG"},
                    {"src": "assets/italy/vat3.JPG"},
                    {"src": "assets/italy/vat4.JPG"},
                    {"src": "assets/italy/vat5.JPG"},

                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.vatican_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Venice':
        return 'It is definitely as charming as everyone says it is. Visit the main plaza (St. Marco) and church, ' \
               'go to the top of the tower there for great views of the city, take a boat ride (the boat usually ' \
               'has a fixed cost no matter the size of your group -- find some new friends to lower the cost per ' \
               "person!) Beyond St. Marco, don't necessarily worry about " \
               "trying to see or do everything -- just enjoy the lovely ambiance of the canals and little streets.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/ven.JPG"},
                    {"src": "assets/italy/ven1.JPG"},
                    {"src": "assets/italy/ven2.JPG"},
                    {"src": "assets/italy/ven3.JPG"},
                    {"src": "assets/italy/ven4.JPG"},
                    {"src": "assets/italy/ven5.JPG"},
                    {"src": "assets/italy/ven6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.venice_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Verona':
        return 'The setting from the famous Romeo and Juliet play -- Verona is a beautiful city ' \
               'that probably does ' \
               'not get enough attention. Verona boasts a large coliseum-like arena that is actually older than ' \
               'the coliseum. The Adige river that runs through the city is really nice. Climb up the hill to ' \
               'Castel San Pietro for stunning sunset views over the city. Also go to this little pizza spot called ' \
               'Wallet Pizza ' \
               'for really cheap and ridiculously good pizzas that are made fresh and cook in literally ' \
               'one minute. ' \
               'Be sure to have some risotto, more traditional than pasta in the north of Italy. I also had ' \
               'legitimately life-changing amaretto gelato at a little shop called Gelateria Ponte Pietra Verona. ' \
               'Lastly, a really good restaurant is Osteria Caffè Monte Baldo.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/italy/verona.JPG"},
                    {"src": "assets/italy/verona3.JPG"},
                    {"src": "assets/italy/verona2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.verona_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Mexico
    if value == 'Cancún':
        return 'The beaches in the Riviera Maya are beautiful. One can obviously come here to party, but ' \
               'visiting the Mayan ruins and exploring nature are also amazing. Visit the Xel-Ha park and snorkel ' \
               'through the waters and caves!', \
                html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.cancun_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Mexico City':
        return "What a city. Weather is temperate year round. So much good cheap food. The tamales with mole " \
               "just might change your life. Surprisingly there really don't seem to be too many tourists." \
               "Obviously also get lots of tacos, but also try tortas, conchas, elote, and some fresh fruits " \
               "like mango and chirimoya. " \
               "Take a little trip on one of the little boats and get ready to see the world's largest floating " \
               "market. Having a mariachi band step onto your boat and play a few songs while drinking beers, " \
               "eating elote, and floating down the river is just truly a beautiful life experience. " \
               "Be sure to have a good amount of cash for this. " \
               "Also see the Frida Kahlo house and check out the Coyoacán market. " \
               "It is 100% authentic and you can try " \
               "ants, crickets, and even scorpions if you are feeling ambitious. It definitely helps to " \
               "speak some Spanish, as there are not a lot of tourists compared to beach or resort towns in Mexico." \
               'Mexico City is also home to the legendary Azteca football stadium, where the Mexico national ' \
               'team plays as well as Club América. Seeing a game here is absolutely on my bucket list. ' \
               'Lastly, Ubers are also really cheap which makes it easy to get around, as it is quite a big city.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/mexico/cdmx.JPG"},
                    {"src": "assets/mexico/cdmx3.JPG"},
                    {"src": "assets/mexico/cdmx2.JPG"},
                    {"src": "assets/mexico/cdmx1.JPG"},
                    {"src": "assets/mexico/cdmx4.JPG"},
                    {"src": "assets/mexico/cdmx5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.mexico_city_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Montenegro
    if value == 'Kotor':
        return "Just as cool as Dubrovnik but not as sexy. It's smaller and way more of an authentic feel. " \
               "Not many tourists here.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/montenegro/kotor1.JPG"},
                    {"src": "assets/montenegro/kotor2.JPG"},
                    # {"src": "assets/montenegro/kotor3.JPG"},
                    {"src": "assets/montenegro/kotor4.JPG"},
                    {"src": "assets/montenegro/kotor5.JPG"},
                    {"src": "assets/montenegro/kotor6.JPG"},
                    {"src": "assets/montenegro/kotor7.JPG"},
                    {"src": "assets/montenegro/kotor8.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.kotor_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Morocco
    if value == 'Tangier':
        return 'Despite being just 17 miles from the southern coast of Spain, I felt more culture shock here than ' \
               'anywhere in Europe. The newer part of th e city has a European ' \
               'feel as this used to be the gateway from Europe to Africa (and vice versa) before air travel. ' \
               'However, inside the old city walls of Tangier (the Kasbah) is a whole different story.' \
               'Here, there are a number of locals who will ask you where you are going or if you want to eat ' \
               'something. I think restaurants compensate them if they bring people to their restaurant. ' \
               'If you are with a local though no one will bother you. Thus, getting a guide for a day is a good ' \
               'idea and not too expensive. They will likely also set you up to go a nearby beach and ride camels, ' \
               'which was such a fun, unique experience. We also visited the Cave of Hercules which was really cool! ' \
               'The food there is so good -- the ' \
               "'thousand-hole pancakes' and shakshouka (my favorite breakfast on the planet), " \
               "chicken tagine (lamb or beef are also amazing), couscous (originally from Morocco and also " \
               "their national dish), fish chermoula, and zaalouk (like baba ganoush). Be sure to visit Cafe Hafa. " \
               "It overlooks the Bay of Tangier (and the Strait of Gibraltar) and you can see the " \
               "southern tip of Spain on a clear day! This was also a favorite spot of Jimi Hendrix!", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/morocco/tangier.JPG"},
                    {"src": "assets/morocco/tangier1.JPG"},
                    {"src": "assets/morocco/tangier2.JPG"},
                    {"src": "assets/morocco/tangier3.JPG"},
                    {"src": "assets/morocco/tangier4.JPG"},
                    {"src": "assets/morocco/tangier5.JPG"},
                    {"src": "assets/morocco/tangier6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.tangier_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Netherlands
    if value == 'Amsterdam':
        return "A really great city. There's a lot more to the city than the red light district. There are so many " \
               "little canals and bridges and they are all so picturesque, especially in the Jordaan " \
               "neighborhood. Don't worry so much about seeing specific sights and just wander in the city " \
               "and enjoy. Go to Winkel 43 to try the famous Dutch " \
               "apple pie. Go to Heertje Friet for fries and bitterballen (these are incredible). Fish sandwiches " \
               "from little stands on the street are also a fantastic choice. " \
               "Take some kind of boat trip -- most boats have some history / fun facts and have drinks " \
               "on board. They aren't too expensive either. " \
               "Walk along the port and also for a nice walk through Vondelpark. " \
               "Go to a coffee shop if that's your vibe haha. Bulldog " \
               "is the most famous coffee shop chain but the more tranquil little coffee shops on the canals are " \
               "really awesome. If you are looking for a wild party, come for King's Day. " \
               "It happens yearly on the king's birthday, April 27. The whole city dresses in orange and there " \
               "is lots of drinking and music everywhere. Was quite the experience... would absolutely recommend! " \
               "Lastly, the Anne Frank house is also one of the main tourist attractions -- personally I have not " \
               "been. Unless you want to wait a long time to go, you need to reserve tickets in advance.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/netherlands/ams3.JPG"},
                    {"src": "assets/netherlands/ams.JPG"},
                    {"src": "assets/netherlands/ams2.JPG"},
                    {"src": "assets/netherlands/ams4.JPG"},
                    {"src": "assets/netherlands/ams5.JPG"},
                    {"src": "assets/netherlands/ams6.JPG"},
                    {"src": "assets/netherlands/ams7.JPG"},
                    {"src": "assets/netherlands/ams8.JPG"},
                    {"src": "assets/netherlands/ams9.JPG"},
                    {"src": "assets/netherlands/ams10.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.amsterdam_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# North Macedonia
    if value == 'Skopje':
        return 'Really cool authentic Balkan city with not so many tourists. This was the home / birthplace ' \
               "of Alexander the Great. There is a huge statue of him on the main plaza, and it's funny there a big " \
               "sign for a Macedonian beer company right behind him -- CKOΠCKO (SKOPSKO). You'll notice that " \
               "most everything is written with the cyrillic alphabet rather than the latin alphabet, so it does " \
               "help to learn a bit about the cyrillic alphabet. "\
               "The Alexander the Great statue is just one of seemingly hundreds of statues in the city. Keep an " \
               "eye out as you walk around for other statues, they are fun. " \
               "Be sure to climb up to the fortress that overlooks the city. Ideally for sunset. There's an " \
               "amazing view of the city and the snow-covered mountains in the background. " \
               "The old town / bazaar is really cool. Just walk around and explore. I went to ___ and it was really " \
               "good. Get the kebap and the Shopsko salad. " \
               "Prices for everything are pretty " \
               'cheap. My hostel was only 10 euros per night (8 bed dorm in Hi Skopje Hostel). The woman who ' \
               'runs the place was so nice ' \
               'and gave great recommendations. She also shared some of her homemade rakija, a local liquor. ', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/macedonia/skopje.JPG"},
                    {"src": "assets/macedonia/skopje3.JPG"},
                    {"src": "assets/macedonia/skopje2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.skopje_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Norway
    if value == 'Oslo':
        return 'The capital of Norway! Oslo is so clean and all the infrastructure is so nice. ' \
               'Everything is quite expensive though… for example, the airport is far away but there is a ' \
               'really nice high speed train that takes you to the main train station in the center of the ' \
               'city in just 20 minutes, but costs ~$20. Right near the main train station is the national ' \
               'opera house right on the water. The architecture is really cool and unique — the street ' \
               'becomes the bridge which eventually becomes the roof of the building! You can walk up to ' \
               'the top of it for some great views of the fjord. Along this fjord there are a couple great ' \
               'spots for food and drinks called SALT and Vippa. It there are some really nice areas of the ' \
               'city on the water. There are also a number of really cool floating docks. They have outdoor ' \
               'areas for enjoying the sun and jumping in the fjord and also indoor saunas! The sauna culture ' \
               'is big here. There is also a sauna at SALT that is supposed to be cool. ' \
               'Somewhere near the train station is a good place to stay. I stayed in K7 Hostel and it was ' \
               'decent but pricey (~$75 per night for a dorm bed). The first highlight of my trip was the ' \
               'hike I did to Vettakollen. I took the local train about 20 minutes to the Vettakollen stop' \
               ' and then it was maybe a 20-30 minute hike up to a viewpoint for amazing views of the city ' \
               'and the Oslo fjord! The next highlight (also the main reason for my trip) was seeing Norway ' \
               'play against Cyprus in a qualifying game for the 2024 European football championships! ' \
               'Norway won 3-1, Erling Haaland scored two goals, and Martin Ødegaard had a great game as well.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/norway/oslo.JPG"},
                    {"src": "assets/norway/oslo2.JPG"},
                    {"src": "assets/norway/oslo3.JPG"},
                    {"src": "assets/norway/oslo4.JPG"},
                    {"src": "assets/norway/oslo5.JPG"},
                    {"src": "assets/norway/oslo6.JPG"},
                    {"src": "assets/norway/oslo7.JPG"},
                    {"src": "assets/norway/oslo8.JPG"},
                    {"src": "assets/norway/oslo9.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.oslo_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Peru
    if value == 'Lima':
        return 'more info to come!', \
                html.Br(), html.Br(), \
                html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.lima_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Iquitos':
        return 'The start of my Amazon river adventure. We flew here from Lima and took a boat about 50 miles down ' \
               'the Amazon. We then stayed in a few remote places in the rain forest before coming back to ' \
               'Iquitos. Really an adventure of a lifetime. If you have the opportunity to do something like this, ' \
               'DO IT !', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/peru/iquitos.PNG"},
                    {"src": "assets/peru/iquitos1.PNG"},
                    {"src": "assets/peru/iquitos2.PNG"},  # need to adjust photo size ratio
                    {"src": "assets/peru/iquitos3.PNG"},  # need to adjust photo size ratio
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.iquitos_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Poland
    if value == 'Krakow':
        return 'more info coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/poland/kra.JPG"},
                    {"src": "assets/poland/kra2.JPG"},
                    {"src": "assets/poland/kra3.JPG"},
                    {"src": "assets/poland/kra4.JPG"},
                    {"src": "assets/poland/kra5.JPG"},
                    {"src": "assets/poland/kra6.JPG"},
                    {"src": "assets/poland/kra7.JPG"},
                    {"src": "assets/poland/kra8.JPG"},
                    {"src": "assets/poland/kra9.JPG"},
                    {"src": "assets/poland/kra10.JPG"},
                    {"src": "assets/poland/kra11.JPG"},
                    {"src": "assets/poland/kra12.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.krakow_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Wrocław':
        return 'Very pretty small city. The people were all very nice. Go to the market square and check out some ' \
               'of the cafes and restaurants. The Konspira restaurant is really great -- this is also a great option ' \
               'because there is a lot about the history of Wrocław and Poland on the walls of the ' \
               'restaurant and in the menu. Definitely get pierogi. Soups are very good and traditional too. ' \
               'Be on the lookout for the hundreds of little gnomes around the city as you walk around. They are ' \
               'really fun and funny. They are a recent project that is inspired by ____. Lastly, go north of the ' \
               'market square and walk around the river / island area -- the churches there are really nice as well.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/poland/wro.JPG"},
                    {"src": "assets/poland/wro1.JPG"},
                    {"src": "assets/poland/wro2.JPG"},
                    {"src": "assets/poland/wro3.JPG"},
                    {"src": "assets/poland/wro4.JPG"},
                    {"src": "assets/poland/wro5.JPG"},
                    {"src": "assets/poland/wro6.JPG"},
                    {"src": "assets/poland/wro7.JPG"},
                    {"src": "assets/poland/wro8.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.wroclaw_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Portugal
    if value == 'Lisbon':
        return 'Absolutely lovely city! More info to come!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/portugal/lisbon.JPG"},
                    {"src": "assets/portugal/lisbon1.JPG"},
                    {"src": "assets/portugal/lisbon2.JPG"},
                    {"src": "assets/portugal/lisbon3.JPG"},
                    {"src": "assets/portugal/lisbon4.JPG"},
                    {"src": "assets/portugal/lisbon5.JPG"},
                    {"src": "assets/portugal/lisbon6.JPG"},
                    {"src": "assets/portugal/lisbon7.JPG"},
                    {"src": "assets/portugal/lisbon8.JPG"},
                    {"src": "assets/portugal/lisbon9.JPG"},
                    {"src": "assets/portugal/lisbon10.JPG"},
                    {"src": "assets/portugal/lisbon11.JPG"},
                    {"src": "assets/portugal/lisbon12.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.lisbon_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Guincho Beach':
        return 'Not too far of a drive from Lisbon -- I was lucky to meet someone with a car and we drove here. ' \
               "There are big sand dunes next to the coast. There's also a couple cafes here where you can grab a" \
               "drink or a bite to eat. Sunset here over the ocean was just beautiful. ", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/portugal/guincho.JPG"},
                    {"src": "assets/portugal/guincho1.JPG"},
                    {"src": "assets/portugal/guincho2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.guincho_beach_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Puerto Rico
    if value == 'Rincón':
        return 'Beautiful! More info to come!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/pr/rincon.JPG"},
                    {"src": "assets/pr/rincon2.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.rincon_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'San Juan':
        return 'So fun. More info to come!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.san_juan_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Slovakia
    if value == 'Bratislava':
        return 'What a fun little city with a cool old town and a really cool citadel that overlooks the city and ' \
               'the river that runs through it.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/slovakia/bratislava.JPG"},
                    {"src": "assets/slovakia/bratislava2.JPG"},
                    {"src": "assets/slovakia/bratislava1.JPG"},
                    {"src": "assets/slovakia/bratislava3.JPG"},
                    {"src": "assets/slovakia/bratislava4.JPG"},
                    {"src": "assets/slovakia/bratislava5.JPG"},
                    {"src": "assets/slovakia/bratislava6.JPG"},
                    {"src": "assets/slovakia/bratislava7.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.bratislava_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Slovenia
    if value == 'Ljubljana':
        return 'The smallest European capital and what a cute little city it is. I went in October and the trees ' \
               'lining the river were beautiful colors. The city is very clean and the people are really nice. ' \
               'Climb up to the citadel to see the city from above. Eat some goulash. Great place for sunset as well.' \
               "Fun fact: George W Bush the second landed here for some conference and greeted the people of " \
               "'Slovakia.'", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/slovenia/lju.JPG"},
                    {"src": "assets/slovenia/lju1.JPG"},
                    {"src": "assets/slovenia/lju2.JPG"},
                    {"src": "assets/slovenia/lju3.JPG"},
                    {"src": "assets/slovenia/lju4.JPG"},
                    {"src": "assets/slovenia/lju5.JPG"},
                    {"src": "assets/slovenia/lju6.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.ljubljana_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Spain
    if value == 'Azpeitia':
        return 'Birthplace of St. Ignatius and home to a large festival on July 31 each year for his feast day', \
               html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.azpeitia_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Barcelona':
        return 'PSA -- I am biased having studied abroad here but this is one of my favorite cities in the world! ' \
               'So much to do, see, and eat in this beautiful city on the Mediterranean Sea. Things to do include ' \
               'visiting the Bunkers del Carmel (amazing place for a picnic with stunning views of the city), the ' \
               'beach (Ciutat Vella is much less crowded than Barceloneta), Parc Güell (get your Cheetah Girls on! ' \
               'also note that to get to the area of the park with the famous bench, you need to book tickets -- it ' \
               'do is best to do so ahead of time!), Sagrada Familia church, the apartment buildings designed by ' \
               'the famous architect Gaudí (La Pedrera and Casa Batllo), Montjuic Park / Castle, La Boquería market ' \
               "(on the touristy street of La Rambla), Arc de Triomf and the Parque de la Ciutadella (fun spot " \
               "to rent little boats), the old Olympic Stadium, and if you're a soccer fan -- the Camp Nou, home " \
               "of FC Barcelona, and the largest soccer stadium in Europe with a capacity of 105,000! There are " \
               "also plenty of great rooftop bars, just look some up online. ", \
               html.Br(), html.Br(), \
               "There is so much great food here. Maybe my favorite restaurant in the world is here and is " \
               "called El Glop (the one in the Gràcia neighborhood is the original and is the best. The chicken & " \
               "vegetable paella is incredible. Also get the crema catalana (similar to a Crème Brûlée) for " \
               "dessert. My other favorite place to eat is at either Sol Soler or Niña. They are right next " \
               "to each other on the lovely Plaça del Sol and share the same kitchen. This plaza is an awesome " \
               "neighborhood spot and it fills up every evening with people socializing. There are" \
               "also empanada places nearby if you want to grab an empanada and enjoy the atmosphere! " \
               "Some other great dinner " \
               "spots include Taverna la Llesca, La Pubilla, Arume Restaurante (duck paella is amazing), and " \
               "La Pepita. Another awesome place is Surfhouse Barcelona right on the beach -- it is a bit touristy " \
               "but the food is great, and there is often live music next to the outdoor seating area! One more food " \
               "place that is really cool and more upscale is El Nacional.", \
               html.Br(), html.Br(), \
               "Barcelona has what was my absolute favorite bar in the world -- Gato Negro! It has changed a bit " \
               "unfortunately, but it is still a really cool spot with great cheap local beer on draft (Moritz)." \
               "There are lots of other really fun little bars in Gràcia as well." \
               "Barcelona also has a big party scene -- there are many clubs on the beach which are a bit touristy " \
               "but really cool. These include Opium, Pacha, and Shoko. Besides the beach clubs, there is Otto Zutz, " \
               "Razzmatazz (huge, known to be probably the best club', and Jamboree (dance club). There are also " \
               "some really fun salsa clubs." \
               "For an upbeat atmosphere but not clubs, there is Oveja Negra (two locations, one is more casual " \
               "and the other " \
               "is more of a beer hall), Dow Jones (drink prices change like stocks), and Espit Chupitos " \
               "(cool shot bar).", \
               html.Br(), html.Br(), \
               "Outside of Barcelona, there is even more to do! Up the coast from Barcelona is the beautiful 'Costa" \
               "Brava,' with a number of cute little towns, nice beaches, and really cool coves for swimming. " \
               "You can also take a train inland to go for a really cool hike and visit Montserrat, where there are " \
               "some really uniquely shaped mountains. Lastly, in winter you can even go skiing -- it is just " \
               "a few hours drive to the tiny country of Andorra, on the border of Spain and France, " \
               "up in the Pyrenees mountains. It is absolutely beautiful here and the skiing is great. I have " \
               "another page on Andorra.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/spain/bcn.JPG"},
                    {"src": "assets/spain/bcn1.JPG"},
                    {"src": "assets/spain/bcn2.JPG"},
                    {"src": "assets/spain/bcn3.JPG"},
                    {"src": "assets/spain/bcn4.JPG"},
                    {"src": "assets/spain/bcn5.JPG"},
                    {"src": "assets/spain/bcn6.JPG"},
                    {"src": "assets/spain/bcn7.JPG"},
                    {"src": "assets/spain/bcn9.JPG"},
                    {"src": "assets/spain/bcn10.JPG"},
                    {"src": "assets/spain/bcn11.JPG"},
                    {"src": "assets/spain/bcn12.JPG"},
                    {"src": "assets/spain/bcn13.JPG"},
                    {"src": "assets/spain/bcn14.JPG"},
                    {"src": "assets/spain/bcn15.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.barcelona_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Begur':
        return 'Really nice beaches if you want to visit nice beaches up the coast from Barcelona', \
               html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.begur_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Bilbao':
        return "Capital of the Basque country! I didn't spend too much time here but definitely worth a stop. ", \
               html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.bilbao_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Buñol':
        return "Home of the world’s biggest food fight! It happens the last Wednesday of August every year. " \
               "It is a tiny town with probably little to no tourism for most of the year besides this weekend. " \
               "Trucks upon trucks bring tomatoes that weren’t quite up to Spain’s high standards to be sold for " \
               "consumption. These trucks then push through the super narrow streets -- there are even people / " \
               "staff in front of the trucks to push the crowds off to the side so the trucks can get through. As " \
               "the trucks pass, people standing on the truck throw and shovel tomatoes into the crowds. People " \
               "in turn throw these tomatoes around again and again. By the end, the entire street becomes a river " \
               "of tomato mush. Make sure you wear a shirt that you don’t mind throwing out. Also, you 100% want to " \
               "wear ski goggles or lab goggles, especially if you are tall. Tall people are going to get caught " \
               "in the tomato crossfire a lot more! It is quite the experience and was a lot of fun, but I probably " \
               "don't need to go again.", \
               html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.bunol_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Girona':
        return "Capital of the northern province of Catalonia! It's a cool little city if you want to visit another " \
               "Catalan city.", \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.girona_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Granada':
        return 'Absolutely beautiful city. The Sierra Nevada mountains surround the city and the city itself is ' \
               'quite mountainous too. THe Alhambra castle complex is incredible. The south of Spain was controlled ' \
               'by the Moors for a long time, and each new leader would add a new addition to the Alhambra. However, ' \
               "when the 'Reconquista' culminated in 1492 and Spain once again took control of Granada, " \
               "King Ferdinand and Queen Isabella chose not have the Muslim palace destroyed, but rather " \
               'added their own addition and touches. The resulting structures, that still stand today, are ' \
               'incredible. The gardens there are also so beautiful. ' \
               'Granada has a strong tapas tradition -- meaning that whenever you order drinks you are almost always' \
               'served a tapa to go with the drinks. The food in general is also great.', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.granada_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Irún':
        return 'This is the main city on the Spanish side of the Spain / France border near the coast. ' \
               'Definitely off the beaten path but really nice little city. The view from on top of the mountain ' \
               'at Jaizkibeleko V. Dorrea where you can see the Bidasoa river that divides Spain and France is ' \
               'absolutely beautiful. You can also walk along this river in the city as well, there are plenty ' \
               'of nice bars, restaurants, and shops here!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.irun_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Madrid':
        return 'The Spanish capital! Definitely a different feel than Barcelona but both are amazing cities. ' \
               'Tons of places to visit: Parque de Retiro (for sure see the central pond and the Palacio ' \
               'de Cristal here), Real Palacio, Las Ventas Plaza de Toros (tour is pretty cool to learn ' \
               'about bullfighting history), Puerta del Sol Plaza (famous bear and cherry tree statue), Plaza Mayor, ' \
               'famous art museums (El Prado and Reina Sofia), Templo de Debod (Egyptian temple from 200BC, ' \
               'awesome spot for sunset), Siete Tetas (nice park a little outside the city, also good for sunset), ' \
               'and the Broadway-like street of Gran Vía. Additionally, if you ' \
               "are a soccer fan, there are three teams in Madrid that play in the top league in Spain, " \
               "called Rayo Vallecano, Real Madrid, and Atlético de Madrid.", \
                html.Br(), html.Br(), \
               'Some great restaurants/food spots include Cuevas el Secreto, El MiniBar (go for dinner), San Ginés ' \
               '(super famous hot chocolate and churros -- worth the wait!), Bar Postas or Casa Rúa famous for ' \
               'bocadillos de calamares / calamari sandwiches, Museo del Jamón (a bunch of locations, ' \
               'great ham sandwiches), Bocadillos Oink (get a sandwich with Jamón Serrano -- soooo good), ' \
               'and the Basque restaurant Maitetxe. Also be sure to visit the Círculo de Bellas Artes Terrace. ' \
               'The view is amazing, it costs a few euros to go up but it is well worth it!', \
               html.Br(), html.Br(), \
               'Although there are tons of things to do in Madrid, definitely consider a day trip to either Segovia ' \
               'and / or Toledo. Both are cities with fascinating history, dating back much further than Madrid.', \
               html.Br(), html.Br(), dbc.Carousel(
                    items=[
                        {"src": "assets/spain/mad2.JPG"},
                        {"src": "assets/spain/mad1.JPG"},
                        {"src": "assets/spain/mad.JPG"},
                        {"src": "assets/spain/mad5.JPG"},
                        {"src": "assets/spain/mad3.JPG"},
                        {"src": "assets/spain/mad6.JPG"},
                    ],
                    interval=2000,
                    ride="carousel",
                    className="carousel-fade"
                ),  html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.madrid_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Málaga':
        return 'Nice city on the Costa del Sol (Coast of the Sun)', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/spain/mal.JPG"},
                    {"src": "assets/spain/mal1.JPG"},
                    # {"src": "assets/spain/mal2.JPG"},
                    {"src": "assets/spain/mal3.JPG"},
                    {"src": "assets/spain/mal4.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.malaga_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Mallorca':
        return 'Beautiful island not far from Barcelona. You can actually take a ferry here from Barcelona, or it ' \
               'is a very quick flight. Many people come to enjoy some nice beaches and island tranquility, but ' \
               'there is also a German-speaking part of the island where many Germans come to party. There is a ' \
               'whole German genre of music made for partying on Mallorca.', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.mallorca_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Montserrat':
        return 'Beautiful and really uniquely shaped mountains that are only an hour or so by train inland from ' \
               'Barcelona.', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.montserrat_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Pineda de Mar':
        return 'more info coming soon!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.pineda_de_mar_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'San Sebastián':
        return 'Beautiful city on the northern coast of Spain. It supposedly has the highest density of bars and ' \
               'restaurants in the world. Take the Funicular Monte Igueldo up to Igeldo mendiko behatokia ' \
               'to get an amazing view of the bay and city from above.', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.san_sebastian_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Sitges':
        return 'The carnaval capital of Spain!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.sitges_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Segovia':
        return 'Another small city with fascinating history, Segovia is a very old city that makes for an awesome ' \
               'day trip from Madrid. There is a Roman aqueduct that runs through the main plaza of the city that ' \
               'was built in the year 50! Enjoy a meal on the main plaza with this stunning backdrop. Get the ' \
               'cochinillo — a delicacy that is most famous in Segovia. This is a slow roasted suckling pig that ' \
               'is crazy tender and flavourful. Get the marzipan cake for dessert. This was amazing as well. Enjoy ' \
               'a walk along the aqueduct.  Don’t forget to admire the castle — it looks like something out of a ' \
               'fairytale. Enjoy the architecture as you stroll around the rest of the city. Check out the city ' \
               'gates as well. ', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/spain/seg4.JPG"},
                    {"src": "assets/spain/seg1.JPG"},
                    {"src": "assets/spain/seg2.JPG"},
                    {"src": "assets/spain/seg3.JPG"},
                    {"src": "assets/spain/seg.JPG"},
                    {"src": "assets/spain/seg5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.segovia_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Sevilla':
        return "Such a lovely city in the south of Spain (Andalusia). It’s a decent-sized city but " \
               "extremely walkable. One of the highlights (especially for Star Wars fans) is the " \
               "Plaza de España, which was featured as the main castle in the planet of Naboo in Star Wars! " \
               "Regardless of the Star Wars connection, it is so picturesque with the canal, the bridge, " \
               "the little boats, and the ceramic tiles. ", \
               html.Br(), html.Br(), \
               "Other main things to do and see include the main cathedral (inside you can see " \
               "Christopher Columbus’ tomb), the Royal Alcázar (the Muslim influences are really cool to see, " \
               "and the gardens are beautiful), and the giant mushrooms! The Setas de Sevilla is a large " \
               "wooden structure in the shape of mushrooms with a rooftop walkway and really nice views " \
               "from the top. In December, there is actually an ice skating rink below the structure, " \
               "which I found pretty fun since it can still be quite warm and sunny in winter. Additionally, " \
               "something that is a must for Sevilla is seeing a flamenco show! There is a great traditional " \
               "place called La Carbonería — I would highly recommend. Be sure to also visit the neighborhood " \
               "of Triana across the Canal de Alfonso XIII from the center of Sevilla. Triana is really " \
               "interesting as it used to be the area where all the Jews, Muslims, and gypsies lived " \
               "(while the Catholics lived in the center). Today, it is a very creative and artistic area. " \
               "This is a great place to explore some markets (especially the Mercado de Triana) and buy " \
               "some beautiful colorful ceramics as a gift or as a souvenir! On your way to/from Triana, " \
               "you can also pass the old bullfighting arena (Plaza de Toros) of the city. Lastly, if you " \
               "are a soccer fan, there are two teams in Sevilla that play in the top league in Spain, " \
               "called Real Betis Balompié and Sevilla FC.", \
               html.Br(), html.Br(), \
               "One of the great things about Andalusia is that it is very customary to receive complimentary " \
               "tapas when you order a drink! The food and drink scene in general is so great here — laid back " \
               "yet very lively. Also, as with most places in Spain, be aware that dinner is eaten very late " \
               "here (9pm at the earliest). Some great restaurants include La Santa (right next to Las Setas), " \
               "La Taberna, Taberna Coloniales, and Las Golondrinas (Triana). There is also a rooftop bar with " \
               "amazing views of the main cathedral called La Terraza del EME.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/spain/sev.JPG"},
                    {"src": "assets/spain/sev1.JPG"},
                    {"src": "assets/spain/sev2.JPG"},
                    {"src": "assets/spain/sev3.JPG"},
                    {"src": "assets/spain/sev4.JPG"},
                    {"src": "assets/spain/sev5.JPG"},
                    {"src": "assets/spain/sev10.JPG"},
                    {"src": "assets/spain/sev11.JPG"},
                    {"src": "assets/spain/sev6.JPG"},
                    {"src": "assets/spain/sev7.JPG"},
                    {"src": "assets/spain/sev9.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.sevilla_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Tenerife':
        return 'Amazing island with incredibly diverse wildlife and landscapes. Temperatures here are consistently ' \
               'warm (but not too hot) year round. There are lots of nice beaches (including black sand beaches) and ' \
               'also many opportunities to get out on the water in a boat. We enjoyed an awesome boat trip with ' \
               'captain José -- we were lucky to see tons of ____ whales (size-wise they ' \
               'look much more like dolphins than whales, but still so cool)! There are also some really cool ' \
               'natural swimming pools made up of natural rock formations along the coast, definitely try to visit ' \
               'one! The center of the island is the Teide Volcano. The volcano and ' \
               'the surrounding area make up Teide National Park. One of the most memorable experiences of my life ' \
               'was a Teide day-trip excursion -- we went up the volcano by bus and watched the sunset from the ' \
               'top of the volcano, above the clouds! This was absolutely stunning. We then enjoyed a ' \
               'wonderful dinner at a nearby restaurant, and lastly we found a secluded spot to stargaze. ' \
               'This was equally stunning! This is supposed to ' \
               'be one of the best places in the world to stargaze as it is an island, and the thick clouds beneath ' \
               'us traps much of the light from the cities below the clouds.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/spain/tenerife.JPG"},
                    {"src": "assets/spain/tenerife1.JPG"},
                    {"src": "assets/spain/tenerife2.JPG"},
                    {"src": "assets/spain/tenerife3.JPG"},
                    {"src": "assets/spain/tenerife4.JPG"},
                    {"src": "assets/spain/tenerife5.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.tenerife_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Toledo':
        return 'The original capital of Spain, Toledo is a very old city that makes for an awesome day trip from ' \
               'Madrid. It is a small city that is essentially on a little island, surrounded by city walls and a ' \
               'river / moat. It is known for its mixture or clash of cultures — catholics, jews, and muslims all ' \
               'coexisted here for many, many years until the ______ in 1492, the declaration that required any ' \
               'non-Catholics in Spain to either convert or leave the country. Over 500 years later, there is ' \
               'still a mosque and a synagogue that still stand today. Toledo is also famed as the city where Don ' \
               'Quijote starts his journey in the fictional books by Miguel Cervantes. The citadel that sits atop ' \
               'the city is very cool. Enjoy the old bridge as you enter the old city, and also be sure to make ' \
               'the 20 (?) minute walk south along the opposite side of the river to get a great view of the city. ' \
               'Lastly, make sure to try lots of different marzipan treats — to bring some back for friends! Toledo ' \
               'is known to make maybe the best marzipan in Europe. There is a shop that even has a maybe 10 foot ' \
               'tall Don Quijote made completely out of marzipan! It has some Guinness world record for this.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/spain/toledo.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.toledo_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Valencia':
        return 'The birthplace of paella! Be sure to eat plenty of paella while you’re here. Valencia is on the ' \
               'eastern coast of Spain, but the city center is not quite on the coast. The coast and beaches are ' \
               'not too far but it takes a bit of effort to get there. There is plenty to do in Valencia though — ' \
               'starting off with the Ciudad de Artes y Ciencias (City of Arts and Sciences). The buildings in this ' \
               'area look super futuristic and are really impressive. They look like they could be space ships from ' \
               'the next Star Wars movie. In reality they are actually museums, hence the name of the area. There ' \
               'are some very nice parks in the city. There is also a cool market area where you can eat and drink. ' \
               'Lastly, if you are here in August, make the little trip to Buñol for La Tomatina, the world’s ' \
               'biggest food fight! Select Buñol for more info about that.', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.valencia_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Vilanova':
        return 'more info coming soon!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.vilanova_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Sweden
    if value == 'Stockholm':
        return 'The Swedish capitol is absolutely beautiful! The city itself is made up of ___ islands and they ' \
               'definitely have a different feel. The center island with the old town (___) ' \
               'has some of the picturesque little streets that you may see in pictures online. ' \
               'There are some lovely cafes here. ___ on the water has nice views, awesome open-faced seafood ' \
               'sandwiches, and the traditional Swedish cinnamon rolls that are so good! There are also ' \
               'some great bars and restaurants. I loved the cozy little neighborhood restaurant called ___. ' \
               'We also had so much fun drinking mead out of little ceramic mugs in the underground, ' \
               'viking-themed bar here called ___. ' \
               "The staff are dressed in 'viking' clothes, and there is also live 'viking' music! They have many " \
               'different types of mead, but I think we preferred the classic.', \
               html.Br(), html.Br(), \
               'To the south of ___ is ___. The view of the old town from ___ on this island (first pic below)' \
               'is perhaps the most famous in Stockholm! Right next to this viewpoint, check out a really unique ' \
               "little bridge connecting to someone's apartment! It's called ___"\
               'There are also a couple really cool restaurants / bars ' \
               'here that give you a bit of a view of the old town as well, including __ ' \
               'These are a great idea during the day or at night! ', \
               html.Br(), html.Br(), \
               'Also on ___, you can find a main shopping street (impressively clean), a great beach / swimming ' \
               'area (with a cool dock bar called Loopen Bar), a really fun and quirky open air area / club ' \
               'called ___, and probably most importantly... ' \
               'MEATBALLS ! You need to go to the Meatballs for the People. No, they are not just meatballs. ' \
               'They are worth the wait. There are so many different kinds, so getting the sampler plate (comes ' \
               'with amazing mashed potatoes) is a great idea. ' \
               'sample them all!', \
               html.Br(), html.Br(), \
               'Getting out on a boat is also highly recommended in Stockholm. This is a great way to see more of ' \
               'the islands. We did the a quick tour of the main handful of islands near the old town island ___, ' \
               'but there are many options that go much farther!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/sweden/sto.JPG"},
                    {"src": "assets/sweden/sto1.JPG"},
                    {"src": "assets/sweden/sto2.JPG"},
                    {"src": "assets/sweden/sto3.JPG"},
                    {"src": "assets/sweden/sto4.JPG"},
                    {"src": "assets/sweden/sto5.JPG"},
                    {"src": "assets/sweden/sto6.JPG"},
                    {"src": "assets/sweden/sto7.JPG"},
                    {"src": "assets/sweden/sto9.JPG"},
                    {"src": "assets/sweden/sto10.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.stockholm_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# Turkey
    if value == 'Istanbul':
        return 'Amazing trip with Zach! more coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/turkey/ist.JPG"},
                    {"src": "assets/turkey/ist1.JPG"},
                    {"src": "assets/turkey/ist2.JPG"},
                    {"src": "assets/turkey/ist3.JPG"},
                    {"src": "assets/turkey/ist4.JPG"},
                    {"src": "assets/turkey/ist5.JPG"},
                    {"src": "assets/turkey/ist6.JPG"},
                    {"src": "assets/turkey/ist7.JPG"},
                    {"src": "assets/turkey/ist8.JPG"},
                    {"src": "assets/turkey/ist9.JPG"},
                    {"src": "assets/turkey/ist10.JPG"},

                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.istanbul_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

# USA
    if value == 'Bonneville Salt Flats':
        return 'More info to come', \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/ARB2FxUwGvU?si=tQyMJ2wkoTSY6Fq1",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-ut/bonneville.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.bonneville_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Boston':
        return 'More info to come', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-ma/boston.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.boston_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Champaign':
        return 'Long live the chief!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-il/champaign.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.champaign_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Chicago':
        return 'Home of the Digglers!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-il/chicago.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.chicago_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Copper Mountain':
        return 'awesome skiing', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-co/copper.JPG"},
                    {"src": "assets/usa-co/copper2.JPG"},
                    {"src": "assets/usa-co/copper3.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.copper_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Milwaukee':
        return 'lil Chicago', html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.milw_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Dayton':
        return 'Go to the Wandering Griffin Pub! The namesake for this app!', \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/YyQi6PEiOJk?si=mT2A04PNZRMx7GDV",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.dayton_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Dubuque':
        return 'Jewel of the Mississippi!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-ia/dbq.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.dubuque_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Miami':
        return 'Beautiful latino cultural melting pot. And of course the home of Messi! More info to come!', \
               html.Br(), html.Br(), \
               html.Div(
                   style={"margin-left": "3rem", "margin-right": "3rem", "max-width": "500px", "max-height": "500px",
                          "margin": "auto"},
                   children=[
                       dp.DashPlayer(
                           id="player",
                           url="https://youtu.be/n5q6gziq3KY?si=w35Q-qqbBTYBWYLv",
                           controls=True,
                           width="100%",
                           height="200px",
                       )
                   ]
               ), \
               html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-fl/miami.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.miami_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Missoula':
        return 'more info coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-mt/missoula.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.missoula_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'NYC':
        return 'KATZ', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.nyc_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'San Francisco':
        return 'more info coming soon!', \
               html.Br(), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.san_francisco_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
    if value == 'Seattle':
        return 'more info coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-wa/seattle.JPG"},
                    {"src": "assets/usa-wa/seattle1.JPG"},
                    {"src": "assets/usa-wa/seattle2.JPG"},
                    {"src": "assets/usa-wa/seattle3.JPG"},
                    {"src": "assets/usa-wa/seattle7.JPG"},
                    {"src": "assets/usa-wa/seattle4.JPG"},
                    {"src": "assets/usa-wa/seattle5.JPG"},
                    {"src": "assets/usa-wa/seattle8.JPG"},
                    {"src": "assets/usa-wa/seattle6.JPG"},
                    {"src": "assets/usa-wa/seattle9.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.seattle_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))

    if value == 'Zion National Park':
        return 'more info coming soon!', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"src": "assets/usa-ut/zion.JPG"},
                    {"src": "assets/usa-ut/zion1.JPG"},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ), html.Br(), \
               html.Div(
                   dl.Map([dl.TileLayer(),
                           dl.GeoJSON(data=coordinates.zion_geojson)],
                          style={'height': '35vh', 'max-width': "400px", "margin": "auto"}, center=[25, -40], zoom=1))
