# Import Packages and other files for app
from app import app, server #NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import random
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import date
today = date.today()
#check2
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

all_options = {
    'Andorra 🇦🇩': ['Pal Arinsal'],
    'Argentina 🇦🇷': ['Buenos Aires'],
    'Austria 🇦🇹': ['Dornbirn', 'Vienna'],
    'Bahamas 🇧🇸': ['Eleuthera', 'New Providence (where Nassau is)'],
    'Belgium 🇧🇪': ['Antwerp', 'Brussels', 'Ghent', 'Leuven'],
    'Bolivia 🇧🇴': ['Cliza', 'Cochabamba'],
    'Bosnia & Herzegovina 🇧🇦': ['Medjugorje', 'Mostar'],
    'Bulgaria 🇧🇬': ['Sofia', 'Varna'],
    'Canada 🇨🇦': ['Banff', 'Calgary'],
    'Chile 🇨🇱': ['Puerto Natales', 'Santiago', 'Torres del Paine', 'Valparaíso / Viña del Mar'],
    'Croatia 🇭🇷': ['Dubrovnik', 'Plitvice Lakes National Park', 'Pula', 'Rovinj', 'Zagreb'],
    'Czechia 🇨🇿': ['Prague'],
    'Denmark 🇩🇰': ['Copenhagen'],
    'Ecuador 🇪🇨': ['Galapagos Islands', 'Quito'],
    'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿': ['London'],
    'France 🇫🇷': ['Paris'],
    'Germany 🇩🇪': ['Berlin', 'Dortmund', 'Dresden', 'Flensburg', 'Hamburg', 'Kiel', 'Lübeck', 'Leipzig', 'Munich',
                   'Stuttgart'],
    'Hungary 🇭🇺': ['Budapest'],
    'Iceland 🇮🇸': ['Reykjavik', 'Southern half of island'],
    'Italy 🇮🇹': ['Bergamo', 'Florence ', 'Milan', 'Rome', 'Vatican 🇻🇦', 'Venice', 'Verona'],
    'Ireland 🇮🇪': ['Cliffs of Moher', 'Dublin'],
    'Mexico 🇲🇽': ['Cancún', 'Mexico City'],
    'Montenegro 🇲🇪': ['Kotor'],
    'Morocco 🇲🇦': ['Tangier'],
    'Netherlands 🇳🇱': ['Amsterdam'],
    'North Macedonia 🇲🇰': ['Skopje'],
    'Poland 🇵🇱': ['Wroclaw'],
    'Portugal 🇵🇹': ['Guincho Beach', 'Lisbon'],
    'Peru 🇵🇪': ['Lima', 'Iquitos'],
    'Slovakia 🇸🇰': ['Bratislava'],
    'Slovenia 🇸🇮': ['Ljubljana'],
    'Spain 🇪🇸': ['Azpeitia', 'Barcelona', 'Begur', 'Bilbao', 'Buñol', 'Girona', 'Granada', 'Irún', 'Madrid', 'Málaga',
                 'Mallorca', 'Montserrat', 'Pineda de Mar', 'San Sebastián', 'Sitges', 'Sevilla', 'Tenerife',
                 'Valencia', 'Vilanova'],
    # 'USA 🇺🇸': ['Arizona', 'California', 'Colorado', 'DC', 'Florida', 'Illinois', 'Indiana', 'Iowa', 'Kentucky', 'Maine',
    #            'Massachusetts', 'Michigan', 'Missouri', 'Montana', 'Nebraska', 'New Hampshire', 'New York',
    #            'North Carolina', 'Ohio', 'Pennsylvania', 'Tennessee', 'Utah', 'Vermont', 'West Virginia', 'Wisconsin',
    #            'West Virginia'],
    'USA 🇺🇸': ['Chicago', 'Champaign', 'Dayton', 'San Francisco', 'NYC'],
}


# state_options = {
#     'Arizona': ['Montaña ski'],
#     'California': ['Buenos Aires'],
#     'Colorado': ['Dornbirn', 'Vienna'],
#     'DC': ['Eleuthera', 'New Providence (where Nassau is)'],
#     'Florida': ['Antwerp', 'Ghent'],
#     'Illinois': ['Champaign', 'Chicago'],
#     'Indiana': ['Medjugorje', 'Mostar'],
#     'Iowa': ['Sofia', 'Varna'],
#     'Kentucky': ['Banff', 'Calgary'],
#     'Maine': ['Puerto Natales', 'Santiago', 'Torres del Paine', 'Valparaíso / Viña del Mar'],
#     'Massachusetts': ['Dubrovnik', 'Plitvice Lakes National Park', 'Pula', 'Rovinj', 'Zagreb'],
#     'Michigan': ['Prague'],
#     'Missouri': ['Copenhagen'],
#     'Montana': ['Galapagos Islands', 'Quito'],
#     'Nebraska󠁧󠁿': ['London'],
#     'New Hampshire': ['Berlin', 'Dortmund', 'Dresden', 'Flensburg', 'Hamburg', 'Kiel', 'Lübeck', 'Leipzig', 'Munich',
#                    'Stuttgart'],
#     'New York': ['Budapest'],
#     'North Carolina': ['Reykjavik', 'Southern half of island'],
#     'Ohio': ['Bergamo', 'Florence ', 'Milan', 'Rome', 'Vatican 🇻🇦', 'Venice', 'Verona'],
#     'Pennsylvania': ['Cliffs of Moher', 'Dublin'],
#     'Utah': ['Cancún', 'Mexico City'],
#     'Vermont': ['Kotor'],
#     'West Virginia': ['somewhere'],
#     'Wisconsin': ['Milwaukee'],
# }


# define sidebar layout
app.layout = html.Div([
   dcc.Location(id="url"),
   content
])

