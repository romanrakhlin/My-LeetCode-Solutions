"""
у этого рещения такая асимптотика
O(1) space, O(n) runtime

поясняю за алгоритм:
1) создаем hash_map со всеми буквами в magazine
где value к каждой букве будет количество появлений в строке
наример: если дана строка "aab" -> {a: 2, b: 1}
2) делаем то же самое для строки ransomeNote
по итогу получается: {a: 2, b: 1} и {a: 2}"
3) проходимся по всем буквам в hash_map от amgazine
и если текущая буква есть в hash_map ransomeNote, то
вычитаем количество появлений буквы в magazine из
количестве поялений буквы в ransomeNote
например: {a: 2, b: 1} - {a: 2} -> {a: 0}
4) проходимя по hash_map от ransomeNote
точнее по тому что от него отсталось))))))
и проеряем чтобы все буквы были равны 0 или меньше
то есть то что мы все их смогли воссоздать буквами
из строки magazine, то есть вообще ни однрй не пропустили
и если все окей возвраем Ttue. а если вдруг у какойто
буквы осталось значенпие больше 0, тогда возвращаем False
"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    # 1
    hashMagazine = {}
    for letter in magazine:
        if letter in hashMagazine:
            hashMagazine[letter] += 1
        else:
            hashMagazine[letter] = 1
    
    # 2   
    hashRansomNote = {}
    for letter in ransomNote:
        if letter in hashRansomNote:
            hashRansomNote[letter] += 1
        else:
            hashRansomNote[letter] = 1
      
    # 3  
    print(hashMagazine, "-", hashRansomNote)
    for letter in hashMagazine:
        if letter in hashRansomNote:
            hashRansomNote[letter] -= hashMagazine[letter]
    print(hashRansomNote)
     
    # 4   
    for letter in hashRansomNote:
        if hashRansomNote[letter] != 0:
            return False
        
    return True

canConstruct("aa", "aab")