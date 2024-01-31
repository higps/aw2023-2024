import plotly.express as px

def scatter_plot():
    # Define x values ranging from 1 to 10
    x_values = list(range(1, 11))

    # Calculate y values as squares of x values
    y_values = [x ** 2 for x in x_values]

    # Create a scatter plot using plotly.express
    fig = px.scatter(x=x_values, y=y_values, labels={'x': 'X Values', 'y': 'Y Values'}, title='Scatter Plot: y = x^2')

    # Show the plot
    fig.show()