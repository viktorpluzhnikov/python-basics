def my_f():
    n = 15
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)
        else:
            yield


for z in my_f():
    print(z)
