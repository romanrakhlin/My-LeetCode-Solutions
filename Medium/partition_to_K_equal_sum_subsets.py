"""
Эта задача решается используя Backtracking 
(то есть брутфорс который рекурсивно проходит все варианты и если что-то идет не так, откатывается обратно). 
Решение использующее этот подход самое понятное, но по времени такое средненькое. 
Но оно помогает разобраться в задаче чтобы потом оптимизировать решение для Dynamic Programming, с более хорошей Time Complexity.

Первым делом на начинаем проверять Best Cases когда можно сразу вернуть ответ за O(1). 
Ну и создаем переменные target_sum - сумма одной части которую нам нужно получить для всех трех частей. 
Еще создаем переменную visited - которая имеет столько элементов сколько заданные массив с False внутри, 
для того чтобы рекурсивно проходясь находить шаги которые уже невозможны и мы смогли бы их помечать как уже пройденные.
Еще нам сильно облегчит алгоритм то что мы отсортируем числа в убывающем порядке.

Ну и потом идет сам алгоритм рекурсивного прохода, это Depth First Search, 
знаю, тупо юзать такое для массивов, ну а что, рекурсивный алгоритм, который изначально идет в depth. 
Плюс его Time Complexity подходящее. 
А именно O(N**M), где M это количество ркурсивных вызовов, а N это основные итерации.

COMPLEXITY ANALISYS:
Сначала идет поиск суммы и длинны - 2O(n), 
После этого сортировка O(n logn). 
И наконец алгоритм DFS - O(k^n). 
Отбрасывая все незнакомое, остается O(k^n). 
Где k - количество частей, n - количество сувениров. 
А так как в нашем случае k = 3, то сложность получается O(3^n).
"""

def backtracking(nums, k):
	if k == 1 or k == 0:
		return True
	
	total_sum = sum(nums)
	n = len(nums)
	
	if n < k or total_sum % k != 0:
		return False

	nums.sort(reverse = True)
	target_sum = total_sum // k
	
	if nums[0] > target_sum:
		return False
		
	visited = [False] * n
	
	def dfs(cur_sum, begin, parts_left):
		if parts_left == 0:
			return True

		if cur_sum > target_sum:
			return False
		elif cur_sum == target_sum:
			return dfs(0, 0, parts_left - 1)

		for i in range(begin, n):
			if visited[i] == False:
				visited[i] = True

				if dfs(cur_sum + nums[i], i + 1, parts_left) == True:
					return True

				visited[i] = False

		return False # did the traversal and still cur_sum < target_sum
		
	return dfs(0, 0, k)

assert backtracking([3, 3, 3, 3], 3) == False
assert backtracking([40], 3) == False
assert backtracking([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 3) == True
assert backtracking([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 3) == True
print("Tests are passed !")


"""
Второй способ - Dynamic Programming with Memoization and with Bit Masking
Memoizations helps to optimixe the algorithm and make it more DP
And Bit Masking helps to save up some memory
Time Complexity - O(n * 2^n)
Полное обьясниее ниже
"""
def dynamic_programming(nums, k):
	n = len(nums)
   	total_sum = sum(nums)

	if len(nums) < k or total_sum % k != 0: 
		return False

	nums.sort(reverse = True)
	target_sum = total_sum // k

	def dp(mask, cur_sum, results):
		if mask == 0: # если mask равно 0, значит все элементы были использованы,
			# и нам нужно проверить является ли cur_sum равной 0,
			# если это так то мы нашли способ разбиания массива на части k.
			return cur_sum == 0
		elif cur_sum == 0: 
			# если cur_sum просто равен 0, это значает что мы успешно собрали одну часть и k частей,
			# но нам нужно продолжать собирать отсавшиеся части.
			return dp(mask, target_sum, results)

		if (mask, cur_sum) not in results:
			result = False

			# итерируем через все "биты" которые соответствуют всем числам в заданном массиве.
			for bit in range(n):

				# проверяем если число еще не было использовано
				# 1 - неиспользована, 0 - использована.
				if mask & (1 << bit):
					if nums[bit] > cur_sum: 
						continue

					# юзаем XOR чтобы пометить биты как использованные (из 1 сделать 0)
					if dp(mask ^ (1 << bit), cur_sum - nums[bit], results):
						result = True
						break

			results[(mask, cur_sum)] = result

		return results[(mask, cur_sum)] 

	# mask изначально равно 11111...., N
	return dp((2 ** n) - 1, target_sum, dict())

