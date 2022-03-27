# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
знаююююю неэффективно пиздец как ! но это сработало
работает за O(n^2) ведь два вложенных цикла

суть в том что мы должны пробегаться по всем элементам строки
и начинать составлять там строку temp до того момента пока
не дойдем до элемента уже находящимся в temp
если мы еще не дошли до такого элемента то добавляем в temp
текущий элемент и добавляем длинну составленной строки
в hash table с ключем j он учикальный так как именно с него
мы начинали состаление строки когда мы дойдем до элемента 
который уже есть в temp то делаем break и начинаем составлять строку
temp со следующего символа в строке и так же добалвять все реузультаты
в hash table когда мы пройдем все элементы просто пробежимся по
всем value в hash table и добавим их во временный массив arr
а потом выведем максимальный из них
"""

def lengthOfLongestSubstring(s):
	if len(s) <= 1:
		return len(s)

	results = {}
	for j in range(0, len(s)):
		temp = ""
		for i in range(j, len(s)):
			if s[i] not in temp:
				temp += s[i]
				results[j] = len(temp)
			else:
				break
	
	arr = []
	for i in results.values():
		arr.append(i)
	return max(arr)

# Тестики
print(lengthOfLongestSubstring("abcdfscds"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("abccdfg"))
print(lengthOfLongestSubstring(" "))