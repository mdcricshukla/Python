import datetime

'''current_date_and_time = datetime.datetime.now()

print("Current Date and Time:", current_date_and_time)'''


import datetime

current_date_and_time = datetime.datetime.now()

# Format 1: Default string representation
print("Default format:", current_date_and_time)

# Format 2: Custom format
custom_format = current_date_and_time.strftime("%Y-%m-%d %H:%M:%S")
print("Custom format:", custom_format)

# Format 3: Date only
date_only_format = current_date_and_time.strftime("%Y-%m-%d")
print("Date only format:", date_only_format)

# Format 4: Time only
time_only_format = current_date_and_time.strftime("%H:%M:%S")
print("Time only format:", time_only_format)

# Format 5: Another custom format
another_custom_format = current_date_and_time.strftime("%A, %B %d, %Y %I:%M %p")
print("Another custom format:", another_custom_format)

