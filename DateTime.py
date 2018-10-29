# Python DateTime, TimeDelta, Strftime(Format) with Examples

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    today=date.today();
    print("Today date is ",today)
    today=datetime.now()
    t = datetime.time(datetime.now())
    print("The current date and time is ",today,t)
    wd=date.weekday(today)
    days=["Mon","Tue","Wed","THu","Fri","Sat","Sun"]
    print("Today is day number %d"%wd)
    print("Which is "+days[wd])

today=date.today()
print("Date Componets ",today.day,today.month,today.year,today.weekday())

if __name__ == '__main__':
 main()
# Date formatting
now=datetime.now()
print(now.strftime("%Y") +"&" + now.strftime("%y"))
print(now.strftime("%a,%d %B,%Y"))# %Y/y - year , %a,A-Weekday,%b/B-month, %d-day of month
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

#Time Formating

#%I,H - 12/24 hrs ,%M - mints , %S- seconds,%p-local's PM?/AM
print(now.strftime("%I:%M:%S %p"))
print(now.strftime("%H:%M"))

#basic timedelta and print it

print(timedelta(days=365,hours=8,minutes=15,seconds=10))
print("Today is "+str(datetime.now()))
print("One year from today it will be "+str(datetime.now()+timedelta(days=365)))
print("in one week and 4 days it will be "+str(datetime.now()+timedelta(weeks=1,days=4)))

today=date.today()
nyd=date(today.year,1,1)
if nyd < today:
    print("New year day is already went by %d days ago" %(today-nyd).days)
