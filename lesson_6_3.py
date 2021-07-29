from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        users.seek(0)
        hobby.seek(0)
        with open("u_h.json", "w", encoding="utf-8") as f:
            all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
            m_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}
            dump(m_dict, f)
        print(m_dict)
