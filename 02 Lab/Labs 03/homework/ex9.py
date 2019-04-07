def get_even_list(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result

print(get_even_list([1, 4, 5, -1, 10]))
