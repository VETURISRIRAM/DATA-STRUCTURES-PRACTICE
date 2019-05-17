amount = 5
coins = [1, 2, 5]

def coinChange(S, m, n):

	if n == 0: return 1
	if n < 0: return 0
	if S == []: return 0








length = len(coins)
print(coinChange(coins, length, amount))