# index page layout
index_layout = html.Div(
    children=[
            html.Header(
                children=[
                    html.Br(),
                    # html.Div(children="wandering griffin", style={"fontSize": "75px"}),
                    html.Div(children="wandering griffin", className="wg"),
                    html.Div(children="travel recs", className="wg"),
                    html.Div(children="🌎", style={"fontSize": "85px"}),
                    html.Div(children="powered by JI", className="powered"),
                    html.Div(children="(Joe's Intelligence)", className="powered"),
                    html.Br(),
                ],
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    # 'background': colors['background']
                }
            ),
            # html.Div(children="Let's travel better", style={'textAlign': 'center', "font-weight": "bold", "fontSize": "20px"}),
            # html.Br(),
            html.Div(children="I have personally been to all of these places and these are all my personal recs!",
                     style={"font-weight": "bold", 'textAlign': 'center', 'color': 'black'}),

            html.Br(),
            html.Div([
                "Select a country",
                dcc.Dropdown(
                    list(all_options.keys()),
                    clearable=False,
                    searchable=False,
                    id='countries-dd'
                ),
                html.Br(),
                html.Div("Select a city / place"),
                dcc.Dropdown(id='cities-dd', options=[], searchable=False, clearable=False),
                html.Br(),
            ], style={
                'textAlign': 'center', 'margin-left': '250px', 'margin-right': '250px',
                'color': 'black',
                # "display": "flex",
                # 'max-width': '500px',
                # 'verticalAlign': 'middle',
                # 'align-items': 'center', 'justify-content': 'center'
                # 'justify': center
                      }
            ),
            html.Div([
                html.Div(id='city_info'),
                html.Br(),
                # html.Div(id='us-city-info'),
                html.Br(),
            ], style={'textAlign': 'center', 'margin-left': '200px', 'margin-right': '200px', 'color': 'black',
              # 'width': '50%',
              # 'verticalAlign': 'middle'
              # 'align-items': 'center', 'justify-content': 'center'
                      }
            )

    ])

# page callback

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
           html.P(f"The pathname {pathname} was not recognised..."),
       ]
    )

@app.callback(
    # Output('cities-dd', 'children'),
    Output('cities-dd', 'options'),
    Input('countries-dd', 'value'),
    prevent_initial_call=True
)
def set_cities_options(selected_country):
    # if selected_country == 'Andorra':
    #     return 'hit the slopes papi'
    # else:
    return [{'label': i, 'value': i} for i in all_options[selected_country]]
    # return 'Select a city / place in ', selected_country, dcc.Dropdown([{'label': i, 'value': i} for i in
    #                                                                     all_options[selected_country]],
    #                                                                    value=[],
    #                                                                    searchable=False, clearable=False,
    #                                                                    id='cities-dd'),


@app.callback(
    Output('city_info', 'children'),
    Input('cities-dd', 'value')
)
def set_display_children(value):

# Andorra
    if value == 'Pal Arinsal':
        return 'Go skiing. Pyrenees mountains are beautiful and very affordable compared to the US. ' \
               'Only ~3-4 hour drive from Barcelona. I stayed in ____ hotel. Nothing fancy but very nice and clean. ' \
               'Would recommend', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"key": "1", "src": "assets/Andorra-44.JPG",
                     "img_style": {"max-height": "500px"}},
                    {"key": "2", "src": "assets/Andorra-4.JPG",
                     "img_style": {"max-height": "500px"}},
                    {"key": "2", "src": "assets/Andorra-10.JPG",
                     "img_style": {"max-height": "500px"}},
                ],
                # controls=True,
                # indicators=True,
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),

# Argentina
    if value == 'Buenos Aires':
        return "The capital of Argentina! One of the most fun weekend trips I’ve ever enjoyed. Be sure to eat lots " \
               "of ‘parilla’ (grilled meat). The ‘choripan’ is a classic and is so good - a grilled chorizo sandwich " \
               "with a chimmichurri sauce. You can (and should) enjoy delicious steak dinners for pretty cheap. " \
               "Everything gets especially cheap if you take advantage of the ‘blue dollars.’ Argentinian pesos have " \
               "continued to decline in value, and because of this many Argentinians would rather store their " \
               "savings in USD rather than pesos. Thus, they are willing to trade you almost twice the current " \
               "exchange rate for your American dollars. This is very common and open on ‘Calle Florida.’ As soon as " \
               "you walk down the street you will here people saying ‘cambia’ (‘change’ in English). Do this as soon " \
               "as you get to Argentina and pay with cash for everything. By doing this everything in the country " \
               "essentially becomes 50% off! Even without this ‘discount,’ Airbnbs are still very cheap. Next — " \
               "absolutely go to a soccer game while you are here. The atmosphere is insane. There are 5 top league " \
               "teams in Buenos Aires, the biggest being Boca Juniors and River Plate. The Boca Juniors stadium, " \
               "called La Bombonera, is many soccer fans’ holy grail of soccer stadiums. We did not go to a " \
               "game there unfortunately, but we went to a San Lorenzo (Pope Francis’ team) game " \
               "and the atmosphere was still like nothing I had ever seen before. You can be sure to get legitimate " \
               "tickets by booking through this website: ______________ " \
               "Santiago is the name of the guy who runs the company. He is from " \
               "Argentina and loves football. You will meet him and any others going to the game at a famous pizza " \
               "place. Buenos Aires has a huge Italian population and here you can try the famous super cheesy " \
               "Argentinan pizza. Be sure to try the most famous one — onions and cheese. After some pizza and beer, " \
               "you will take a private bus to the stadium. The pizza and beer at the restaurant, and the " \
               "transportation to and from the game, are included in your football ticket package. Although we did " \
               "not see a game at La Bombonera, we were still able to do a stadium visit. There was a very big " \
               "game while we were there though — the league game between Boca Juniors and River Plate, " \
               "known as the Súperclasico. These two teams are known to have perhaps the fiercest rivalry of " \
               "any two sports teams on tehe planet. Every bar in the city was packed for game, and Boca " \
               "ended up winning. The streets near the stadium proceeded to celebrate all night long. We grabbed a " \
               "couple beers and joined the celebrations. This was one of the most fun experiences of my life!'"

