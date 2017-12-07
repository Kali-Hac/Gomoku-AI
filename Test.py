#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/12/5 11:12        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：        √ ━━━━━☆*°☆*°
"""
from graphics import *

win = GraphWin('5_chess', 480, 600)
p = [[0 for a in range(15)] for b in range(15)]
black = [[0 for a in range(15)] for b in range(15)]
white = [[0 for a in range(15)] for b in range(15)]
q = [[0 for a in range(15)] for b in range(15)]
# q 为啥是0-15，表示存疑

def Create_Board():
	global p
	for i in range(15):
		for j in range(15):
			p[i][j] = Point(i*30+30, j*30+30)
			p[i][j].draw(win)
	for r in range(15):
		Line(p[r][0], p[r][14]).draw(win)
		Line(p[0][r], p[14][r]).draw(win)
	center = Circle(p[7][7], 3)
	center.draw(win)
	center.setFill('black')

def Click(cnt):
	global p, q, black, white
	p1 = win.getMouse()
	x1 = p1.getX()
	y1 = p1.getY()
	for i in range(15):
		for j in range(15):
			sqrdis = ((x1 - p[i][j].getX()) ** 2 + (y1 - p[i][j].getY()) ** 2)
			if sqrdis <= 200 and q[i][j] == 0:
				if cnt % 2 == 0:
					black[i][j] = 1
					q[i][j] = Circle(p[i][j], 10)
					q[i][j].draw(win)
					q[i][j].setFill('black')
				else:
					white[i][j] = 1
					q[i][j] = Circle(p[i][j], 10)
					q[i][j].draw(win)
					q[i][j].setFill('white')
				cnt += 1
	return cnt

def Check():
	for i in range(15):
		for j in range(11):
			if black[i][j:j+5] == [1, 1, 1, 1, 1]:
				return 'black'
			elif white[i][j:j+5] == [1, 1, 1, 1, 1]:
				return 'white'
	for i in range(15):
		for j in range(11):
			if black[j][i] and black[j+1][i] and black[j+2][i] and black[j+3][i] and black[j+4][i]:
				return 'black'
			elif white[j][i] and white[j+1][i] and white[j+2][i] and white[j+3][i] and white[j+4][i]:
				return 'white'
	for i in range(11):
		for j in range(11):
			if black[i][j] and black[i+1][j+1] and black[i+2][j+2] and black[i+3][j+3] and black[i+4][j+4]:
				return 'black'
			elif white[i][j] and white[i+1][j+1] and white[i+2][j+2] and white[i+3][j+3] and white[i+4][j+4]:
				return 'white'
	for i in range(11):
		for j in range(14):
			if black[i][j] and black[i+1][j-1] and black[i+2][j-2] and black[i+3][j-3] and black[i+4][j-4]:
				return 'black'
			elif white[i][j] and white[i+1][j-1] and white[i+2][j-2] and white[i+3][j-3] and white[i+4][j-4]:
				return 'white'

if __name__ == '__main__':
	Create_Board()
	cnt = 0
	while 1:
		cnt = Click(cnt)
		Check()
		if Check() == 'black':
			Text(Point(240, 550), 'the black wins').draw(win)
			break
		if Check() == 'white':
			Text(Point(240, 550), 'the white wins').draw(win)
			break
	win.getMouse()