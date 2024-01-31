def int_to_month_year(value, start_year):

    # Ensure the value is non-negative
    value = value % 12

    # Adjust 0 to 11 to match the index of months
    if value == 0:
        value = 12

    # Calculate the number of years and quarters
    years = start_year + value // 12
    quarter = (value - 1) // 3 + 1  # Calculate the quarter (1, 2, 3, 4)

    # Define the list of month names
    months = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    # Return a list containing the corresponding month, year, and quarter (in uppercase)
    return [months[value - 1].upper(), quarter, years]

# Example usage
# start_year = 2013
# result = int_to_month_year(15, start_year)
# print(result)

# Example usage:
# integer_value = 34
# month_name = int_to_month(integer_value)
# print(f"{integer_value} corresponds to {month_name}")
# the_list = [0, 0, 0, 0, 1, 2, 3, 4, 5]
# for i in the_list:
#     print(int_to_month_year(i, start_year))
