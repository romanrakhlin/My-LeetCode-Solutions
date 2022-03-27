# https://leetcode.com/problems/maximum-subarray/
# https://en.wikipedia.org/wiki/Maximum_subarray_problem

"""
вообще это ОЧЕНЬ популярная проблема ее задают во многих
компаниях по типу гугла или амазона так что уметь ее
решать должен абсолютно каждый 
всего есть несколько подходов один их которых это обыкновенный
брутфорс который рабоате за O(n^2)
то есть мы проходим все значения постепенно сужаясь
-2 2 5 -11 6
   2 5 -11 6
     5 -11 6
       -11 6
           6
но на общей картинке это все равно O(n^2)
"""
def bruteforce_algorithms(arr):
	max_sum = -999999 # задаем желательно очень большой мин элемент
	for i in range(0, len(arr)):
		cur_sum = arr[i] # каждую итерацию задаем cur_sum на i (первый элемент)
		max_sum = max(max_sum, arr[i]) # проверяем для текущего элемента
		for j in range(i + 1, len(arr)):
			cur_sum += arr[j] # добавлям текущее число к cur_sum
			max_sum = max(max_sum, cur_sum)# также сравниваем переменный и меняем
	return max_sum # возвращаем максимальную сумму

"""
но это не очень эффективно и есть Kadane's алгоритм
именно его лучше всего использовать на интервью
ведь он работает за O(n) 
1) смысл в том что смначала мы задаем две переменные
current_sum - для хранения промежуточной суммы (изначально 0)
best_sum - для хранения максимальной current_sum за все время
2) перебираем все числа в массиве
2.1) на каждой итерации мы выбираем продолжить ли считать subarray
прибавляя числа в current_sum или сбросить весь счет снова на 0, 
то есть цепочка не удовлетворяет нас
2.2) в этой же итерации мы сравниваем current_sum и best_sum,
и если cur_sum перерос best_sum, то задаем его как новый best_sum
"""

def max_subarray(numbers):
    best_sum = 0
    current_sum = 0
    for i in numbers:
        current_sum = max(0, current_sum + i)
        best_sum = max(best_sum, current_sum)
    return best_sum

# Тестируем
arr = [-2, 2, 5, -11, 6]
print(bruteforce_algorithms(arr))
print(max_subarray(arr))

