import plotly.express as px
import numpy as np

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
#fig.show()

x = [1,2,3,4,5,6]
y = x
x = np.arange(10)
Y = np.random.random_integers(10)
print(x1)
fig2 = px.line(x=x, y=y)
#fig2.show()