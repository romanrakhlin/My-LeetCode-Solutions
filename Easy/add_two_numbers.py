# https://leetcode.com/problems/add-two-numbers/

"""
очень тупое задание, легче запрогать linked list самому
и написать все методы но они придумали якобы облегчить задачу
и на деле сделали только хуже ну да ладно

решил я ее так сначала написал доп метод который принимает node
и выдает уже перевернутое число int очень удобно
потом я с помощью него обраатываю два числа и нахожу их сумму
когда я нашел сумму для удобства создаю из нее массив (перевернуто)
и наконец остается только создать linked list из нашего массива
вообще это очень легко но изза того что автор задачи намудрил
нам придется мудрить тоже я придумал способ создания result 
как пустой node и наследовать cur от result потом перебирать
все числа в массиве и добалять их в текущий node
и после этого проверять не является ли текущий элемент последним
потому что если это так то мы случайно добавим node после последнего 
(который будет пустой тоесть none) а нам этого не нужно
поэтому после добавления значения мы делаем проверку
если текущий node является последним то делаем break
а если не является то инициализирует cur.next и делаем cur на cur.next
то есть двигаем поинтер и в конце концов произойдет break и мы вернем result
"""

class Solution:
	# вспомагательный метод
    def int_from_ll(self, linked_list):
        result = ""
        cur = linked_list
        while cur is not None:
            result += str(cur.val)
            cur = cur.next
        return int(result[::-1])
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # находу сумму чисел
        first = self.int_from_ll(l1)
        second = self.int_from_ll(l2)
        summ = first + second

        # полученную сумму кладу в массив (перевернуто)
        summ_arr = []
        
        for i in str(summ)[::-1]:
            summ_arr.append(int(i))
        
        # создаем listnode для ответа
        result = ListNode()
        cur = result
        for i in range(0, len(summ_arr)):
            cur.val = summ_arr[i]
            if i == len(summ_arr) - 1:
                break
            cur.next = ListNode()
            cur = cur.next
        
        # выводим ответ
        return result

