import dash
import plotly.express as px
from dash import html
from dash import dcc
temps_dict = {"Jan":-2, "Feb": -4, "Mar":5, "Apr": 10, "Mai": 15, "Jun": 18, "Jul": 19, "Aug": 18,
"Sep": 13, "Oct": 10, "Nov": 4, "Dec": 2}

months = list(temps_dict.keys())
temperatures = list(temps_dict.values())

radio_value = 1
slider_value = 10

x_val = months
y_val = temperatures
#1 Farhen, 2 celcius
celcius = 2
farhenheit = 1
if radio_value == celcius:
    temp = (slider_value-32)*5/9
elif radio_value == farhenheit:
    temp = 9/5*slider_value+32
# • C = (F-32)*5/9
# • F = 9/5*C+32
print("pre ", temperatures)
for i, values in enumerate(temperatures):
    print(values)
    temperatures[i] += temp
print("post ",temperatures)
px_bar_plot = px.bar(x=x_val, y=y_val, range_y=[-30,50])