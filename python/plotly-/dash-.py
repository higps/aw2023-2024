import dash
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from dash import html
from dash import dcc

app = dash.Dash(__name__)

categories = ['Those who know', 'Those who dont know', 'Those who know they dont know', 'Those who dont know they dont know']
type1 = 'Gen Z'
type2 = 'Millenials'
def generate_random_values(imin, imax):
    return np.random.randint(imin, imax+1, size=len(categories))

@app.callback(
        dash.dependencies.Output('graphy', 'figure'),
        [dash.dependencies.Input('my-slider', 'value'), dash.dependencies.Input("my-slider2", "value"), dash.dependencies.Input("dropdown", "value")]
)
def create_bar(val1,val2,val3):
    primary_color = 'rgba(255, 0, 0, 0.5)'
    values = generate_random_values(val1,val2)
    additional_values = generate_random_values(val1,val2)
    additional_color = 'rgba(0, 0, 255, 0.7)'
    n = len(values)
    for i in range(n):
        values[i] += val3

    bar_fig = go.Figure(data=go.Bar(x=categories, y=values, name=type1, marker_color=primary_color))    
    bar_fig.add_trace(go.Bar(x=categories, y=additional_values, marker_color=additional_color, name=type2))
    return bar_fig

# Add an additional bar with a different color
# additional_values = np.random.randint(1, 100, size=len(categories))
# additional_color = 'rgba(0, 0, 255, 0.7)'  # Set the color as needed


graph = dcc.Graph(id='graphy')
header = html.H1('Who knows they know?')

my_slider = dcc.Slider(min=0, max=20, step=1, value=1, id='my-slider')
my_slider2 = dcc.Slider(min=1, max=20, step=1, value=2, id='my-slider2')
dropdown = dcc.Dropdown(id='dropdown', options=[
            {'label': f'Add 1 for {type1}', 'value': 1},
            {'label': f'Add 2 for {type1}', 'value': 2},
            {'label': f'Add 3 for {type1}', 'value': 3}], value=1)

sliders = html.Div([my_slider, my_slider2])

label = html.Label('Select min value of random variance')
label2 = html.Label('Select max value of random variance')
#  labels = [label, label2]

slide_labels = [label,my_slider, label2, my_slider2]



image = html.Img(src=r'/assets/image.webp')

app.css.append_css({
    'external_url': '/assets/styles.css'
})
app.layout = html.Div([header, dropdown, image, label,my_slider, label2, my_slider2,graph])

# Report Title

if __name__=="__main__":
    app.run_server(debug=True, use_reloader=False)