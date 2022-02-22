#!/bin/env python3
'''
A hopefully(?) understandable Python script that will aid in adding overlay
text to AllSky images created by Thomas Jacquin's AllSky software v0.8.3
(https://github.com/thomasjacquin/allsky). It should also work with earlier
and later versions.

Base idea/design from LinuxKidd (https://github.com/linuxkidd/allsky-scripts)
Additions & Modifications by AllSkyJim (https://twitter.com/allskyj)

Dependencies :
--------------
PythonMagick -sudo apt install python3-pythonmagick
    (https://www.raspberryconnect.com/raspbian-packages/55-raspbian-python).
    * Used to do the core text overlays, fast and efficient.
    * Available Font Colors list - (https://imagemagick.org/script/color.php)
Pandas - pip install pandas
    (https://pandas.pydata.org/docs/getting_started/install.html)
    * Used to read CSV files (and probably JSON?) for live-data in overlays.

'''
import argparse,json,math,os,time
import PythonMagick as Magick
import pandas as pd  # to parse through CSV log files


def addCardinals():
    c = {
        "N":calcXY(math.pi),
        "W":calcXY(math.pi/2),
        "S":calcXY(0),
        "E":calcXY(math.pi*1.5)
        }
    try:
        fontPoint=(w*0.025)                             # dynamic font size (width divide by #)
        img.fontPointsize(fontPoint)
        img.fillColor(Magick.Color('forestgreen'))      # Font Color for Cardinals
    except:
        pass
    for i in c:
        try:
            img.draw( Magick.DrawableText(c[i]['X'], c[i]['Y'], i) )
        except:
            try:
                outarr.append("text {0:0.0f},{1:0.0f} '{2:s}'".format(c[i]['X'], c[i]['Y'], i))
            except:
                pass
    return

def calcXY(angle): # (for cardinals)
    X = cX + ( R * math.sin(dTheta + angle))
    Y = cY + ( R * math.cos(dTheta + angle))
    return { "X": X, "Y": Y }

def bLt(): # All Optional
    xPos=20                                         # Over from right
    yPos=(h*0.85)                                   # Down from top
    fontPoint=(h*0.014)                             # dynamic font size (height multiply by #)
    img.fontPointsize(fontPoint)
    img.fillColor(Magick.Color('yellow'))        # Font color for Bot Lt text
    img.strokeColor(Magick.Color('slateblue'))      # Font Stroke color for Bot Lt text

    botLt_fields=[
            { "out": " Your Name"                   },
            { "out": " City, State"                 },
            { "out": " LAT & LONG"                  },
            { "out": " AllSky v0.8"                 },
            { "out": " Raspberry Pi 4b, 8gb"        },
            { "out": " ASI 178MC"                   },
            { "out": " Contact Info"                },
            { "out": " Contact Info 2 if wanted"    },
            # {},           # Spacer line incase you want more    
            ]

    for field in botLt_fields:
        try:
            img.draw( Magick.DrawableText(xPos,yPos, field['out']))
        except:
            try:
              img.draw( Magick.DrawableText(xPos,yPos, field['out']))
            except:
                pass
        yPos+=fontPoint*1.3333

def wx(): # Bottom Right Weather
    xPos=(w*0.83)                                           # Over from right, in width percent
    yPos=(h*0.89)                                           # Down from top, in height percent
    fontPoint=(h*0.014)                                     # Font size, in height percent
    img.fontPointsize(fontPoint)
    img.fillColor(Magick.Color('LightSteelBlue1'))          # Font color for weather text
    img.strokeColor(Magick.Color('SlateGray4'))             # Font Stroke color for weather text

    # grabbing data from CSV file - https://bit.ly/3AvRTBA
    intTemp =  wxfile["intTempF"].values[-1] #temperature
    intHum = wxfile["intHum"].values[-1] #humidity
    dewP = wxfile["dewpoint"].values[-1] #dewpoint
    cpuTemp = wxfile["cpuTempF"].values[-1] #CPU temp

    wxfields=[
            { "out": "AllSky Internal Readings"                            },
            { "out": "------------------------"                            },
            { "out": " Case Temp: {0: .2f} °F".format(intTemp)             },
            { "out": " CPU Temp: {0: .2f} °F".format(cpuTemp)              },
            { "out": " DewPt: {0: .2f} °F".format(dewP)                    },
            { "out": " Hum: {0: .2f}%".format(intHum)                      },
            #{ },                                                               # Spacer line if wanted
            # { "out": " More Stuff: {0: 5.1f} mph.format(wind)"           },
            #             Text    {string formatting}.format(value)
            ]

    for field in wxfields:
        try:
            img.draw( Magick.DrawableText(xPos,yPos, field['out']))

        except:
            try:
                outarr.append("text {0:0.0f},{1:0.0f} '{2:s}'".format(xPos,yPos,field['out'].format(wxdata[field['value']])))
            except:
                pass
        yPos+=fontPoint*1.3333

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cardinals", action = 'store_true',   help="Add Cardinals")
    parser.add_argument("-d", "--dTheta",    default = 0,   type=int, help="Cardinals: Angle Delta in Degrees ( 0 = North, 90 = due East, 180 = South, 270 = due West )")

    parser.add_argument("-w", "--weather",   action = 'store_true',  help="Add Weather")
    parser.add_argument("-f", "--wxfile",    default = '',           help="Weather JSON file")

    parser.add_argument("-i", "--infile",    default = '',           help="Image file to manipulate")
    parser.add_argument("-o", "--outfile",   default = '',           help="Output file")

    parser.add_argument("-bl", "--botleft", action = 'store_true',   help="Bottom Left Text Block")

    args = parser.parse_args()

    cardinals  = args.cardinals
    dTheta     = (args.dTheta * 2 * math.pi)/360

    weather    = args.weather
    wxfile     = pd.read_csv(args.wxfile)

    infile     = args.infile
    outfile    = args.outfile

    botLt      = args.botleft

    outarr = []
    myFont="/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf"

    if infile!="" and outfile!="":
        if os.path.isfile(infile):
            img = Magick.Image(infile)
            w,h = img.size().width(), img.size().height()   # dynamic Cardinal centering
            cX = w/2                                        # dynamic Cardinal centering
            cY = h/2                                        # dynamic Cardinal centering
            R = h/2.1

    if weather:
        wx()
    if cardinals:
        addCardinals()
    if botLt:
        bLt()

    try:
        img.write(outfile)
    except:
        print(" ".join(outarr))