# Austria
    if value == 'Dornbirn':
        return 'Rhombergers'
    if value == 'Vienna':
        return 'Kuchen'

# Bahamas
    if value == 'Eleuthera':
        return 'ready for an epic sailing trip??'
    if value == 'New Providence (where Nassau is)':
        return 'explore Nassau, eat conch, go to the beach, and listen to Bob'

# Belgium
    if value == 'Antwerp':
        return 'Beware of the Long Wapper'
    if value == 'Brussels':
        # image_path = 'assets/andrea_delirium.gif'
        return 'It is often suggested to skip Brussels and visit other Belgian cities such as Ghent or Antwerp... ' \
               'and while I love these smaller cities of Belgium, I definitely would NOT recommend immediately ' \
               'skipping Brussels for other cities in Belgium. The center of Brussels is really nice. The main ' \
               'square has a huge ____ with hundreds of little statues on the exterior depicting saints. ' \
               'In addition to the main _____, the square has a number of other buildings that are much more ' \
               'stunning in person than in pictures, especially becuase all the gold touches on the buildings ' \
               'really stand out in person. I would highly recommend restaurant __ and ____. There are also ' \
               'a couple really nice cafes in the _____ park in front of the Brussels Palace, called ___ and ___. ' \
               'Would definitely recommend coming for a beverage and  / or some food hwen the weather is nice. ' \
               'It is also absolutely necessary to try the Belgian waffles (in the Liege style, they are somewhat ' \
               'circular in shape). The best ones are from the food trucks called _____. You can find one ' \
               '(or two) in front of the palace, and another one next to the Ferris wheel. Lastly, the ' \
               'Delirium Village is really fun -- especially in the evenings -- definitely enjoy a few beers here! ', \
                # html.Br(), html.Br(), html.Div(html.Img(src=image_path, style={"height": "500px"}))

    if value == 'Leuven':
            return 'What a fun little town really close to Brussels. The main attraction in Leuven is the ____ ' \
                   'and wow it is actually quite stunning. Be sure to also check out the oter main plaza, ___.' \
                   'Enjoy some Stella Artois -- it is brewed here! You can actually visit the brewery, it is not far ' \
                   'at all from the center of the city or the main train station. Be sure to book a tour ahead of time ' \
                   'though as the time slots fill ahead of time.'
    if value == 'Ghent':
        return 'So cute and amazing beer and Delirium'


# Bolivia
    if value == 'Cliza':
        return 'A very small town outside of Cochabamba, this was the destination for the Solidarity Bridge ' \
               'mission trip where I joined as a Spanish interpreter. This is quite far off the beaten path and ' \
               'I would not recommend for tourism purposes, but this will always be a special place for me!'
    if value == 'Cochabamba':
        return 'el Cristo más grande'

# Bosnia & Herzegovina
    if value == 'Medjugorje':
        return 'brr'
    if value == 'Mostar':
        return 'brr'

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
               'kebapcha (caseless sausages with actually some of the best potatoes I’ve ever had).'
    if value == 'Varna':
        return "I would so highly recommend this little gem of a city on the Black Sea. Enjoy the beaches and the " \
               "cheap prices. This is probably the cheapest place I’ve ever been in Europe. The most expensive " \
               "beers I saw were at a craft brewery — and they were just 2.50 Euros! The beach is beautiful. Go to " \
               "the beach club called ’Moonlight.’ You can get all-day access to the club for just 5 euros. You get " \
               "to use the beach chairs and umbrellas and you get a 1.5L bottle of water and a beer. Crazy. You can " \
               "eat here or there are a number of other cafes and bars on the beach. Walk around the port as well. " \
               "‘Craft Beer and Meats’ is on the water at the port. I got to watch a Bulgarian soccer game on TV " \
               "while enjoying sea bass, calamari, and a really good NEIPA (I don’t know what it is about IPAs in " \
               "the Balkans but I really like them — also technically Bulgaria is not in the Balkans but close " \
               "enough and the taste was similar). You can also stroll through the park area by the beach and down " \
               "the main tourist / shopping street, it’s very nice as well. Lastly, the main cathedral of the city " \
               "is also really impressive."

# Canada
    if value == 'Banff':
        return 'The color of the lake is really stunning'
    if value == 'Calgary':
        return 'Cool, clean city'

# Chile
    if value == 'Puerto Natales':
        return 'eat the guanaco and the spider crab and drink the calafate beer'
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
               'option if you are there in winter.'
    if value == 'Torres del Paine':
        return 'The W was stunning start to finish. The Torres on the last morning was an amazing finish. ' \
               'About 50 miles in 4 days. The refugios are really fun to stay in. We stayed at Francés the first ' \
               'two nights and then Chileno on the last night. Breakfast and dinner ' \
               'there is a bit expensive but worth it for the convenience. You can bring snacks as lunch and to get ' \
               'you through the day until dinner. There are tons of rivers and streams with freshly melted glacier ' \
               "water that you can drink, so you don't need to bring any water with you. This was really nice. " \
               "End of September was a good time to go as it wasn't too hot as winter just ended and " \
               "there weren't too many tourists yet. You can also catch the end of ski season in the Andes as well!" \
               "Also the southern-most game of beer die ever was played in this park in Sept 2022. "
    if value == 'Valparaíso / Viña del Mar':
        return 'eat the ceviche. joder'

