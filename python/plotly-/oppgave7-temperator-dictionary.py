import plotly.express as px

def bar_plot():
    # Given dictionary
    temps_dict = {"Jan": -2, "Feb": -4, "Mar": 5, "Apr": 10, "Mai": 15, "Jun": 18, "Jul": 19, "Aug": 18,
                "Sep": 13, "Oct": 10, "Nov": 4, "Dec": 2}

    # Extracting keys and values from the dictionary
    months = list(temps_dict.keys())
    temperatures = list(temps_dict.values())

    # Create a bar chart using plotly.express
    fig = px.bar(x=months, y=temperatures, labels={'x': 'Months', 'y': 'Temperature (°C)'}, title='Monthly Temperatures')

    # Show the plot
    fig.show()
