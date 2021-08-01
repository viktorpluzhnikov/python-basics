import os

script = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, value in script.items():
    if not os.path.exist(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
