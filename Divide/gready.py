'''
    The coin problem
'''
'''
    Returns the list of values of coins wich fill into the sum
    with the smallest list of coin values
'''
def coins(coinList,sum):
    '''
        Returns the list of values of coins wich fill into the sum
        with the smallest list of coin values
        input:
            -list of the coins
            -the sum we want to return
        output:
            -the list of the coin balues wich fit into the sum
            -emplty list if the coni values does not fit
    '''
    newList=[]
    index = 0
    while (sum != 0):
        if sum - coinList[index] <0:
            index+=1
        else:
            sum = sum - coinList[index]
            newList.append(coinList[index])
    return newList

def Coin_Test():
    coinList = [50,10,5,1]
    rez = coins(coinList,35)
    print(rez)

Coin_Test()
