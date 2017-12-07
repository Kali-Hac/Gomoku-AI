#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/12/6 17:13        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：        √ ━━━━━☆*°☆*°
"""

import Calcu_every_step_score
import Global_variables
import copy

# used for testing
test = [[0 for i in range(15)] for j in range(15)]
a = [[0 for i in range(15)] for j in range(15)]
b = [[0 for i in range(15)] for j in range(15)]
best_b_sums = -1
best_w_sums = -1
best_b = []
best_w = []
black_used_pos = []
white_used_pos = []
max_b_score = -1000
max_w_score = -1000
best_b_pos = []
best_w_pos = []
best_pos = []
search_range = []
origin_color = ''
test_pos = []
def alpha_beta_process(mod):
	global search_range, best_pos
	search_range = shrink_range()
	# print alpha_beta(color, depth, alpha, beta)
	best_pos = machine_thinking(mod)
	return best_pos

def alpha_beta(color, depth, alpha, beta):
	global test_pos, origin_color, rblack_used_pos, white_used_pos, max_score, best_pos, black_used_pos, white_used_pos, search_range, max_b_score, max_w_score, best_b_pos, best_w_pos
	if origin_color == '':
		origin_color = color
	if depth <= 0:
		if color == 'black':
			ii = black_used_pos[-1][0]
			jj = black_used_pos[-1][1]
			score = Calcu_every_step_score.cal_score('black', ii, jj)
			# max_scores = -5
			# for i in range(15):
			# 	for j in range(15):
			# 		if Global_variables.black[i][j] == 1:
			# 			score = Calcu_every_step_score.cal_score('black', i, j)
			# 			if score > max_scores:
			# 				max_scores = score
				# print 'score：' + str(score)
				# if score > max_b_score:
				# 	max_b_score = score
					# bug 修复
					# best_b_pos = (ii, jj)
					# print best_b_pos
			# return max_b_score
		else:
			ii = white_used_pos[-1][0]
			jj = white_used_pos[-1][1]
			score = Calcu_every_step_score.cal_score('white', ii, jj)
			# max_scores = -5
			# for i in range(15):
			# 	for j in range(15):
			# 		if Global_variables.white[i][j] == 1:
			# 			score = Calcu_every_step_score.cal_score('white', i, j)
			# 			if score > max_scores:
			# 				max_scores = score
		# print 'score：' + str(score)
		return score
				# print 'score：' + str(score)
				# if score > max_w_score:
				# 	max_w_score = score
				# 	best_w_pos = (ii, jj)
					# print best_w_pos
			# return max_w_score
		# return cal_score(color, i, j)
	for i in range(15):
		for j in range(15):
			# print i,j
			# for k in search_range:
			# 	print k
			# for k in flag:
			# 	print k
			if Global_variables.flag[i][j] == 0 and search_range[i][j] == 1:
				Global_variables.flag[i][j] = 1
				# print i,j
				search_range[i][j] = 0
				if color == 'black':
					# 修复bug * 4 => long time
					Global_variables.black[i][j] = 1
					black_used_pos.append((i, j))
				else:
					Global_variables.white[i][j] = 1
					white_used_pos.append((i, j))
				if color == 'black':
					new_color = 'white'
				else:
					new_color = 'black'
				val = - alpha_beta(new_color, depth-1, -beta, - alpha)
				Global_variables.flag[i][j] = 0
				search_range[i][j] = 1
				if color == 'black':
					black_used_pos.remove((i, j))
					Global_variables.black[i][j] = 0
				else:
					white_used_pos.remove((i, j))
					Global_variables.white[i][j] = 0
				if val >= beta:
					# print 'beta:' + str(beta)
					return beta
				if val > alpha:
					# print alpha
					# 修复bug =》 fatal 233
					if color == origin_color and depth == 4:
						# print origin_color
						# print val
						# print best_pos
						best_pos = (i, j)
					alpha = val
	return alpha

# 测试用
def alpha_beta_test(color, depth, alpha, beta):
	global a, b, test, best, best_b_sums, best_w_sums, best_b, best_w
	if depth <= 0:
		sums = 0
		for i in range(15):
			for j in range(15):
				if color == 'black':
					if a[i][j] == 1:
						sums += Global_variables.board_scores[i][j]
				else:
					if b[i][j] == 1:
						sums += Global_variables.board_scores[i][j]
		if color == 'black':
			if sums > best_b_sums:
				best_b_sums = sums
				best_b = copy.deepcopy(a)
		else:
			if sums > best_w_sums:
				best_w_sums = sums
				best_w = copy.deepcopy(b)
		return sums
		# return cal_score(color, i, j)
	for i in range(15):
		for j in range(15):
			if test[i][j] == 0:
				test[i][j] = 1
				if color == 'black' and not a[i][j] == 1:
					a[i][j] = 1
				else:
					b[i][j] = 1
				if color == 'white' and not b[i][j] == 1:
					new_color = 'black'
				else:
					new_color = 'white'
				val = - alpha_beta_test(new_color, depth-1, -beta, - alpha)
				test[i][j] = 0
				if color == 'black':
					a[i][j] = 0
				else:
					b[i][j] = 0
				if val >= beta:
					return beta
				if val > alpha:
					alpha = val
					# print color, alpha
	# r = 0
	# for i in range(15):
	# 	for j in range(15):
	# 		if a[i][j] == 1:
	# 			r += board_scores[i][j]
	# print 'Result：' + str(r)
	return alpha

# 替代alpha-beta的剪枝操作，直接找'半径'为1的闭包
def shrink_range():
	cover_range = [[0 for i in range(15)] for j in range(15)]
	for i in range(15):
		for j in range(15):
			if Global_variables.flag[i][j] == 1:
				for k in range(3):
					# bug修复
					cover_range[max(0, i - 1)][min(14, j - 1 + k)] = 1
					cover_range[max(0, i)][min(14, j - 1 + k)] = 1
					cover_range[min(14, i + 1)][min(14, j - 1 + k)] = 1
	cnt = 0
	for i in range(15):
		for j in range(15):
			if Global_variables.flag[i][j] == 1:
				cover_range[i][j] = 0
			if cover_range[i][j] == 1:
				cnt += 1
	# print 'cover_range_size：%d' % cnt
	return cover_range

# if __name__ == '__main__':
# 	# alpha_beta_test('black', 6, -1000000, 1000000)
# 	# for i in best_b:
# 	# 	print i
# 	# for j in best_w:
# 	# 	print j
# 	search_range = shrink_range()
# 	print alpha_beta('black', 3, -1000000, 1000000)


# 比alpha-beta效果好太多，2017-12-7 11:16 用贪心思想再权衡各参数
def machine_thinking(mod):
	global search_range
	black_max_score = -5
	white_max_score = -5
	w_best_pos = ''
	b_best_pos = ''
	for i in range(15):
		for j in range(15):
			if Global_variables.flag[i][j] == 0 and search_range[i][j] == 1:
				Global_variables.flag[i][j] = 1
				search_range[i][j] = 0
				Global_variables.white[i][j] = 1
				if mod == '初级':
					white_score = Calcu_every_step_score.cal_score_wise('white', i, j)
				elif mod == '中级':
					white_score = Calcu_every_step_score.cal_score('white', i, j)
				else:
					pass
				Global_variables.white[i][j] = 0
				Global_variables.black[i][j] = 1
				if mod == '初级':
					black_score = Calcu_every_step_score.cal_score_wise('black', i, j)
				elif mod == '中级':
					black_score = Calcu_every_step_score.cal_score('black', i, j)
				else:
					pass
				Global_variables.black[i][j] = 0
				Global_variables.flag[i][j] = 0
				if black_score > black_max_score:
					black_max_score = black_score
					b_best_pos = (i, j)
					# print black_max_score
					# print b_best_pos
				if white_score > white_max_score:
					white_max_score = white_score
					w_best_pos = (i, j)
					# print white_max_score
					# print w_best_pos
	if white_max_score > black_max_score:
		return w_best_pos
	else:
		return b_best_pos
