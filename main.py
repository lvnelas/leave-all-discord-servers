import requests

token = 'your_token_here'
headers = {
            'Authorization': token,
        }
r = requests.get('https://discord.com/api/users/@me/guilds', headers=headers)
guilds = r.json()
count = -1

for guild in guilds:
    guild_id = guilds[count]['id']
    guild_name = guilds[count]['name']
    isowner = guilds[count]['owner']
    count += 1

    if isowner:
        print(f'Você não pode sair do servidor {guild_name} pois é dono dele.')
    else:
        wantto = str(input(f'Você deseja sair do servidor {guild_name}? '))
        if wantto == '1':
            x = requests.delete(f'https://discord.com/api/users/@me/guilds/{guild_id}', headers=headers)
            print(f'Você saiu do servidor {guild_name}!')
        else:
            continue
