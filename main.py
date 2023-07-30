import datetime
from astral import LocationInfo
from astral.sun import sun
import time
import ctypes
import os

app_folder = os.getenv('LOCALAPPDATA') + "\\WallpaperSwitcher"
log_file = os.path.join(app_folder, 'log.txt')
wallpapers = {'day': None, 'sunset': None, 'night': None}

def main():
    print_log("Starting wallpaper switcher...")

    if not os.path.exists(app_folder):
        os.makedirs(app_folder)

    # if the log file exists, delete it
    if os.path.exists(log_file):
        os.remove(log_file)

    # load wallpapers
    for time_of_day in wallpapers.keys():
        for ext in ['jpg', 'png']:
            wallpaper_path = f'{app_folder}\\{time_of_day}.{ext}'
            if os.path.exists(wallpaper_path):
                wallpapers[time_of_day] = wallpaper_path
                break
            
        if wallpapers[time_of_day] is None:
            print_log(f'No {time_of_day} wallpaper found. Please put a .jpg or .png image named {time_of_day} in the folder {app_folder}.', "Error")
        
    if wallpapers["day"] is None or wallpapers["sunset"] is None or wallpapers["night"] is None:
        return
    
    try_change_wallpaper()

    print_log("Exiting wallpaper switcher...")


##############################################################################################################################################
# Functions
##############################################################################################################################################
        
def print_log(text, level="info"):
    """Print a log to console and the log file.

    Paramters:
    text (string): message to print
    level (string): Either "info", "warning" or "error". Can be ommited. Defaults to "info".
    """

    valid_levels = ["info", "warning", "error"]
    if level.lower() not in valid_levels:
        level = "info"
    
    level = "[" + level.upper() + "]"
    timestamp = "[" + datetime.datetime.now().strftime("%Y.%m.%d. %H:%M:%S") + "]"
    message = timestamp + " " + level + ": " + text

    print(message, end="\n")
    with open(log_file, 'a') as file:
        file.write(message + "\n")

def try_change_wallpaper():
    print_log("Starting wallpaper update")

    city = LocationInfo("Belgrade", "Serbia", "Europe/Belgrade", 44.8125, 20.4612)
    
    time_now = datetime.datetime.now()
    astral_sun = sun(city.observer, date=time_now)

    time_sunset = astral_sun["sunset"]
    time_sunset += datetime.timedelta(hours=1, minutes=0)

    # adjust for daylight saving
    if time.localtime().tm_isdst:
        time_sunset += datetime.timedelta(hours=1, minutes=0)

    t1 = time_sunset - datetime.timedelta(hours=0, minutes=30)
    change_time_sunset = datetime.datetime(t1.year, t1.month, t1.day, t1.hour, t1.minute, t1.second)

    t2 = time_sunset + datetime.timedelta(hours=0, minutes=30)
    change_time_night = datetime.datetime(t2.year, t2.month, t2.day, t2.hour, t2.minute, t2.second)

    if time_now < change_time_sunset:
        print_log("It's day. Setting day wallpaper.")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpapers['day'], 0)

        wait_time = (change_time_sunset - time_now).total_seconds() + 5
        print_log("Wait time: " + str(wait_time))
        time.sleep(wait_time)

        try_change_wallpaper()
    elif time_now >= change_time_sunset and time_now <= change_time_night:
        print_log("It's sunset. Setting sunset wallpaper.")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpapers['sunset'], 0)

        wait_time = (change_time_night - time_now).total_seconds() + 5
        print_log("Wait time: " + str(wait_time))
        time.sleep(wait_time)

        try_change_wallpaper()
    else:
        print_log("It's night. Setting night wallpaper.")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpapers['night'], 0)



if __name__ == "__main__":
    main()