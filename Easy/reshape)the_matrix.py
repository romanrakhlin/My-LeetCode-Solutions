"""
не очень сложная задачка на матрицы
я смог решить - O(n^2) runtime, O(n) space

алгоритм такой:
1) проверить монжо ли создать новую матрицу из данной,
если нет, то просто вернуть текущую
2) создаем массив для резульата (reshaped)
создаем временный массив в котором будем временно
срхранять скроки для reshaped массива (current_row)
3) проходимся по ВСЕМ элемнтам данном массиве
и сохраняем все элементы в current_row и на каждой
итерации проверяем длинну current_row 

если она станет равна длине row в матрице которая должна по итогу получиться (c)
то тогда добавляем в reshaped этот current_row
ой да и обнуляем current_row
"""

def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    # in originla matrix
    rows = len(mat)
    cols = len(mat[0])
        
    # if its impossible
    if r * c != rows * cols:
        return mat
        
    # overwise
    reshaped = []
        
    current_row = []
    for row in range(rows):
        for col in range(cols):
            current_row.append(mat[row][col])
            print(current_row)
            if len(current_row) == c:
                reshaped.append(current_row)
                current_row = []
        
    return reshaped

# Более короткая запись
def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if r * c != len(mat) * len(mat[0]):
        return mat
        
    reshaped = []
    current_row = []
    for row in mat:
        for element in row:
            current_row.append(element)
            if len(current_row) == c:
                reshaped.append(current_row)
                current_row = []
        
    return reshaped

