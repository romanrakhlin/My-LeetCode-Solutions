"""
O(1) space, O(n) runtime
Stack solution
most popular and easy to write one!!
"""
def isValid(self, s: str) -> bool:
    my_stack = ["some dummy string"]

    for i in s:
        if i == ")" and my_stack[-1] == "(":
            my_stack.pop()
        elif i == "}" and my_stack[-1] == "{":
            my_stack.pop()
        elif i == "]" and my_stack[-1] == "[":
            my_stack.pop()
        else:
            my_stack.append(i)
            
    return len(my_stack) == 1

"""
O(1) space, O(n) runtime
Second Stack solution
really accurace solution but boooooring !!!!
"""
def isValid(self, s: str) -> bool:
    stack = []

    hash_map = {'}':'{', ')':'(', ']':'['}
    open_brackets = hash_map.values()

    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if len(stack) > 0 and stack[-1] == hash_map[bracket]:
                stack.pop()
            else:
                return False
    
    return len(l) == 0

