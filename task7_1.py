mass = [1, 2, 3, 4, 5, 6, 7, 8]

file = open('task7_1.txt', 'w')

count = 0

for a1 in mass:
    for a2 in mass:
        if a2 == a1:
            continue
        for a3 in mass:
            if a3 == a2 or a3 == a1:
                continue
            for a4 in mass:
                if a4 == a3 or a4 == a2 or a4 == a1:
                    continue
                for a5 in mass:
                    if a5 == a4 or a5 == a3 or a5 == a2 or a5 == a1:
                        continue
                    s = str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + '\n'
                    file.write(s)
                    count += 1

size = 1
for i in range(len(mass)-4, len(mass)+1):
    size *= i

if size != count:
    file.write('wrong mass\n')
else:
    file.write(str(count))

file.close()