# Croatia
    if value == 'Dubrovnik':
        return 'cool af'
    if value == 'Plitvice Lakes National Park':
        return 'Really beautiful. It provides a nice contrast to the cities you will likely in Croatia.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"key": "1", "src": "assets/croatia/np.JPG",
                     "img_style": {"max-height": "700px"}},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),
    if value == 'Pula':
        return "Definitely worth a stop. There's a very old Roman arena and nice little port. There are some cool" \
               "shops and restaurants as well. The view of the city " \
               "from the water / parking lot when you enter the city is beautiful as well. This peninsula is so " \
               "fertile and provides great conditions for grapes, olives, and black truffles. Sample frequently.", \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"key": "1", "src": "assets/croatia/dogs.JPG",
                     "img_style": {"max-height": "700px"}},
                    {"key": "1", "src": "assets/croatia/olive_oil.JPG",
                     "img_style": {"max-height": "700px"}},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),
    if value == 'Rovinj':
        return "One of the most picturesque towns I've ever seen, especially from the port. The view of the city " \
               "from the water / parking lot when you enter the city is beautiful as well. This peninsula is so " \
               "fertile and provides great conditions for grapes, olives, and black truffles. Sample frequently."
    if value == 'Zagreb':
        return 'Cool to see the Croatian capital with more of the Germanic influences, compared to the more Italian ' \
               'feel on the coast.', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"key": "1", "src": "assets/croatia/church.JPG",
                     "img_style": {"max-height": "700px"}},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),

# Czechia
    if value == 'Prague':
        return 'tank beer baby -- and Staropramen unfiltered -- yum'

# Denmark
    if value == 'Copenhagen':
        return 'very nice. take the ferry train to/from Germany!'

# Ecuador
    if value == 'Quito':
        return 'go up'
    if value == 'Galapagos Islands':
        return "Maybe the coolest place I've ever been. Week-long cruise with daily snorkeling. We saw penguins, " \
               "sea lions, sting rays, sharks, and more sea turtles than you could ever imagine."

# England
    if value == 'London':
        return "Yes it can be expensive but it is a really great city. Tons of history and of course... " \
               "the world mecca for football. If there are no games when you are here but you " \
               "like soccer (or sports in general), consider doing a stadium tour. My biased opinion would be " \
               "Arsenal's Emirates Stadium (GO GUNNERS !) Be sure to go to Big Ben, Buckingham Palace, Harrod's" \
               "(try a meat pie), " \
               "and Tower Bridge. Many people think that Tower Bridge is London Bridge, but no -- the famous pic is " \
               "from the south side of the River Thames between London Bridge and Tower Bridge. Be sure to walk " \
               "across the Tower Bridge as well." \
               "Also enjoy Hyde Park (a bike ride here is great). One of the best areas in the city is " \
               "Camden Market. The area is cute with some little canals, and there are tons of food and drink " \
               "stands / vendors. You cand just about any cuisine here. Get some food and drinks here. " \
               "There is a lot of great beer here too. There are lots of awesome " \
               "old-timey pubs: The Toucan, The Cross Keys, The Harp, The Seven Stars, The Blackfriar, and more. " \
               "Hop Locker is also a sweet beer bar by the river. " \
               "Many pubs and bars will also have a good fish & chips. Make sure to try some cask ales / real ales. " \
               "They are known as Britain's national drink. It's a unique beer style to the UK. But be warned, " \
               "the beers are not served very cold. The idea is so you can taste " \
               "the flavors more (which is scientifically true). If you like Guinness, " \
               "try the London Black beer -- it's a modern take on an old English style dark porter. If you have " \
               "time, there is a whole strip of breweries (Brew by Numbers, Anspach & Hobday, and more) all right " \
               "under the train, it's a cool setup. " \
               "So... lots to do here. I could definitely live here."

# France
    if value == 'Colmar':
        return 'Colmar is a small city but really goes all out for Christmas. It is a really cute little city, and ' \
               'it is actually wild how many tourists come to visit the Christmas markets. If you have the time, it ' \
               'is definitely worth a day trip from Strasbourg.'
    if value == 'Paris':
        return 'It is expensive and many people prefer other parts of France... but worth it to see Messi! JK ' \
               'there is also plenty to do besides see Messi. Of course visit the Eiffel Tour -- catch some great ' \
               "views from train line 6. Also be prepared for the little 'light show' that happens " \
               "on the hour after the sun goes down. Also visit Arc de Triomphe, the Champs-Élysées street for " \
               "shopping, and the Louvre. Mona Lisa lives here. You could " \
               'spend days in here so have an idea of what you want to see. Definitely enjoy the Montmarte ' \
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
                    {"key": "1", "src": "assets/paris/messi.JPG",
                     "img_style": {"max-height": "700px"}},
                    {"key": "1", "src": "assets/paris/louvre.JPG",
                     "img_style": {"max-height": "700px"}},
                    {"key": "1", "src": "assets/paris/cafe.JPG",
                     "img_style": {"max-height": "700px"}},
                    {"key": "1", "src": "assets/paris/senne.JPG",
                     "img_style": {"max-height": "700px"}},
                    {"key": "1", "src": "assets/paris/steak_restaurant.JPG",
                     "img_style": {"max-height": "700px"}},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),

    if value == 'Strasbourg':
        return 'Known as the ‘Capital of Christmas,’ Strasbourg is quite magical for Christmas. There are so many ' \
               'lights and markets all over the city. Christmas season or not, be sure to walk around the ‘Petite ' \
               'Paris’ area. It is really cute. More recs to come___. A day trip to Colmar is also a great idea, ' \
               'especially during Christmas time.'

