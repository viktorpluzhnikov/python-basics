from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

t_k = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))
print(type(t_k))
for i in zip_longest(tutors, klasses):
    print(i)






