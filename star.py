inp=int(input("Enter the input :"))
for i in range(inp):
    for j in range(2*inp-1):
        if j<(inp-i-1) or j>(inp+i-1):
            print(' ',end='')
        else:
            print('*',end='')
    print()