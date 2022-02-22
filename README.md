# Text overlay module for Thomas Jacquin's AllSky project

![Overlay Image](https://github.com/jcauthen78/as_overlay/blob/1567cadf570bfb3f25462e8793f0786d50d8faea/allSky_overlay.jpg)

Required install : <br>
PythonMagick - (https://www.raspberryconnect.com/raspbian-packages/55-raspbian-python)<br>
**sudo apt install python3-pythonmagick** _(unsure if sudo is required)_<br>
Used to do the core text overlays, fast and efficient. Available Font Colors list - (https://imagemagick.org/script/color.php)

Pandas - (https://pandas.pydata.org/docs/getting_started/install.html)<br>
**pip install pandas**<br>
Used to read CSV files (and probably JSON?) for live-data in overlays.<br

    
2 core files modified. The notes & additions are inside the above provided files. These are _**ADDITIONS**_ to the existing files, not full replacements. Replacing the core files with these attached files **WILL BREAK YOUR ALLSKY** <br>
**/home/pi/allsky/scripts/config/config.sh<br>
/home/pi/allsky/scripts/saveImage.sh<br>**

I made a new folder in the /home/pi/allsky/scripts , called **mods**, where the main overlay.py lives, as well as a CSV file from my temperature logger, so it can be called via the run. 
