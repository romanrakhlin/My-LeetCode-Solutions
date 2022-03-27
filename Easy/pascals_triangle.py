"""
очень сложно асимптотически проанализировать,
но как я понял - O(n^2) space, O(n^2) runtime
потому что на больших значениях реально будет похоже на n^2
но к сожалению лучше решения вообше нет!!

алгоритм такой:
1) задаем в массиве с резульататом изначально первый ряд где просто [1]
2) сделаем цикл который будет идти от 0 до numRows - 1 (- 1 тк первый ряд мы уже добавлии вручную)
3) начинаем создавать новый ряд
- добавляем dummy 1 в начало
- дальше добавляем элементы, где каждый это сумма двух (по которым мы проходмся)
- добавляем dummy 1 в конец
по итогу у нас получится новый ряд
4) беерм добаляем его в основной массив result
5) цикл как раз остановится (сам) и ретерним result
"""

def generate(self, numRows: int) -> List[List[int]]:
    result = [[1]]
        
    for row in range(0, numRows - 1):
        new_row = [1]
            
        for i in range(0, len(result[row]) - 1):
            current_row = result[row]
                
            # sum current element and the next one
            new_row.append(current_row[i] + current_row[i + 1])
            
        new_row.append(1)
            
        # save this row
        result.append(new_row)
        
    return result