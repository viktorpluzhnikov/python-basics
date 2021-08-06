import re

def email_parse(email_adress):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)')
    if not RE_email.match(email_adress):
        raise ValueError(f'wrong email: {email_adress}')
    print(RE_email.match(email_adress).groupdict())

for i in ['pluzhnikov93@inbox.ru', 'someone@geekbrainsru', 'someone@geekbrains.ru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)
