import dash
import plotly.express as px
import plotly.graph_objects as go
from dash import html
from dash import dcc

app = dash.Dash(__name__)

#defining the data
x_cords = [0,1,2,3,4]
y_cords = [5,3,2,7,12]
primary_color_with_alpha = 'rgba(86, 84, 98, 0.5)'
reset_table = -1

@app.callback(
        dash.dependencies.Output('graph', 'figure'),
        [dash.dependencies.Input('my-slider', 'value'), dash.dependencies.Input("radio-button", "value")]
)
def create_bar(slider_val,button_index):

    if (button_index == reset_table):
        bar_fig = go.Figure(data=go.Bar(x=x_cords, y=y_cords, name="Suit Figure", marker_color=primary_color_with_alpha))
    else:  
        #copy the list so we don't override the original with the new values  
        values = y_cords.copy()
        values[button_index] = slider_val
       
        bar_fig = go.Figure(data=go.Bar(x=x_cords, y=values, name="Suit Figure", marker_color=primary_color_with_alpha))    
    return bar_fig


graph = dcc.Graph(id='graph')
header = html.H1('Suit Sales Per Weekday')

my_slider = dcc.Slider(min=0, max=max(y_cords)*2, step=1, value=1, id='my-slider')
my_radio_button = dcc.RadioItems(options=[                  
            {'label': 'Monday', 'value': 0},
            {'label': 'Tuesday', 'value': 1},
            {'label': 'Wednesday', 'value': 2},
            {'label': 'Thursday', 'value': 3},
            {'label': 'Friday', 'value': 4},
            {'label': 'Reload original graph', 'value': reset_table},
        ],
        value=0,
        id='radio-button')

app.css.append_css({
    'external_url': '/assets/styles.css'
})
app.layout = html.Div([header, my_slider, my_radio_button,graph])

if __name__=="__main__":
    app.run_server(debug=True, use_reloader=False)
