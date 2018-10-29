import calendar

# create a text plain calender
c=calendar.TextCalendar(calendar.SUNDAY)
str=c.formatmonth(2018,7)
print(str)

#create HTML formatted calender
hc=calendar.HTMLCalendar(calendar.THURSDAY)
str=hc.formatmonth(2018,8)
print(str)
for i in hc.itermonthdays(2018,8):
    print(i)

for name in calendar.month_name: #day_name
    print(name)

# fetch the list of the specific day for a whole year
for months in range(1,13):
    mycal=calendar.monthcalendar(2018,months) # Fetches list of weeks that present in a month
    # The second monday has to be within first two weeks
    week1=mycal[0]
    week2=mycal[1]
    if week1[calendar.MONDAY]!=0:
        auditday=week1[calendar.MONDAY]
    else:
        auditday=week2[calendar.MONDAY]

    print("%10s %2d"%(calendar.month_name[months], auditday))