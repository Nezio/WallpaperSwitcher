import datetime
from astral import LocationInfo
from astral.sun import sun
import time
import ctypes

# wallpaper paths (format e.g.: "D:\\My documents\\4 Pictures\\Wallpapers\\Other\\Hogwarts artwork 1 - day.png")
wallpaper_day = "D:\\My documents\\4 Pictures\\Wallpapers\\Other\\Hogwarts artwork 1 - day.png"
wallpaper_sunset = "D:\\My documents\\4 Pictures\\Wallpapers\\Other\\Hogwarts artwork 2 - sunset.png"
wallpaper_night = "D:\\My documents\\4 Pictures\\Wallpapers\\Other\\Hogwarts artwork 3 - night.png"

def main():
    
    try_change_wallpaper()


##############################################################################################################################################
# Functions
##############################################################################################################################################
        
def print_log(text, end="\n", include_timestamp=True):
    if(include_timestamp):
        print("[" + datetime.datetime.now().strftime("%Y.%m.%d. %H:%M:%S") + "]", end=" ")
    print(text, end=end)

def try_change_wallpaper():
    print_log("Starting wallpaper switcher")

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

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_day, 0)

        wait_time = (change_time_sunset - time_now).total_seconds() + 5
        print_log("Wait time: " + str(wait_time))
        time.sleep(wait_time)

        try_change_wallpaper()
    elif time_now >= change_time_sunset and time_now <= change_time_night:
        print_log("It's sunset")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_sunset, 0)

        wait_time = (change_time_night - time_now).total_seconds() + 5
        print_log("Wait time: " + str(wait_time))
        time.sleep(wait_time)

        try_change_wallpaper()
    else:
        print_log("It's night")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_night, 0)

    
    print_log("Exiting wallpaper switcher")



if __name__ == "__main__":
    main()