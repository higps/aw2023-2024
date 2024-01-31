# Go back to ex_if_else_bool exercise 2, implement the
# same logic, but using dict instead of if/elif/else. Test the
# program to make sure it works as it should.

month_short = "MAY"

month_dict = {
    "JAN": "JANUARY",
    "FEB": "FEBRUARY",
    "MAR": "MARCH",
    "APR": "APRIL",
    "MAY": "MAY",
    "JUN": "JUNE",
    "JUL": "JULY",
    "AUG": "AUGUST",
    "SEP": "SEPTEMBER",
    "OCT": "OCTOBER",
    "NOV": "NOVEMBER",
    "DEC": "DECEMBER"
}

month = month_dict.get(month_short, 'Unknown')

print(month)