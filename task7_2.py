mass = [1, 2, 3, 4, 5, 6, 7, 8]

a = 0

file = open('task7_2.txt', 'w')

def check_single_sym(arr, size):
    ans = 0
    for a in arr:
        count = 0
        if a == 0:
            continue
        for b in range(0, len(arr)):
            if (a == arr[b]):
                count += 1
                arr[b] = 0
        if count == size:
            ans += 1
    if ans == 1:
        return True
    else:
        return False

for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    for a6 in mass:
                        for a7 in mass:
                            check_3 = check_single_sym([a1, a2, a3, a4, a5, a6, a7], 3)
                            check_2 = check_single_sym([a1, a2, a3, a4, a5, a6, a7], 2)
                            if check_3 and check_2:
                                file.write(str([a1, a2, a3, a4, a5, a6, a7]))
                                file.write('\n')
                                a += 1
file.write(str(a))
file.close()

print('done')

# ровно 1 символ 3 раза
# ровно 1 символ 2 раза
