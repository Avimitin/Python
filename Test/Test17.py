def test(x,y):
    return x*y

results = [test(x,y) for x in range(10) for y in range(10)]

print(results)