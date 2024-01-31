import numpy as np
import plotly.graph_objects as go

# Generate data
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)

# Create line plot
line_fig = go.Figure(data=go.Scatter(x=x_line, y=y_line, mode='lines'))

# Show plot
line_fig.show()
