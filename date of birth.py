from datetime import date
import calendar
age = int(input(' Age: ')) # age of the person
year = int(input(' Current year: '))
dob = int(input('date of birth(1-31): ')) # date of birth
month = int(input('month(1-12): '))
current_date = 18,5
if dob >18  and month > 5:
    b = year - age - 1# calculates the year as long as the month is after the current month
else:
    b = year - age # calculates the date if the date and or month of birth have not yet reached
birthday = date(b,month,dob)
print(birthday.strftime('I was born on %d %A %b %Y'))
print('END')
