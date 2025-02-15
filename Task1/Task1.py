def CreateList():
    lst = []
    print("Введите строки (для завершения нажмите Enter):")
    string = input()
    while string:
        lst.append(string)
        string = input()
    return lst

print("Введите элементы первого списка:")
list1 = CreateList()
print("Введите элементы второго списка:")
list2 = CreateList()

def solution(list1, list2):
    common = set(list1) & set(list2)
    return sorted(common)

result = solution(list1, list2)
print("Числа, которые входят в оба списка (в порядке возрастания):", result)