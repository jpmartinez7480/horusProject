#!/usr/bin/python2.7

import telepot
import sys

bot = telepot.Bot('674455085:AAF_hunYYC3rFERN8EugnLI2rYb8yi8motw:bot_token')
pic = sys.argv[1]

if pic.endswith("snapshot.jpg"):
    cap = "snapshot"
else:
    cap = "motion detected"


bot.sendPhoto(674455085, photo=open(pic,'rb'),caption=cap)

exit(0)