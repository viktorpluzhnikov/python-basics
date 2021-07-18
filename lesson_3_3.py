def thesaurus(*args):
    my_dict = {}
    for i in sorted(args):
        first = i[0]
        if first in my_dict:
            my_dict[first] += [i]
        else:
            my_dict[first] = [i]


    return my_dict

print(thesaurus('Gleb','Viktor','Putin','Volodya'))
