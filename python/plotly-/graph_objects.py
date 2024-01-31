import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
# Graph objects
trace1 = go.Scatter(x=[1,2,3], y=[3,2,1])
fig_1 = go.Figure(data=[trace1])
fig_1.write_html('simple_scatter1.html', auto_open=True)

trace1 = go.Scatter(x=[1,2,3], y=[3,2,1], name='Hvor mye jeg bryr meg')
trace2 = go.Scatter(x=[1,4,6], y=[3,2,1], name='Hvor mye jeg bør bry meg')
trace3 = go.Bar(x=[1,4,6], y=[3,6,1], name='Folk som brydde seg')
trace4 = go.Line(x=[1,2,3,],y=[2,4,6], name='Folk som ga faen')


fig_layout = go.Layout(
    title=go.layout.Title(
        text='Det å bry seg',
        font= go.layout.title.Font(
            color='orange', 
            size=30)
    )
)
fig_2 = go.Figure(data=[trace1,trace2,trace3,trace4], layout=fig_layout)

fig_2.update_layout(
    xaxis_title='Ukedager',
    yaxis_title='Folk'
)

fig_2.show()