import dash
import dash_bootstrap_components as dbc
# Dash instance
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
        __name__,
        title='Wandering Griffin Travel',
        external_stylesheets=[dbc.themes.QUARTZ],
        suppress_callback_exceptions=True
        )
server = app.server # NEED THIS FOR RENDER
