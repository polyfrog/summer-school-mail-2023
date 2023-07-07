from CGPCLI.Commands import Server
from tabulate import tabulate


def get_full_name(settings):
    if 'RealName' in settings:
        return settings['RealName'] 
    return ''

def get_creation_date(info):
    if 'Created' in info:
        return info['Created']
    return ''


def get_last_login(info):
    if 'LastLogin' in info:
        return info['LastLogin'].strftime('%d-%m-%Y_%H:%M:%S')
    return ''


host = ''
auth_username = ''
password = ''

server = Server(host)
server.connect()
server.login(auth_username, password)

domains = server.list_domains()['body']
domain = domains[2]

users = server.list_accounts(domain)['body']

headers = ['Имя', 'Адрес', 'Дата создания', 'Последний вход']
output = []

for user in users:
    email = f'{user}@{domain}'
    settings = server.get_account_effective_settings(email)['body']
    info = server.get_account_info(email)['body']

    full_name = get_full_name(settings)
    creation_date = get_creation_date(info)
    last_login = get_last_login(info)

    output.append([full_name, email, creation_date, last_login])

print(tabulate(output, headers=headers))