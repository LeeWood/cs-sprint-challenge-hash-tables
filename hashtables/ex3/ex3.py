def intersection(arrays):
    table = {}  
    res = [] 

    for a in arrays:
        for num in a:
            if num not in table:
                table[num] = None
            elif num not in res:
                    res.append(num)

    return res


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