# Germany
    if value == 'Berlin':
        image_path = 'assets/berlin/berliner_dom.JPG'
        return "'Poor but sexy' has become the city motto after the mayor said this back in 2003. " \
               "So much to do here. There is always " \
               "something happening. It's a very creative, unique, fun, and often quirky city. The club scene " \
               "(especially techno) is world famous. Berghain is the " \
               "name of the Berlin's most famous club (and maybe the world's most famous club). It opens Friday " \
               "night and does not close until noon on Monday. If you want to go, be prepared " \
               "to wait a long time in line and know that there is a good chance you will not be let in -- it's part " \
               "of the funky culture that preserves the hype and exclusivity aura of the club. For other club " \
               "options, try Watergate, Tresor, Club der Visionäre, or Ritter Butzke. For a really fun bar that " \
               "isn't exactly a club, go to minimal bar. Beyond the clubs, " \
               "there are tons of concerts here every day and there are always " \
               "people playing music on the streets (especially around Museum Island) as well. Lots of fun " \
               "bars as well. There is an unreal rooftop at Klunkenkranich. Great craft beers and a good time at" \
               "Kaschk, Muted Horn, Hops & Barley, Protokoll, and Straßenbräu. Berlin may also randomly " \
               "have the most beaches of any city in the world. In many parks there are sand volleyball courts " \
               "and there are so many beach bars in parks and on the rivers around the city as well. There are so " \
               "many parks, including maybe the coolest park ever, which is an old airport that has now become a " \
               "massive park right in the city. Another awesome park is Treptower Park. There are lots of sports " \
               "here as well (to watch and play). The pro " \
               "basketball (Alba), soccer (2 teams: Hertha and Union), handball (Füchse), and ice hockey (Eisbären) " \
               "games all provide really fun atmospheres. Be sure to eat a döner kebab (a variation of a Turkish " \
               "kebab that originated in Berlin -- the best place is Nefi's), currywurst (Curry 36 is great), and " \
               "vietnamese food (the duck at New Day is crazy good). For German food, 'Max & Moritz' is a " \
               "really cool restaurant with great food and beers. There is also the Hofbrauhaus Berlin for very " \
               "fun and festive Bavarian food, beers, live music, and good vibes. Lastly, there is also a lot of " \
               "great middle eastern food, especially yemenite food at the 'Jemenitisches Restaurant' " \
               "and Syrian food at the 'Aleppo Supper Club.'", \
               html.Br(), html.Br(), html.Div(html.Img(src=image_path, style={"height": "500px"})),
    if value == 'Dortmund':
        return "Home to Borussia Dortmund! Go to a football game. It's known to be one of the best game atmospheres " \
               "in the world."
    if value == 'Dresden':
        return 'Home to one of the biggest and most amazing Christmas markets in the world. The medieval Christmas' \
               "market is also really cool. Be sure to try the 'Handbrot.' A famous dessert from here " \
               "during Christmas is ______. The one with marzipan in the middle is so good. " \
               "You can come here on a day trip from Berlin."
    if value == 'Flensburg':
        return 'Really cute port area and home to the Flensburger brewery. The tour is really cheap and you get ' \
               "a lot of food and beer. They have the best marketing by any company I've ever seen."
    if value == 'Hamburg':
        return 'A beautiful city in the north of Germany. The port of Hamburg is bigger than the entire city of ' \
               'Copenhagen. There are also more bridges than Amsterdam, Venice, and London combined! If you like ' \
               'seafood you are in luck, the fresh fish sandwiches (Fischbrötchen) are so good. Go to Brücke 37 ' \
               'on port. At the port you will also see the iconic new concert hall called the Elbphilharmonie, ' \
               'with its roof resembling and reflecting the waves of the water below. Go up to the top of the ' \
               'nearby church, ____ to get great views of the port and of the concert hall. Be sure to walk ' \
               'through the Speicherstadt, the beautiful storage area for all incoming goods coming by boat ' \
               'to the city. Have a drink at the little castle in this area, called the ______. Also be sure ' \
               'to visit the Hamburger version of the Amsterdam red light district, St. Pauli. ' \
               'Different than Amsterdam though in that this was formerly the outside of the city of Hamburg ' \
               'and thus became the more expressive and creative area, with music, art, and bars ' \
               '(and also prostition). There are tons of fun bars and clubs' \
               'here. The Beatles wrote their first album here and have actually played more shows in ' \
               'St. Pauli than anywhere else in the world. The football team has also gained a cult ' \
               'following worldwide as they really represent the ' \
               'neighborhood well -- as a foil to the historically much more successful Hamburger SV, supporting the ' \
               'LGBTQ community by wearing a rainbow captain armband, and by often making demonstrations for various ' \
               'human rights issues. Go to a game if you can!'
    if value == 'Kiel':
        return 'My home on the coast of the Baltic Sea for a little less than a year after college. ' \
               'Definitely not the most happening place in Germany ' \
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
               "successful handball teams in the world. The handball games are actually pretty electric."
    if value == 'Lübeck':
        return 'Home to some of the best marzipan in the world. I actually only played a basketball game here ' \
               "but we won ;) It's supposed to be very cute and have a really nice Christmas market."
    if value == 'Munich':
        return 'If you like to have fun and drink beer then Oktoberfest is ' \
               'a must at some point. Munich is where the one true Oktoberfest is held. There are other ' \
               'celebrations around Germany but nothing compares to the real deal. Beyond Oktoberfest -- it is ' \
               'the capital of Bavaria. Very pretty city. Bavaria is home to some beautiful mountains, the ' \
               'fairtyale-like castle called Neuschwanstein that inspired the Disney castle, one of the ' \
               'most successful (but annoying) football teams in the world in Bayern Munich, ' \
               'and also home to some of the best beers in the world. Some of their most delicious ' \
               '(and most unique) beers are the wheat beers (Weissbier / Weißbier / Hefeweizen). ' \
               'The Englischer Garten park is beautiful -- people surf ' \
               "it's fun to watch people surf here on a little artificial wave canal and there " \
               "is a really cool beer garden at the base of the Chinese Tower. You have to visit " \
               "the Hofbraühaus as well - the most iconic beer hall in the world. There is always " \
               "live music and the vibes are immaculate. " \
               "It was originally founded as the royal brewery and for hundreds of " \
               "years it has been the primary gathering place in the city, even for political matters. The Nazi " \
               "party was actually officially established here, and not long after Hitler was officially named " \
               "the leader of the Nazi party here as well. Lastly, there is some nice shopping " \
               "along ___ near the " \
               "famous and beautiful main square of the city, Marienplatz, where the town hall (Rathaus) is."
    if value == 'Stuttgart':
        return 'Was only here briefly but the main Christmas market was nice'

