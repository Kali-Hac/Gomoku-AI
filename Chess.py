#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/12/5 11:12        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction： 五子棋主运行程序   √ ━━━━━☆*°☆*°
"""
from graphics import *
import Global_variables
import Alpha_beta_optimize
import Calcu_every_step_score
p = [[0 for a in range(15)] for b in range(15)]
q = [[0 for a in range(15)] for b in range(15)]
win = ''
def Create_Board():
	global win
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

def human_vs_machine(cnt, mod):
	global win
	if cnt % 2 == 0:
		human_flag = False
		while not human_flag:
			p1 = win.getMouse()
			x1 = p1.getX()
			y1 = p1.getY()
			for i in range(15):
				for j in range(15):
					sqrdis = ((x1 - p[i][j].getX()) ** 2 + (y1 - p[i][j].getY()) ** 2)
					if sqrdis <= 200 and Global_variables.flag[i][j] == 0:
						Global_variables.black[i][j] = 1
						# print Calcu_every_step_score.cal_score_wise('black', i, j)
						q[i][j] = Circle(p[i][j], 10)
						q[i][j].draw(win)
						q[i][j].setFill('black')
						human_flag = True
						break
				if human_flag:
					break
	else:
		machine_pos = Alpha_beta_optimize.alpha_beta_process(mod)
		if not machine_pos:
			Text(Point(240, 500), '机器对战已结束...').draw(win)
			return -1
		i = machine_pos[0]
		j = machine_pos[1]
		Global_variables.white[i][j] = 1
		# cal_score('white', i, j)
		q[i][j] = Circle(p[i][j], 10)
		q[i][j].draw(win)
		q[i][j].setFill('white')
	cnt += 1
	# 测试图显示bug修复
	Global_variables.flag[i][j] = 1
	return cnt

def machine_vs_machine(cnt, mod):
	global win
	if cnt % 2 == 0:
		machine_pos = Alpha_beta_optimize.alpha_beta_process(mod)
		if not machine_pos:
			Text(Point(240, 500), '机器对战已结束...').draw(win)
			return -1
		i = machine_pos[0]
		j = machine_pos[1]
		Global_variables.black[i][j] = 1
		# cal_score('white', i, j)
		q[i][j] = Circle(p[i][j], 10)
		q[i][j].draw(win)
		q[i][j].setFill('black')
	else:
		machine_pos = Alpha_beta_optimize.alpha_beta_process(mod)
		if not machine_pos:
			Text(Point(240, 500), '机器对战已结束...').draw(win)
			return -1
		i = machine_pos[0]
		j = machine_pos[1]
		Global_variables.white[i][j] = 1
		# cal_score('white', i, j)
		q[i][j] = Circle(p[i][j], 10)
		q[i][j].draw(win)
		q[i][j].setFill('white')
	cnt += 1
	# 测试图显示bug修复
	Global_variables.flag[i][j] = 1
	return cnt

def human_with_machine_vs_machine(cnt, mod):
	global win
	if cnt % 2 == 0:
		human_flag = False
		machine_pos = Alpha_beta_optimize.alpha_beta_process(mod)
		ii = machine_pos[0]
		jj = machine_pos[1]
		q[ii][jj] = Circle(p[ii][jj], 3)
		q[ii][jj].draw(win)
		q[ii][jj].setFill('black')
		Text(Point(240, 550), 'The black point is the current suggestion of the system...').draw(win)
		Text(Point(240, 570), 'The white point is the previous suggestion of the system...').draw(win)
		if not machine_pos:
			Text(Point(240, 500), '对战已结束...').draw(win)
			return -1
		while not human_flag:
			p1 = win.getMouse()
			x1 = p1.getX()
			y1 = p1.getY()
			for i in range(15):
				for j in range(15):
					sqrdis = ((x1 - p[i][j].getX()) ** 2 + (y1 - p[i][j].getY()) ** 2)
					if sqrdis <= 200 and Global_variables.flag[i][j] == 0:
						q[ii][jj].setFill('white')
						Global_variables.black[i][j] = 1
						q[i][j] = Circle(p[i][j], 10)
						q[i][j].draw(win)
						q[i][j].setFill('black')
						human_flag = True
						break
				if human_flag:
					break
	else:
		machine_pos = Alpha_beta_optimize.alpha_beta_process(mod)
		if not machine_pos:
			Text(Point(240, 500), '对战已结束...').draw(win)
			return -1
		i = machine_pos[0]
		j = machine_pos[1]
		Global_variables.white[i][j] = 1
		# cal_score('white', i, j)
		q[i][j] = Circle(p[i][j], 10)
		q[i][j].draw(win)
		q[i][j].setFill('white')
	cnt += 1
	# 测试图显示bug修复
	Global_variables.flag[i][j] = 1
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

def Run_chess(mod, option):
	global win
	win = GraphWin(mod + option, 480, 600)
	Create_Board()
	cnt = 0
	Global_variables.white[7][7] = 1
	# cal_score('white', i, j)
	q[7][7] = Circle(p[7][7], 10)
	q[7][7].draw(win)
	q[7][7].setFill('white')
	Global_variables.flag[7][7] = 1
	while 1:
		if option == 'MM':
			cnt = machine_vs_machine(cnt, mod)
		elif option == 'HM':
			cnt = human_vs_machine(cnt, mod)
		elif option == 'HMM':
			cnt = human_with_machine_vs_machine(cnt, mod)
		# 测试用
		# if cnt == 2:
		# 	alpha_beta_process('black', 7, -1000000, 1000000)
		Check()
		if cnt == -1:
			break
		if Check() == 'black':
			Text(Point(240, 500), 'Black wins').draw(win)
			break
		if Check() == 'white':
			Text(Point(240, 500), 'White wins').draw(win)
			break
	win.getMouse()

# if __name__ == '__main__':
# 	top = Tk()
# 	top.title("五子棋")
# 	def callback():
# 		global thread_num
# 		if thread_num >= 5:
# 			print '最多创建5个窗口！'
# 		else:
# 			thread_num += 1
# 			thread.start_new_thread(Run_chess)
# 	b = Button(top, text="外观装饰边界附近的标签", width=19, bg="red", relief="raised").pack()
#
# 	Button(top, text="设置按钮状态", width=21, state="disable", command=callback).pack()
#
# 	Button(top, text="设置bitmap放到按钮左边位置", compound="left", bitmap='info').pack()
#
# 	c = Button(top, text="设置command事件调用命令", fg="blue", bd=2, width=28, command=callback)
# 	c.pack()
# 	Button(top, text="设置高度宽度以及文字显示位置", anchor='sw', width=30, height=2).pack()
#
# 	tk.mainloop()
