import numpy as np
import plotly.graph_objects as go

# Generate data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = np.random.randint(1, 100, size=len(categories))

# Create bar plot
bar_fig = go.Figure(data=go.Bar(x=categories, y=values))

# Show plot
bar_fig.show()
