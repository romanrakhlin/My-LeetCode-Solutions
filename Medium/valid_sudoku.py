"""
очень странная задача
и решать ее можно без серьезного знания алгортмов и структур данных
надо только уметь работать с матрицами
про асимтотику очень сложно, хотя что сложного,
с количетсвом поступаемых данных массивы не растут, размер +- всегда один, до 9 максимум
да и по времени, всегда одно и то же вермя работы, так как данные одни и те же
то есть линейное время
поэтому - O(n) runtime, O(1) space

алгоритм разбит на 3 этапа:
1) проверяем все все rows имеют разные числа
2) проверяем что все colums имеют разные числа
3) проверяем что все sub-box 3x3 имеют разные числа
это уже намного сложнее
основная часть времени ушла именно на эту часть
методом проб и ошибок сдлел вот то что получилось
сложно обтяснить как работает, но попытайся понять
сначала я научился проверять один квадратик
потом первый ряд квадратиков
потом перешел на 3 ряда квадратиков
"""

def isValidSudoku(self, board: List[List[str]]) -> bool:  
    # validate rows
    for row in range(0, 9):
        dummy_arr = []
        for column in range(0, 9):
            value = board[row][column]
            if value != ".":
                dummy_arr.append(value)
            
        if len(dummy_arr) != len(set(dummy_arr)):
            return False
    
    # validate columns
    column = 0
    for column in range(0, 9):
        dummy_arr = []
        for row in range(0, 9):
            value = board[row][column]
            if value != ".":
                dummy_arr.append(value)
        
        if len(dummy_arr) != len(set(dummy_arr)):
            return False
        
    # validate sub-boxes
    row = 0
    column = 0
    for max_row in [3, 6 ,9]:
        for max_col in [3, 6, 9]:
            # first
            dummy_arr = []
            while row != max_row:
                while column != max_col:
                    print(row, column)
                    value = board[row][column]
                    if value != ".":
                        dummy_arr.append(value)
                    column += 1
                row += 1
                column = max_col - 3

            # reset vals
            row = max_row - 3
            column = max_col

            # check
            if len(dummy_arr) != len(set(dummy_arr)):
                return False
        
        row = max_row
        column = 0
    
    # the sudoku board is valid 
    return True