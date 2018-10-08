#!/usr/bin/python2.7

import telepot
import sys

bot = telepot.Bot('token')
pic = sys.argv[1]

if pic.endswith("snapshot.jpg"):
    cap = "snapshot"
else:
    cap = "motion detected"


bot.sendPhoto(number, photo=open(pic,'rb'),caption=cap)

exit(0)