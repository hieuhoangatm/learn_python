t = int(input())
for k in range(t):
    a = input()
    d, id = [], 1
    for i in a:
        if i == '(':
            print(id, end=' ')
            d.append(id)
            id += 1
        elif i == ')':
            print(d[-1], end=' ')
            d.pop()
    print()
