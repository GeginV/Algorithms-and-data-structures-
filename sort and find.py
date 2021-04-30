while True:
    try:
        inp = list(map(int, input('Give me some numbers').split()))
        numb = int(input('Now give me any number'))
        break
    except ValueError:
        print('You can put only numbers')

def sort(inp):
    for i in range(len(inp)):
        min_index = i
        for j in range(i, len(inp)):
            if inp[j] < inp[min_index]:
                min_index = j
            if i != min_index:
                inp[i], inp[min_index] = inp[min_index], inp[i]
    return inp

def binary_search(inp, numb, left, right):
    middle = (right + left) // 2
    if inp[middle] == numb:
        x = inp[: middle]
        for i in x:
            if i == numb:
                x.remove(numb)
        index_1 = (len(x) - 1)
        y = inp[middle:]
        for n in y:
            if n <= numb and len(y) > 1:
                y.remove(n)
        f = y[0]
        index_2 = inp.index(f)
        if index_1 < 0:
            print(index_2)
        elif index_2 == len(inp) - 1:
            print(index_1)
        else:
            print(index_1, index_2)
        return index_1, index_2
    elif numb < inp[middle]:
        return binary_search(inp, numb, left, middle - 1)
    else:
        return binary_search(inp, numb, middle + 1, right)
