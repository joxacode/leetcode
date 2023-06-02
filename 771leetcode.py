jewels = "aA"
stones = "aAAbbbb"
result = 0
for i in jewels:
    for j in stones:
        if i == j:
            result += 1

print(result)

