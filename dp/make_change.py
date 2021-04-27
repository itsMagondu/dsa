# How many ways are there to make change from the currency provided.

def make_change(money, coins, list_index=0, memo={}):
  if money == 0:
    return 1

  if list_index >= len(coins):
    return 0

  key = f"{money}-{list_index}"
  if key in memo:
    return memo[key]

  amountWithCoins = 0
  ways = 0
  while (amountWithCoins <= money):
    remaining = money - amountWithCoins
    ways += make_change(remaining, coins, list_index+1, memo)
    amountWithCoins += coins[list_index]

  memo[key] = ways
  return ways

def find_change(money, coins):
  return make_change(money, coins, 0, {})

print ("change 1: ", make_change(27, [10,5,2,1]))
print ("change 2: ", make_change(5, [5,2,1]))
print ("change 3: ", make_change(3, [5,2,1]))
print ("change 4: ", find_change(3, [1])) # Should return 1. Only one way to make change.
print ("change 5: ", find_change(3, [2])) # Should return 0. Cannot make change here.