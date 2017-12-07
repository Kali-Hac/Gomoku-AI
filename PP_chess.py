#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/12/5 11:12        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction： 人人对战模式 √ ━━━━━☆*°☆*°
"""
from graphics import *
import Global_variables

win = ''
p = [[0 for a in range(15)] for b in range(15)]
q = [[0 for a in range(15)] for b in range(15)]

def Create_Board():
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
	human_flag = False
	while not human_flag:
		p1 = win.getMouse()
		x1 = p1.getX()
		y1 = p1.getY()
		for i in range(15):
			for j in range(15):
				sqrdis = ((x1 - p[i][j].getX()) ** 2 + (y1 - p[i][j].getY()) ** 2)
				if sqrdis <= 200 and Global_variables.flag[i][j] == 0:
					if cnt % 2 == 0:
						Global_variables.black[i][j] = 1
						q[i][j] = Circle(p[i][j], 10)
						q[i][j].draw(win)
						q[i][j].setFill('black')
						human_flag = True
					else:
						Global_variables.white[i][j] = 1
						q[i][j] = Circle(p[i][j], 10)
						q[i][j].draw(win)
						q[i][j].setFill('white')
						human_flag = True
					cnt += 1
					Global_variables.flag[i][j] = 1
					# print i, j
					break
				# if flag[i][j] == 1:
				# 	print flag[i][j]
	return cnt


def Check():
	for i in range(15):
		for j in range(11):
			if Global_variables.black[i][j:j+5] == [1, 1, 1, 1, 1]:
				return 'black'
			elif Global_variables.white[i][j:j+5] == [1, 1, 1, 1, 1]:
				return 'white'
	for i in range(15):
		for j in range(11):
			if Global_variables.black[j][i] and Global_variables.black[j+1][i] and Global_variables.black[j+2][i] and Global_variables.black[j+3][i] and Global_variables.black[j+4][i]:
				return 'black'
			elif Global_variables.white[j][i] and Global_variables.white[j+1][i] and Global_variables.white[j+2][i] and Global_variables.white[j+3][i] and Global_variables.white[j+4][i]:
				return 'white'
	for i in range(11):
		for j in range(11):
			if Global_variables.black[i][j] and Global_variables.black[i+1][j+1] and Global_variables.black[i+2][j+2] and Global_variables.black[i+3][j+3] and Global_variables.black[i+4][j+4]:
				return 'black'
			elif Global_variables.white[i][j] and Global_variables.white[i+1][j+1] and Global_variables.white[i+2][j+2] and Global_variables.white[i+3][j+3] and Global_variables.white[i+4][j+4]:
				return 'white'
	for i in range(11):
		for j in range(14):
			if Global_variables.black[i][j] and Global_variables.black[i+1][j-1] and Global_variables.black[i+2][j-2] and Global_variables.black[i+3][j-3] and Global_variables.black[i+4][j-4]:
				return 'black'
			elif Global_variables.white[i][j] and Global_variables.white[i+1][j-1] and Global_variables.white[i+2][j-2] and Global_variables.white[i+3][j-3] and Global_variables.white[i+4][j-4]:
				return 'white'


def pp_main(mod, option):
	global win
	win = GraphWin(mod, 480, 600)
	Create_Board()
	cnt = 0
	while 1:
		cnt = Click(cnt)
		Check()
		if Check() == 'black':
			Text(Point(240, 500), 'Black wins').draw(win)
			break
		if Check() == 'white':
			Text(Point(240, 500), 'White wins').draw(win)
			break
	win.getMouse()
