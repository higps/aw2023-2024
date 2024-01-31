import plotly.express as px
import pandas as pd

stages = ["Swipes", "Matches", "Messages", "Conversation", "Meeting up", "Meeting up continuation"]
df_mtl = pd.DataFrame(dict(number=[3645, 2434, 1187, 453, 5, 1], stage=stages))
df_mtl['Status'] = 'Happened'
df_toronto = pd.DataFrame(dict(number=[26417, 1211, 1247,  734, 448, 3], stage=stages))
df_toronto['Status'] = 'Did not happen'
df = pd.concat([df_mtl, df_toronto], axis=0)
fig = px.funnel(df, x='number', y='stage', color='office')
fig.show()
