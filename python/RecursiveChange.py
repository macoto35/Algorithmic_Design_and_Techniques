
def greedyChange(money, coins):
    result = money
    cnt = i = 0

    while result > 0:
        if result >= coins[i]:
            result -= coins[i]
            cnt += 1
        else:
            i += 1
    return cnt

def recursiveChange(money, coins):
    if money == 0:
        return 0
    minNumCoins = 100
    for coin in coins:
        if money >= coin:
            numCoins = recursiveChange(money - coin, coins)
            if numCoins + 1 < minNumCoins:
                minNumCoins = numCoins + 1
    return minNumCoins

def dpChange(money, coins):
    minNumCoins = [0] * (money + 1)
    for i in range(1, money + 1):
        minNumCoins[i] = 99999
        for coin in coins:
            if i >= coin:
                numCoins = minNumCoins[i - coin] + 1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i] = numCoins
    return minNumCoins[money]


#print(greedyChange(997, [2,4,8]))
#print(recursiveChange(950, [1,3,4]))
print(dpChange(5, [1,2,3]))

'''
money = 1
coins = [20,8,1]
while True:
    if greedyChange(money, coins) == dpChange(money, coins):
        print(money, ' - success!')
        money += 1
    else:
        print(money, ' - fail!')
        break
'''