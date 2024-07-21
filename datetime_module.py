import datetime
#from datetime import datetime  # This import is redundant since datetime is already imported from the datetime module.

# Get the current date and time
current_time = datetime.datetime.now()

# Print the current date and time
print(current_time)

# Print various components of the current date and time
print(current_time.year)          # Current year
print(current_time.month)         # Current month
print(current_time.day)           # Current day
print(current_time.weekday())     # Day of the week (Monday is 0 and Sunday is 6)
print(current_time.time())        # Current time
print(current_time.hour)          # Current hour
print(current_time.minute)        # Current minute
print(current_time.second)        # Current second
print(current_time.microsecond)   # Current microsecond

# Print the time component again
print(current_time.time())

# Print the current date and time again
print(current_time.now())

# Print the current time in C time format
print(current_time.ctime())

# Print the time as a time.struct_time object
print(current_time.timetuple())

# Create a specific date (October 10, 2024)
test_date = datetime.date(2024, 10, 10)
print(test_date)              # Print the specific date
print(type(test_date))        # Print the type of the test_date object
print(test_date.year)         # Year of the specific date
print(test_date.month)        # Month of the specific date
print(test_date.day)          # Day of the specific date

# Calculate the difference in days between two current times (should be 0)
current_time = datetime.datetime.now()
future_time = datetime.datetime.now()
print((future_time - current_time).days)

# Parsing and working with time using strptime
from datetime import datetime

start_time = datetime.strptime("2:13:20", "%H:%M:%S")  # Parse start time
end_time = datetime.strptime("11:26:20", "%H:%M:%S")   # Parse end time
print(start_time)   # Print start time
print(end_time)     # Print end time

# Calculate the difference between the end and start time
get_diff = end_time - start_time
print(get_diff)     # Print the time difference

# Calculate and print the difference in seconds and minutes
seconds = get_diff.total_seconds()
print('Difference in seconds', seconds)
minutes = seconds / 60
print('Difference in minutes', minutes)

# Working with time zones using pytz
import pytz

ist = pytz.timezone('Asia/Karachi')  # Get the timezone for Karachi
print(datetime.now(ist))             # Print the current time in Karachi timezone
print(ist)                           # Print the timezone object

# Formatting date and time using strftime
from datetime import datetime

current = datetime.now()
year = current.strftime("%Y")  # Format current year
month = current.strftime("%M") # Format current month
day = current.strftime("%d")   # Format current day
print(year)
print(month)
print(day)

time = current.strftime("%H:%M:%S")  # Format current time
print(time)
date = current.strftime("%d/%m/%y")  # Format current date in dd/mm/yy
print(date)
date = current.strftime("%d-%M-%Y")  # Format current date in dd-MM-YYYY
print(date)
datetime = current.strftime("%d-%M-%Y, %H:%M:%S")  # Format current date and time
print(datetime)

# Using alias for datetime as dt
from datetime import datetime as dt

current = dt.now()  # Get the current date and time using alias
print(current)

date = current.strftime('%Y-%M-%d')  # Format current date
print(date)

# Custom date formatting using strftime
from datetime import datetime

current = datetime.now()  # Get the current date and time
print(current)
custom_date = datetime.strftime(current, "%Y-%M-%d")  # Custom date format
print(custom_date)

current = datetime.now()  # Get the current date and time again
print(current)
custom_datetime = datetime.strftime(current, "%Y-%M-%d, %I-%M-%S")  # Custom date and time format
print(custom_datetime)

# Parsing date and time using strptime
from datetime import datetime

my_date = '2023-02-02 04-52-12'  # Define a date string
print(my_date)

my_datetime = datetime.strptime(my_date, "%Y-%m-%d %H-%M-%S")  # Parse the date string into datetime object
print(my_datetime)
