
def backtrackRecursive(x,n):
    x.append(0)
    print(x)
    for i in range(0,n):
        x[len(x)-1]=i
        if consistent(x,n):
            if solution(x,n):
                solutionFound(x,n)
            else:
                backtrackRecursive(x[:],n)

def consistent(x,n):
    pos = len(x)-1
    row=x[pos:(pos//n)*n-1:-1]
    column=x[pos::-n]
    if len(row)!=len(set(row)):
        return False
    if len(column)!=len(set(column)):
        return False
    return True

def solution(x,n):
    if len(x)==n*n:
        print(x)
        return True
    return False

def solutionFound(x,n):
    pass

backtrackRecursive([],2)