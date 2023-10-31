for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    stack =[]
    doDai = [0]*n   

    for i in range(0,len(a)):
        while len(stack) > 0 and a[stack[-1]] <= a[i]:
            stack.pop()
        doDai[i] = i+1 if len(stack) == 0 else i - stack[-1]
        stack.append(i)
    print(*doDai)
    
               