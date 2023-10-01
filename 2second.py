def insert_element(lst, k, C):
    if k < 0 or k > len(lst):
        return "Индекс k вне диапазона"
    lst.insert(k, C)
    return lst

my_list = [1, 2, 3, 4, 5]
k = 2 # index 0,1,2...
C = 99
result = insert_element(my_list, k, C)
print(result) 
