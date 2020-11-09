def has_negatives(a):
    hash_table = {} 
    res = []     

    for i in a:
        hash_table[i] = i         
        if i != 0 and -i in hash_table: 
            print(i)             
            res.append(abs(i)) 

    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
