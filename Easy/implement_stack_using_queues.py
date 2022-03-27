"""
тут опять же два решения - одно использует две очереди, 
другое использует одну (это самое крутое и элегантное решение!!)
вообще Я счтаю что только с одной очередью его решать и нужно

вот решение которое юзает два стака
push - O(1), pop - O(n^2)
реально тупое решение!!
"""

class MyStack:
    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        while len(self.main) != 1:
            self.helper.append(self.main.pop(0))
        value_to_pop = self.main.pop(0)
        while len(self.helper) != 0:
            self.main.append(self.helper.pop(0))
        return value_to_pop

    def top(self) -> int:
        return self.main[-1]

    def empty(self) -> bool:
        return len(self.main) == 0

"""
а вот решие которое юзает всего одну очередь!
push - O(1), pop - O(n^2)
лучше вообще нереально сделать!!
но оно более правильное

весь прикол в функции pop
например наша очередь - 1, 2, 3, 4
мы должны исключить элемент из очереди и добавить его снова
звучит странно, знаю, но очень хиткое решение
начинаем:
1) 2, 3, 4, 1
2) 3, 4, 1, 2
3) 4, 1, 2, 3
вот тут стопаем!!!!
и четверку нам нужно просто удалить без сохранения!
1, 2, 3
готово!!
"""

class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

