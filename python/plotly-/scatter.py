import plotly.express as px
import numpy as np
import pandas as pd

x = [1,2,3,4]
y = [6,3,4,5]
x1 = x[::-1]
y1 = y[::-1]


simple_sc = px.scatter(x=x, y=y)
simple_sc.show()

simple_sc_2 = px.scatter(x=x1, y=y)
simple_sc_2.show()

# x = np.arange(10)
# y = np.random.random(10)
# simple_sc_np = px.scatter(x=x, y=y)
# simple_sc_np.show()
