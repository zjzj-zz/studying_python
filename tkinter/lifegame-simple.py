from random import randint
from tkinter import *

COLS, ROWS = [30, 20]
CW = 20
data = []
for y in range(0, ROWS):
	data.append([(randint(0, 9) == 0) for x in range(0, COLS)])

def check(x, y):
	cnt = 0
	tbl = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
	for t in tbl:
		xx, yy = [x + t[0], y + t[1]]
		if 0 <= xx < COLS and 0 <= yy < ROWS:
			if data[yy][xx]: cnt += 1

	if cnt == 3: return True
	if data[y][x]:
		if 2 <= cnt <= 3: return True
		return False
	return data[y][x]

def next_turn():
	global data
	data2 = []
	for y in range(0, ROWS):
		data2.append([check(x, y) for x in range(0, COLS)])
	data = data2

win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

def draw_stage():
	cv.delete('all')
	for y in range(0, ROWS):
		for x in range(0, COLS):
			if not data[y][x]: continue
			x1, y1 = [x * CW, y * CW]
			cv.create_oval(x1, y1, x1 + CW, y1 + CW, fill="red", width=0)

def game_loop():
	next_turn()
	draw_stage()
	win.after(300, game_loop)

game_loop()
win.mainloop()
