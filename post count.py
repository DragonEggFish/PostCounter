import requests # imports ig
user = input('username: ')
postcount = requests.get('https://scratchdb.lefty.one/v3/forum/user/info/'+user).json()['counts']['total']['count']
print(f'{user} has {postcount} posts.')
