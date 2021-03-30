from tkinter import *
from PIL import Image,ImageTk
root= Tk()

root.geometry("444x384")
root.title("My GUI thats second one")
# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback singer and television personality. In a film career spanning \nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film \nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian \ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian \ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was \nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''',
    bg ="red", fg="yellow", padx=13, pady=94, font="comicsansms 9 bold", borderwidth=15, relief=RIDGE)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(anchor="ne",side=TOP)


root.mainloop()
