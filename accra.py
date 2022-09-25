# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print only the date
# part of the current date and time.
print(f"{current_date_and_time:%Y-%m-%d}")