# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


exam_st_date = (11, 12, 2014)

exam_st_date = list(exam_st_date)

exam_st_date = [str(i) for i in exam_st_date]

schedule = ' / '.join(exam_st_date)
print('The examination will start from: ' + schedule)
