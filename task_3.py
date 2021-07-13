for percent in range(20):
    if percent % 10 == 1 and percent % 100 != 11:
        print(percent,'процент')
    elif percent % 10 != 1 and percent < 5:
        print(percent, 'процента')
    else:
        print(percent,'процентов')