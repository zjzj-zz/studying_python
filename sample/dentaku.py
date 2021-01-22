#!/usr/bin/env python
# coding: utf-8

import Tkinter as tk

BUTTONS = [
	['7', '8', '9', '/'],
	['4', '5', '6', '*'],
	['1', '2', '3', '-'],
	['0', '.', '=', '+']
]

def make_click(ch):
	def click(e):
		print(ch)
		if ch == '=': calc(0); return
		else: disp.insert(tk.END, ch)
	return click

def calc(e):
	label["text"] = '= ' + str(eval(disp.get()))

win = tk.Tk()
win.title("自作の電卓")
win.geometry("400x400")

disp = tk.Entry(win, font=('', 20), justify="center")
disp.pack(fill='x')
disp.bind('<Return>', calc)
label = tk.Label(win, font=('', 20), anchor="center")
label.pack(fill='x')

fr = tk.Frame(win)
fr.pack()
for y, cols in enumerate(BUTTONS):
	for x, n in enumerate(cols):
		btn = tk.Button(fr, text=n,
			font=('', 20), width=6, height=3)
		btn.grid(row=y+1, column=x+1)
		btn.bind('<1>', make_click(n))

win.mainloop()
