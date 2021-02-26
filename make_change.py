def make_change(value, coins, changes, s):
    if len(coins) == 1:
        fc = changes[:]
        fc.append(value // coins[0])
        s.append(fc)
    else:
        coin = coins[0]
        c = value // coin + 1
        for i in range(c):
            changes.append(i)
            make_change(value-i*coin, coins[1:], changes, s)
            changes.pop()

if __name__ == "__main__":
    coins = [25, 10, 5, 1]
    changes = []
    s = []

    value = input("Enter your value: ")

    make_change(int(value), coins, changes, s)
    print(s)
