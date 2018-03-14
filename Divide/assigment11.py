def backtrackRecursive(x, vec):
    if len(x)==0:
        a=-1000000
    else:
        a =x[len(x)-1]
    x.append(vec[0])
    for i in range(0, len(vec)):
        x[len(x) - 1] = vec[i]
        b = vec[i]
        if a < b:
            if len(x)>1:
                print(x)
            backtrackRecursive(x[:], vec[i:])

def backtrackIter(vec):
    pass



vector = [10,2,4,-1, 2, 3]
#backtrackIter(vector)
print("-----------")
backtrackRecursive([],vector)