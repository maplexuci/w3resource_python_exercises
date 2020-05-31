# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14



from datetime import datetime

date_time = datetime.now()

date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")

print("Current data and time : \n" + date_time)