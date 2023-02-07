import datetime
from astral import LocationInfo
from astral.sun import sun
import time

def main():
    print_log("Init log")

    city = LocationInfo("Belgrade", "Serbia", "Europe/Belgrade", 44.8125, 20.4612)
    
    time_now = datetime.datetime.now()
    astral_sun = sun(city.observer, date=time_now)

    time_sunset = astral_sun["sunset"]
    time_sunset += datetime.timedelta(hours=1, minutes=0)

    # left in case daylight saving plays a part
    #if not time.localtime().tm_isdst:
        #time_sunset += datetime.timedelta(hours=1, minutes=0)

    t1 = time_sunset - datetime.timedelta(hours=0, minutes=30)
    change_time_sunset = datetime.datetime(t1.year, t1.month, t1.day, t1.hour, t1.minute, t1.second)

    t2 = time_sunset + datetime.timedelta(hours=0, minutes=30)
    change_time_night = datetime.datetime(t2.year, t2.month, t2.day, t2.hour, t2.minute, t2.second)
    

    if time_now < change_time_sunset:
        print_log("It's day")
    elif time_now >= change_time_sunset and time_now <= change_time_night:
        print_log("It's sunset")
    else:
        print_log("It's night")

    
    print_log("end log")


##############################################################################################################################################
# Functions
##############################################################################################################################################
        
def print_log(text, end="\n", include_timestamp=True):
    if(include_timestamp):
        print("[" + datetime.datetime.now().strftime("%Y.%m.%d. %H:%M:%S") + "]", end=" ")
    print(text, end=end)





if __name__ == "__main__":
    main()