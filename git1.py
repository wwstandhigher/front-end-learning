n = int(input())
def sushu(x):
    if all(x% i != 0 for i in range(2,x+1)):

        return 1

    else:
        return 0

def fj(x):
    for i in range(0,x):
        if x % i == 0:
            x1 = i
            x2 = x/i
    if sushu(x1) == 1:
        ls.append(x1)
    else :
        fj(x1)
    if sushu(x2) == 1:
        ls.append(x2)
    else :
        fj(x2)
ls=[]
fj(n)

ls.sort
print(ls)

