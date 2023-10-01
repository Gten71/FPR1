def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

setA = {1, 2, 3, 4, 5}
setB = {2, 3, 4}
superset(setA, setB)