# Hungary
    if value == 'Budapest':
        return 'Coolest parliament building in the world? The ruin pubs (makeshift pubs out of buildings ' \
               'that were damaged in WW2 and then abandoned) are really quirky, creative, and fun. ' \
               'Be absolutely sure to climb up the __ to see Lady Freedom (formerly called "Lady Communism"). ' \
               'The view of the river and the city ' \
               'down below is amazing. Go to the famous Szyzyzyzy bath too.'

# Iceland
    if value == 'Reykjavik':
        return "Cool city but don't stay too long -- get out and explore the nature in the 'Land of Fire and Ice.'" \
               "There are some unique foods here that are really good and you should try." \
               "Go to ____ restaurant. They had an amazing whale fin steak and a crazy " \
               "good reindeer burger. We didn't see puffin on a menu but it is also eaten here." \
               "See the rainbow road. Check out the Viking church and go to the top of it."
    if value == 'Southern half of island':
        image_path = 'assets/iceland/hottub.JPG'
        return 'so much to see in not enough time', \
               html.Br(), html.Br(), dbc.Carousel(
                items=[
                    {"key": "1", "src": "assets/iceland/hotspring.JPG",
                     "img_style": {"max-height": "700px"}},
                    {"key": "1", "src": "assets/iceland/hottub.JPG",
                     "img_style": {"max-height": "700px"}},
                ],
                interval=2000,
                ride="carousel",
                className="carousel-fade"
                ),

# Italy
    if value == 'Bergamo':
        return 'DO NOT immediately overlook Bergamo in favor of Milan. A lot of budget airlines that ' \
               'fly to "Milan" ' \
               'actually fly to the nearby city of Bergamo. It is a really cute city and they invented ' \
               'Stracciatella gelato. Take the litte cable car up to the high part of the city and walk ' \
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
               'more traditional than pasta in the north of Italy.'
    if value == 'Florence':
        return 'Maybe my favorite city in Italy. The __ river runs right through the city and the sun sets ' \
               'beautifully over it (at least in April when I went!). DO NOT come here without ' \
               'visiting the world ' \
               "famous sandwich shop All'Antico at least once... I would recommend coming multiple times. " \
               "For just 5 " \
               "euros (in 2017) you get a huge sandwich on lovely focaccia bread topped high with the freshest " \
               "mozarrella, tomatoes, and prosciutto, finished with this black truffle sauce that is " \
               "just too good. " \
               "Visit the cathedral (duomo in Italian) and be sure to climb up to the Michaelangelo plaza with a " \
               "bottle of wine to get beautiful views of the whole city, with the duomo taking center stage. " \
               "You are " \
               "in Tuscany, so a day trip to visit vineyards is also a great idea. There are a number of " \
               "options for this."
    if value == 'Milan':
        return 'The center of the city with the cathedral (duomo in Italian) and the arcade to the left of ' \
               'the duomo are really nice. In the south of the city the Navigli district is awesome -- ' \
               'along a river/canal, there are tons of restaurants with massive buffets that offer really good ' \
               'all you can eat happy hour ' \
               'deals. Go to this fun bar with weirdly-shaped beer glasses called ____. Be sure to have some ' \
               'risotto, more traditional than pasta in the north of Italy. The city is also home to the ' \
               'legendary San Siro stadium where both of the very successful football teams, AC Milan and ' \
               'Internazionale (Inter for short) Milan, play. However, beyond this, Milan feels like ' \
               'more of a place to shop luxury brands and eat fancy meals.'
    if value == 'Rome':
        return 'So much fascinating history here. The food scene is also incredible. ' \
               'The city is quite big too with so many different neighborhoods, all deserving of some time ' \
               'being spent there. However, in a short ' \
               'trip, be sure to visit the coliseum and eat as much pizza, pasta, and gelato as possible.'
    if value == 'Venice':
        return 'It is definitely as charming as everyone says it is. Visit the main plaza (St. Marco) and church, ' \
               'go to the top of the tower there for great views of the city, take a boat ride (the boat usually ' \
               'has a fixed cost no matter the size of your group -- find some new friends to lower the cost per ' \
               'person!), and just enjoy the lovely ambiance.'
    if value == 'Verona':
        return 'The setting from the famous Romeo and Juliet play -- Verona is a beautiful city ' \
               'that probably does ' \
               'not get enough attention. Verona boasts a large coliseum-like arena that is actually older than ' \
               'the coliseum. The ___ river that runs through the city is really nice. Climb up the ___ hill to ' \
               '__ for stunning sunset views over the city. Also go to this little pizza spot called ' \
               'Wallet Pizza ' \
               'for really cheap and ridiculously good pizzas that are made fresh and cook in literally ' \
               'one minute. ' \
               'Be sure to have some risotto, more traditional than pasta in the north of Italy. I also had ' \
               'life-changing amaretto gelato at a little shop called ___. Lastly, a really good restaurant is ' \
               '________.'

# Ireland
    if value == 'Cliffs of Moher':
        return 'Awesome (big) day trip from Dublin. They are amazing. My trip also included cool little stops at ' \
               'castles ___ and ___.'
    if value == 'Dublin':
        return 'There is just such a special charm to this city. Go and drink Guinness and enjoy. Sláinte!'

