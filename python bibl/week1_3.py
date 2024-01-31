import datetime
import math
initials = 'M.D.'
population_of_horten = '26,751'
poulation_of_earth = '7.888 billion'

# Get the current date
current_date = datetime.datetime.now()

# Turn weekday in to string
weekday_name = current_date.strftime("%A")

duration_of_course = '12 weeks'

pi = math.pi

print(f"My initials are: {initials}. The population of my hometown is {population_of_horten}");
print(f"Which contributes to the population of the earth that is {poulation_of_earth}");
print(f"The Current weekday is {weekday_name}");
print(f"The duration of the course is {duration_of_course}, which is a different value than that of Pi which is {pi}");



