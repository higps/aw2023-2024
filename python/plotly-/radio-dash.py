import dash
import plotly.express as px
from dash import html
from dash import dcc
app = dash.Dash(__name__)

temps_dict = {"Jan":-2, "Feb": -4, "Mar":5, "Apr": 10, "Mai": 15, "Jun": 18, "Jul": 19, "Aug": 18,
"Sep": 13, "Oct": 10, "Nov": 4, "Dec": 2}

celcius = 1
farhenheit = 2

@app.callback(
        dash.dependencies.Output('my_barplot', 'figure'),
        [dash.dependencies.Input('my-slider', 'value'), dash.dependencies.Input('radio', 'value')]
)
def create_bar_plot(slider_value, radio_value):
    months = list(temps_dict.keys())
    temperatures = list(temps_dict.values())
    #1 Farhen, 2 celcius
    if radio_value == celcius:
        range = [-30,50]
        temp = 0
    elif radio_value == farhenheit:
        temp = 9/5*slider_value+32
        range = [-30,100]
    # • C = (F-32)*5/9
    # • F = 9/5*C+32
    for i, values in enumerate(temperatures):
        temperatures[i] += temp
        print(values)

    px_bar_plot = px.bar(x=months, y=temperatures, range_y=range)

    return px_bar_plot

my_dash_header = html.H1('Warmth Conversion')
my_slider = dcc.Slider(min=0, max=250, step=10, value=50, id='my-slider')
my_radio_button = dcc.RadioItems(options=[
            {'label': 'Fahrenheit', 'value': farhenheit},
            {'label': 'Celsius', 'value': celcius}
        ],
        value=2,
        id='radio')

my_bar_plot = dcc.Graph(id='my_barplot')

sliders = html.Div(my_slider)

app.layout = html.Div([my_dash_header, my_radio_button, sliders, my_bar_plot])

if __name__=="__main__":
    app.run_server(debug=True, use_reloader=False)