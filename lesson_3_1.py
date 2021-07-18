my_dict = {"zero":"ноль","one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть",
           "seven":"семь", "eight":"восемь", "nine":"девять", "ten":"десять"}


def num_translate(slovo):
    return my_dict.get(slovo)

print(num_translate(input('Введите число:')))