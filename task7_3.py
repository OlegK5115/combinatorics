mass = [1, 2, 3, 4, 5, 6, 7, 8]

a = 0

file = open('task7_3.txt', 'w')

def check_func(arr, elem):
    ans = 0
    for a in arr:
        if a == elem:
            ans += 1
    if ans == 3:
        return True
    else:
        return False

for a1 in mass:
    for a2 in mass:
        for a3 in mass:
            for a4 in mass:
                for a5 in mass:
                    for a6 in mass:
                        if check_func([a1, a2, a3, a4, a5, a6], 2):
                            file.write(str([a1, a2, a3, a4, a5, a6]))
                            file.write('\n')
                            a += 1
file.write(str(a))
file.close()

print('done')
