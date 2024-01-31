import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Norway'")
fig = px.bar(data_canada, x='year', y='pop')
# fig.show()

df = px.data.gapminder().query("continent == 'Europe'")
fig = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='country',
             labels={'pop':'population of Canada'}, height=400)
# fig.show()

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df, y='pop', x='country', text_auto='.2s',
            title="Controlled text sizes, positions and angles")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
# Sort the bars alphabetically by country
fig.update_layout(xaxis={'categoryorder':'total ascending'})
fig.show()