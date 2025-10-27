from datetime import date
from datetime import datetime

print(date(1981,1,1).ctime())
print(date(1981,1,1).isoformat())

birthday = datetime.strptime("2007-4-6", "%Y-%m-%d")
if birthday <= datetime.today().replace(year=datetime.today().year-18):
    print('Birthday valid.')
else:
    print('Invalid Birthday.')

# ----------------
    
import date
import time
import calendar
import datetime

def Time01():
    t = time.time()
    print(t)
    print(time.localtime(t))
    print(time.struct_time.tm_year)
    print(time.asctime(time.localtime(time.time())))
    print(time.altzone)

def Calendar01():
    c = calendar.month(1981,11)
    print(c)

def Imprimirdata():
    print(datetime.date(1981,11,12))

Time01()
Calendar01()
Imprimirdata()

# ----------------

def f7():
    import time
    ticks = time.time()
    print(ticks)

    localtime = time.localtime(time.time())
    print(localtime)
    print('%d/%d/%d' %(localtime.tm_mday,localtime.tm_mon,localtime.tm_year))

    asctime = time.asctime(time.localtime(time.time()))
    print(asctime)

    import calendar

    cal = calendar.month(1981, 1)
    print(cal)

    pass

# ----------------

def ftime():
    import time; 

    print('Aguardando...')
    time.sleep(2)

    print(time.localtime())
    print("%d:%d:%d" %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))

    import calendar
    cal = calendar.month(1981, 11, 12)
    print(cal)

    # print(time.clock())

    t = (2015, 12, 31, 10, 39, 45, 1, 48, 0)
    t = time.mktime(t)
    print (time.strftime("%b %d %Y %H:%M:%S", time.localtime(t)))

    struct_time = time.strptime("30 12 2015", "%d %m %Y")
    print ("tuple : ", struct_time)

    print(time.timezone)
    print(time.tzname)

    return

# -----------------------------

import datetime

print(datetime.date(1981,11,12))
print(datetime.datetime.now())
print(datetime.datetime.now().month)
print(datetime.time(12,30,00,00))

today = datetime.datetime.now()
print(today.strftime("%d/%m/%Y - %H:%M:%S"))

import time
print(today.strftime("%m/%d/%Y - %H:%M:%S"))

import datetime

birthdays = [
    datetime.datetime(2009, 2, 14),
    datetime.datetime(2006, 11, 20),
    datetime.datetime(2005, 4, 9),
    datetime.datetime(2007, 12, 3),
    datetime.datetime(2008, 8, 17),
    datetime.datetime(2006, 1, 28),
    datetime.datetime(2009, 6, 5),
    datetime.datetime(2007, 9, 22),
    datetime.datetime(2008, 5, 1),
    datetime.datetime(2005, 7, 11),
]

for b in birthdays:
    min_birthday = datetime.datetime.now().replace(year=today.year - 18).date()
    if b.date() <= min_birthday:
        print("permitido!")
    else:
        print("nao_permitido!")

my_date = datetime.datetime(2021,12,31,0,0,1)
current_time = datetime.datetime.now()
if  current_time <= my_date:
    print('valido!')
else:
    print("vencido!")


from datetime import date
print(date.today())

from datetime import datetime
print(datetime.today()) # nao considera fuso_horario

print(datetime.now()) # considera fuso_horario

from datetime import timezone
print(datetime.now(timezone.utc))
# print(datetime.now(timezone.tzname()))
# print(datetime.today(timezone.utc))

today = date.today()
print(f"{today.day}/{today.month}/{today.year}")

today_datetime = datetime.today()
print(f"{today_datetime.day}/{today_datetime.month}/{today_datetime.year} - {today_datetime.hour}:{today_datetime.minute}:{today_datetime.second}")

print(today.strftime("%d/%m/%Y"))

birthday = date.fromisoformat("1981-11-12") # "string" para objeto
print(birthday.month)
print(birthday.isocalendar())

print(birthday.strftime("%A %d %m %B %dth %Z %y")) # olhar as formas de formatar!

import datetime

birthday_datetime = datetime.datetime(1981,11,12,10,30,00)

from zoneinfo import ZoneInfo

print(birthday_datetime.now(ZoneInfo("UTC")))

print(birthday_datetime.now(ZoneInfo("America/Sao_Paulo")))
print(birthday_datetime.isoformat())

my_time = datetime.time(12,40,35)
print(my_time)
my_time = datetime.time.fromisoformat("12:30:45-03:00")
print(my_time.strftime("%H:%M:%S"))
print(f"{my_time.hour}:{my_time.minute}:{my_time.second}")

from datetime import date, time, datetime
from zoneinfo import ZoneInfo
my_date = date(1981,11,12)
my_time = time(10,30,00)
my_tzinfo = ZoneInfo("America/Sao_Paulo")
combination = datetime.combine(my_date, my_time, my_tzinfo)
print(combination)