# Mexico
    if value == 'Cancún':
        return 'The beaches in the Riviera Maya are beautiful. One can obviously come here to party, but ' \
               'visitng the Mayan'
    if value == 'Mexico City':
        return "What a city. Weather is temperate year round. So much good cheap food. The tamales with mole " \
               "just might change your life. Surprisingly there really don't seem to be too many tourists." \
               "Obviously also get lots of tacos, but also try ______. " \
               "Take a little trip on one of the little boats and get ready to see the world's largest floating " \
               "market. Having a mariachi band step onto your boat and play a few songs while drinking beers, " \
               "eating elote, and floating down the river is just truly a beautiful life experience. " \
               "Be sure to have a good amount of cash for this. " \
               "Also see the Frida Kahlo house and check out __ market. It is 100% authentic and you can try " \
               "ants, crickets, and even scorpions if you are feeling ambitious. It definitely helps to " \
               "speak some Spanish, as there are not a lot of tourists." \
               'Mexico City is also home to the legendary Azteca football stadium, where the Mexico national ' \
               'team plays as well as Clúb America. Seeing a game here is absolutely on my bucket list. ' \
               'Lastly, Ubers are also really cheap which makes it easy to get around, as it is quite a big city.'

# Montenegro
    if value == 'Kotor':
        return "Just as cool as Dubrovnik but not as sexy. It's smaller and way more of an authentic feel. " \
               "Not many tourists here."

# Morocco
    if value == 'Tangier':
        return 'I felt more culture shock here than anywhere in Europe. The newer part of the city has a European ' \
               'feel as this used to be the gateway from Europe to Africa (and vice versa) before air travel. ' \
               'However, inside the old city walls of Tangier (the Kazbah) is a whole different story.' \
               'There are a number of locals here who will as you where you are going or if you want to eat ' \
               'something. I think restaurants compensate them if they bring people to their restaurant. However, ' \
               'once you are with a local no one else will bother you. Getting a guide for a day is not too ' \
               'expensive, and will likely also set you up to go a city near the beach and ride camels, which ' \
               'as you can imagine is a really fun unique experience. The food there is great -- the crepe like ' \
               'pancakes for breakfast, chicken tagine, ____. Also go to Cafe ___. Jimmy Hendrix liked going here ' \
               'and the view of the water is really nice. You can even see the south of Spain in the distance.'

# Netherlands
    if value == 'Amsterdam':
        image_path = 'assets/amsterdam/amsterdam_boat.JPG'
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
               html.Br(), html.Br(), html.Div(html.Img(src=image_path, style={"height": "500px"})),

# North Macedonia
    if value == 'Skopje':
        return 'Really cool authentic Balkan city with not so many tourists. This was the home / birthplace ' \
               "of Alexander the Great. There is a huge statue of him on the main plaza, and it's funny there a big " \
               "sign for a Macedonian beer company right behind him -- CKO(pi)CKO / Skopsko. " \
               "The Alexander the Great statue is just one of seemingly hundreds of statues in the city. Keep an " \
               "eye out as you walk around, they are fun. " \
               "Be sure to climb up to the fortress that overlooks the city. Ideally for sunset. There's an " \
               "amazing view of the city and the snow-covered mountains in the background. " \
               "The old town / bazaar is really cool. Just walk around and explore. I went to ___ and it was really " \
               "good. Get the kebap and the Shopsko salad. " \
               "Prices for everything are pretty " \
               'cheap. My hostel was only 10 euros per night (8 bed dorm in Hi Skopje Hostel). The woman who ' \
               'runs the place was so nice ' \
               'and gave great recommendations. She also shared some of her homemade rakija, a local liquor. '

# Poland
    if value == 'Wroclaw':
        return 'Very pretty small city. The people were all very nice. Go to the market square and check out some ' \
               'of the cafes and restaurants. The ___ restaurant is really great -- this is also a great option ' \
               'because there is a lot about the history of Wroclaw and Poland on the walls of the ' \
               'restaurant and in the menu. Definitely get pierogi. Soups are very good and traditional too. ' \
               'Be on the lookout for the hundreds of little gnomes around the city as you walk around. They are ' \
               'really fun and funny. They are a recent project that is inspired by ____. Lastly, go north of the ' \
               'market square and walk around the river / island area -- the churches there are really nice as well.'

# Portugal
    if value == 'Lisbon':
        return 'Beauty'
    if value == 'Guincho Beach':
        return 'Not too far of a drive from Lisbon -- I was lucky to meet someone with a car and we drove here. ' \
               "There are big sand dunes next to the coast. There's also a couple cafes here where you can grab a" \
               "drink or a bite to eat. Sunset here over the ocean was just beautiful. "

# Peru
    if value == 'Lima':
        return 'gotta go back'
    if value == 'Iquitos':
        return 'The start of my Amazon river adventure. We flew here from Lima and took a boat about 50 miles down ' \
               'the Amazon. We then stayed in a few remote places in the rain forest before coming back to ' \
               'Iquitos. Really an adventure of a lifetime. If you have the opportunity to do something like this,' \
               'DO IT !'

# Slovakia
    if value == 'Bratislava':
        return 'What a fun little city with a cool old town and a really cool citadel that overlooks the city and ' \
               'the river that runs through it.'

# Slovenia
    if value == 'Ljubljana':
        return 'The smallest European capital and what a cute little city it is. I went in October and the trees ' \
               'lining the river were beautiful colors. The city is very clean and the people are really nice. ' \
               'Climb up to the citadel to see the city from above. Eat some goulash. Great place for sunset as well.' \
               "Fun fact: George W Bush the second landed here for some conference and greeted the people of " \
               "'Slovakia.'"

