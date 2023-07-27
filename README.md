# WallpaperSwitcher
Automatically switch between day, sunset and night wallpaper based on sunset time. Sunset wallpaper lasts for 1 hour: 30 minutes before and 30 minutes after sunset time.

Currently, location is set like so: 
```
LocationInfo("Belgrade", "Serbia", "Europe/Belgrade", 44.8125, 20.4612)
```
which means you have to edit this line and build the exe yourself, if you are outside of Serbia.


### Setup notes
1. Use provided exe or create the exe from script using tools like auto-py-to-exe.

2. Add a Windows scheduled task for the exe and set it to run at user logon.

3. Place .jpg or .png wallpapers called "day", "sunset" and "night" in your %localappdata%/WallpaperSwitcher folder.