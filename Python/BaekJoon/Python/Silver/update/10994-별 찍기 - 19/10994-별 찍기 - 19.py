import sys

n = int(sys.stdin.readline())
star = [['*','*', '*', '*', '*'], ['*', ' ', ' ', ' ', '*'],
        ['*',' ', '*', ' ', '*'], ['*', ' ', ' ', ' ', '*'], ['*','*', '*', '*', '*']]
if n ==1 :
    print("*")
elif n ==2 :
    for i in range(4 * (n-1) + 1):
        print(''.join(star[i]))
else:
    for j in range(3, n+1):
        for i in range(len(star)):
            star[i].append(' ')
            star[i].append('*')
            star[i].insert(0, ' ')
            star[i].insert(0, '*')

        for i in range(2):
            star.insert(0, [])
        for i in range(2):
            star.append([])

        star[0].extend(['*' for _ in range(4*(j-1) + 1)])
        star[1].extend([' ' for _ in range(4*(j-1) - 1)])
        star[1].insert(0, '*')
        star[1].insert(len(star[1]), '*')

        star[len(star)-1].extend(['*' for _ in range(4 * (j - 1) + 1)])
        star[len(star)-2].extend([' ' for _ in range(4 * (j - 1) - 1)])
        star[len(star)-2].insert(0, '*')
        star[len(star)-2].insert(len(star[1]), '*')

    for i in range(len(star)):
        print(''.join(star[i]))


