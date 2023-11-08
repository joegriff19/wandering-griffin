import plotly.graph_objs as go
import pycountry
import pandas as pd
import visited_countries

# fig = go.Figure(go.Scattergeo(
#             # lat=[45.5017, 51.509865, 52.520008],
#             # lon=[-73.5673, -0.118092, 13.404954 ],
#             mode='markers',
#             marker_color='red'),
# go.Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'),
# )

# Create instances for each United Nations member state
un_member_states = list(pycountry.countries)
data = [[country.name, country.alpha_3] for country in un_member_states]
df = pd.DataFrame(data)
df.columns = ['Country', 'Iso_Code']
df['Visited'] = df['Country'].apply(lambda x: 0 if x in visited_countries.visited_countries else 1)

# def spin_globe(df):
fig = go.Figure(data=go.Choropleth(
    locations=df['Iso_Code'],
    z=df['Visited'],
    text=df['Country'],
    colorscale=[
        [0, "rgb(220, 220, 220)"],
        # [1, "rgb(175, 225, 175)"],
        [1, "rgb(175, 225, 175)"]],
    autocolorscale=False,
    reversescale=True,
    showscale=False,
    # marker_line_color='black',
    # marker_line_width=0.5,
    hovertemplate=df['Country'],
    name=""),
)

fig.update_layout(
    margin=dict(l=0, r=0, t=2, b=2),
    hoverlabel=dict(
        bgcolor="black",
        font_size=15,
        # font_family="Rockwell"
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    # width=500, height=500,
    geo=dict(
        bgcolor='rgba(0,0,0,0)',
        showcoastlines=True,
        projection_type='orthographic',
        # center_lon=index.lon_deg,
        # projection_rotation_lon=index.lon_deg,
        # center_lat=0,
        projection_rotation_lat=17,
        showland=True,
        showlakes=False,
        showocean=True,
        showcountries=True,
        landcolor='rgb(231, 231, 231)',
        # countrycolor='rgb(204, 204, 204)',
        oceancolor='rgb(137, 207, 240)',
        showframe=True,
        framewidth=1,
        framecolor='black',  # couleur du contour
    ),
    # updatemenus=[dict(type='buttons', showactive=False,
    #                             y=1,
    #                             x=1.2,
    #                             xanchor='right',
    #                             yanchor='top',
    #                             pad=dict(t=0, r=10),
    #                             buttons=[dict(label='Play',
    #                                           method='animate',
    #                                           args=[None,
    #                                                 dict(frame=dict(duration=50,
    #                                                                 redraw=True),
    #                                                      transition=dict(duration=0),
    #                                                      fromcurrent=True,
    #                                                      mode='immediate')
    #                                                ])
    #                                     ])
    #         ]
)

# fig.update_traces(
#         marker_line_width=0.5,
#         marker_line_color='black',
#     )
# lon_range = np.arange(-100, 260, 25)
#
# frames = [go.Frame(layout=dict(geo_center_lon=lon,
#                                geo_projection_rotation_lon =lon
#                            )) for lon in lon_range]

# fig.update(frames=frames)
    # plot(fig, filename='rotation.html', auto_play=True)