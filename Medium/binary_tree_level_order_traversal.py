"""
к этому алгоритму я пришел далеко не сразу
сначала я пытался ее решить как-то юзая DFS
потом меня осенило что тут идеально подходит BFS

первым делал я написал сам BFS и проверил корректность его работы
после этого я начал его улучшать
все улучшение состоит в том что в cur_node
вмето обысного TreeNode, мы храним 
tuple(уровень дерева текущего TreeNode, и сам TreeNode)
уровень мы обновляем так: когда мы проверяем не равны ли childen None
мы добавляем в queue эти ноды, но изменяем в их tuple 
уровень просто прибавляя 1 к уровню их parent
ну и в массив visited мы добвляем все тот же tuple

по итогу у нас получается такой же visited массив
но на этот раз он сожержит tuple где храняться значения и их уровень в дереве

остается только обработать это массив и вывести результат
"""

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
        
    cur_node = (0, root)
    visited = []
    queue = [cur_node]
        
    while len(queue) != 0:
        cur_node = queue[0]
            
        if cur_node[1].left is not None:
            queue.append((cur_node[0] + 1, cur_node[1].left))     
                
        if cur_node[1].right is not None:
            queue.append((cur_node[0] + 1, cur_node[1].right))   
            
        queue.pop(0)
        visited.append((cur_node[0], cur_node[1].val))
        
    # gathering result
    result = []
        
    for node in visited:
        if (len(result) - 1) == node[0]:
            result[node[0]].append(node[1])
        else:
            result.insert(node[0], [node[1]])
        
    return result