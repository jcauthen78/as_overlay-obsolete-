#!/bin/bash
#  usage: add_overlays.py [-h] [-c] [-d DTHETA] [-w] [-f WXFILE] [-bl BOTLTTXT]
#                         [-i INFILE] [-o OUTFILE]
#
#  optional arguments:
#    -h,          --help       show this help message and exit
#    -c,          --cardinals  Add Cardinals
#    -d DTHETA,   --dTheta     DTHETA
#                              Cardinals: Angle Delta in Degrees ( 0 = North, 90 =
#                              due East, 180 = South, 270 = due West )
#    -w,          --weather    Add Weather
#    -f WXFILE,   --wxfile     WXFILE
#                              Weather Daata file
#    -bl BOTLTTXT, --botleft   Bottom Left Txt Block
#    -i INFILE,   --infile     INFILE
#                              Image file to manipulate
#    -o OUTFILE,  --outfile    OUTFILE
#                              Output file
#

## Overlay with cardinals(NSEW), weather, as well as second info-block in bottom left corner
/home/pi/allsky/scripts/mods/overlay.py -w -f /home/pi/allsky/scripts/mods/log-temp.csv -bl -c -d 0 -i $1 -o $2

## Overlay with cardinals(NSEW), as well as second info-block in bottom left corner
# /home/pi/allsky/scripts/mods/overlay.py -bl -c -d 0 -i $1 -o $2