# Spain
    if value == 'Azpeitia':
        return 'Birthplace of St. Ignatius and home to a large festival on July ___ each year for his feast day'
    if value == 'Barcelona':
        return 'mamacita'
    if value == 'Begur':
        return 'Really nice beaches if you want to visit nice beaches outside of Barcelona'
    if value == 'Bilbao':
        return "Capital of the Basque country. I didn't spend too much time here but worth a stop. "
    if value == 'Buñol':
        return "Home of the world’s biggest food fight! It happens in August every year. It is a tiny town with " \
               "probably little to no tourism for most of the year besides this weekend. Trucks upon trucks bring " \
               "tomatoes that weren’t quite up to the country’s high standards to be sold for consumption. These " \
               "trucks then push through the super narrow streets of ___, and there are even people in front of the " \
               "trucks to push the crowds off to the side so the trucks can pass through. As the truck passes, " \
               "people standing on the truck throw and shovel the tomatoes into the crowds. People in turn throw " \
               "these tomatoes around again and again. By the end, the entire street becomes a river of tomato " \
               "mush. Make sure you wear a shirt that you don’t mind throwing out. Also, you absolutely want to " \
               "wear ski goggles or lab goggles, especially if you are tall. Tall people are going to get caught " \
               "in the tomato crossfire a lot more! It is quite the experience and was a lot of fun, but I probably " \
               "do not need to ever go again. I would probably only ever recommend coming to ___ for La Tomatina, FYI. "
    if value == 'Girona':
        return "Capital of the northern province of Catalonia. It's a cool little city if you want to visit another " \
               "Catalan city."
    if value == 'Granada':
        return 'Absolutely beautiful city. The Sierra Nevada mountains surround the city and the city itself is ' \
               'quite mountainous too. THe Alhambra castle complex is incredible. The south of Spain was controlled ' \
               'by the Moors for a long time, and each new leader would add a new addition to the Alhambra. However, ' \
               'when the ___ happened in 1492 and all people were forced to either convert to Christianity or leave' \
               'the country, King Ferdinand and Queen Isabella did not have the Muslim palace destroyed, but rather ' \
               'added their own addition and touches. The result is awesome. The gardens are also beautiful. ' \
               'Granada has a strong tapas tradition -- meaning that whenever you order drinks you are almost always' \
               'served a tapa to go with the drinks. The food in general is also great.'
    if value == 'Irún':
        return 'This is the main city on the Spanish side of the Spain / France border near the coast. ' \
               'Definitely off the beaten path but really nice little city. The view from on top of ___ mountain ' \
               'where you can see the river that divides Spain and France is beautiful and really neat to see.'
    if value == 'Madrid':
        return 'The Spanish capital. Definitely a different feel than Barcelona but both are amazing cities.'
    if value == 'Málaga':
        return 'Nice city on the Costa del Sol (Coast of the Sun)'
    if value == 'Mallorca':
        return 'Beautiful island not far from Barcelona. You can actually take a ferry here from Barcelona, or it ' \
               'is a very quick flight. Many people come to enjoy some nice beaches and island tranquility, but ' \
               'there is also a German-speaking part of the island where many Germans come to party. There is a ' \
               'whole German genre of music made for partying on Mallorca.'
    if value == 'Montserrat':
        return 'Beautiful and really uniquely shaped mountains that are only an hour or so by train inland from ' \
               'Barcelona.'
    if value == 'Pineda de Mar':
        return 'ole'
    if value == 'San Sebastián':
        return 'Beautiful city on the northern coast of Spain. It supposedly has the highest density of bars and ' \
               'restuarants in the world. Go up to ___ to get a great view of the bay and city from above.'
    if value == 'Sitges':
        return 'The carnaval capital of Spain'
    if value == 'Segovia':
        return 'Another small city with fascinating history, Segovia is a very old city that makes for an awesome ' \
               'day trip from Madrid. There is a Roman aqueduct that runs through the main plaza of the city that ' \
               'was built in the year 50! Enjoy a meal on the main plaza with this stunning backdrop. Get the ' \
               'cochinillo — a delicacy that is most famous in Segovia. This is a slow roasted suckling pig that ' \
               'is crazy tender and flavourful. Get the marzipan cake for dessert. This was amazing as well. Enjoy ' \
               'a walk along the aqueduct.  Don’t forget to admire the castle — it looks like something out of a ' \
               'fairytale. Enjoy the architecture as you stroll around the rest of the city. Check out the city ' \
               'gates as well. '
    if value == 'Sevilla':
        return 'ole'
    if value == 'Tenerife':
        return 'ole'
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
               'tall Don Quijote made completely out of marzipan! It has some Guinness world record for this.'
    if value == 'Valencia':
        return 'The birthplace of paella! Be sure to eat plenty of paella while you’re here. Valencia is on the ' \
               'eastern coast of Spain, but the city center is not quite on the coast. The coast and beaches are ' \
               'not too far but it takes a bit of effort to get there. There is plenty to do in Valencia though — ' \
               'starting off with the Ciudad de Artes y Ciencias (City of Arts and Sciences). The buildings in this ' \
               'area look super futuristic and are really impressive. They look like they could be space ships from ' \
               'the next Star Wars movie. In reality they are actually museums, hence the name of the area. There ' \
               'are some very nice parks in the city. There is also a cool market area where you can eat and drink. ' \
               'Lastly, if you are here in August, make the little trip to ____ for La Tomatina, the world’s biggest ' \
               'food fight! Select ____ for more info about that.'
    if value == 'Vilanova':
        return 'ole'

    if value == 'Champaign':
        return 'long live the chief'
    if value == 'Chicago':
        return 'sweet home Chicago'
    if value == 'Milwaukee':
        return 'lil Chicago'
    if value == 'Dayton':
        return 'Go to the Wandering Griffin Pub!'
    if value == 'San Francisco':
        return 'daa Bay'
    if value == 'NYC':
        return 'KATZ'
