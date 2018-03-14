'''
    Given a array find the maximul subarray sum
'''

data = [-2,-5,6,-2,-3,1,5,-6]

def maxArray(data):
    maxi = data[0]
    maxGlobal = data[0]
    for i in range(1,len(data)):
        if data[i] > maxi + data[i]:
            maxi=data[i]
        else:
            maxi=maxi+data[i]
        maxGlobal=max(maxi,maxGlobal)
    return maxGlobal

print(maxArray(data))
