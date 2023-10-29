import plotly.graph_objs as go
import numpy as np

fig = go.Figure(go.Scattergeo(
            # lat=[45.5017, 51.509865, 52.520008],
            # lon=[-73.5673, -0.118092, 13.404954 ],
            mode='markers',
            marker_color='red'),
go.Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'),
)

fig.update_layout(
    # height=1000,
    margin=dict(l=0, r=0, t=0, b=0),
        geo=dict(
            bgcolor='rgba(0,0,0,0)',
            # plot_bgcolor='rgba(0,0,0)',
            projection_type='orthographic',
            # center_lon=-180,
            center_lat=0,
            # projection_rotation_lon=-180,
            projection_rotation_lat=10,
            showland=True,
            showcountries=True,
            showocean=True,
            showlakes=False,
            landcolor='rgb(175, 225, 175)',
            oceancolor='rgb(137, 207, 240)',
            countrycolor='rgb(90, 90, 90)',
            projection_scale=0.85,
        ),
    )
fig.update_traces(
        marker_line_width=1,
        marker_line_color='white',
        hovertemplate=(
                '<b>%{customdata[0]} (%{customdata[1]})</b><br>' +
                'Total number of Rockets launched: %{z}<br>'
        )
    )
lon_range = np.arange(-180, 180, 5)

frames = [go.Frame(layout=dict(geo_center_lon=lon,
                               geo_projection_rotation_lon =lon
                           )) for lon in lon_range]

fig.update(frames=frames)