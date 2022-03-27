"""
есть 2 решения. по одинкаковому эффективные
одно от Nick White. второе от Влад Екушев

начну с решения от Nick White
алгоритм очень простой - проходимся по
всем элементам массива только один раз
и каждую итерацию нам нужно находить
минимальное значение (min_value)
и нужно высчитывать профит (profit) =
текущее значение в массиве - min_value
и потом этот profit сравнивать с max_profit
и если он больше, то это наш новый max_profit
а в самом конце после цикла наш ответ будет
лежать в переменной max_profit
"""

def find_max_profit(prices):
	min_value = 99999999
	max_profit = 0

	for i in range(0, len(prices)):
		# 1
		min_value = min(min_value, prices[i])

		# 2
		cur_profit = prices[i] - min_value
		max_profit = max(max_profit, cur_profit)

	return max_profit

"""
теперь решение от Влада

суть в том что у нас есть два поинтера
и каждую итерацию мы находим текущий профит (profit)
после этого проверяем положительный или отрицательный профит
- если профит положительный (значит акция выросла)
в этом случае мы проверяем является ли текущий максимум
прям самым максимальным за все время и если да
то задаем cur_profit как новый max_profit
- если профит отрицательный (значит цена акции упала)
в этом случае мы ставим left_pointer на right_pointer
то есть двигаемся дальше так как profit отприцательный
"""

def find_max_profit(prices):
	left_pointer = 0
	right_pointer = 1
	max_profit = 0

	while right_pointer != len(prices):
		cur_profit = prices[right_pointer] - prices[left_pointer]

		if cur_profit > 0:
			max_profit = max(max_profit, cur_profit)
		else:
			left_pointer = right_pointer

		right_pointer += 1

	return max_profit

	