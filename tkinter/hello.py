#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter

root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

Static1 = Tkinter.Label(text=u'test', foreground='#ff0000', background='#ffaacc')
Static1.pack()

root.mainloop()
