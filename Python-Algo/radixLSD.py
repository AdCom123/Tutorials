import random


def radix(unsorted_list): # falls bugs 
    if len(unsorted_list) <= 1:
        return unsorted_list

    _BASE = 10 # 2 für Binär
    maximum = max(unsorted_list)
    faktor = 1 #1, 10, 100er

    while faktor <= maximum:
        partition = [[] for _ in range(_BASE)]
        for i in unsorted_list:
            idx = (i//faktor) % _BASE # 1337//1 % 10 = 7
            partition[idx].append(i) 

        unsorted_list =[]
        for p in partition:
            unsorted_list += p

        faktor *= _BASE
    
    return unsorted_list
        


l=[random.randint(0,999) for _ in range(100)]
print(radix(l))