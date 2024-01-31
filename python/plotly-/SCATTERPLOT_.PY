#viktig
import numpy as np
import plotly.graph_objects as go

# Generate random data
np.random.seed(42)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Create scatter plot
scatter_fig = go.Figure(data=go.Scatter(x=x_scatter, y=y_scatter, mode='markers'))

# Show plot
scatter_fig.show()
