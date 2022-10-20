import pandas as pd, datetime
pd.options.display.max_colwidth = 150



def create_readme():
    heroes = pd.read_json('working/heroes.json')
    heroes = heroes.rename(columns={'name':'url'})
    heroes['url'].replace('npc_dota_hero_','https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/',regex=True,inplace=True)
    print(heroes)
    hero_list = pd.read_json('hero_list.json')
    hero_list = hero_list.to_dict('records')
    player_list = pd.read_json('player_list.json')
    player_list = player_list.to_dict('records')
    teams = pd.read_json('working/teams.json')
    team_list = pd.read_json('team_list.json')
    team_list = team_list.to_dict('records')
    tournament_list = pd.read_json('tournament_list.json')
    tournament_list = tournament_list.to_dict('records')
    timenow = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    readme_file = open("README.md","w",encoding="utf-8")
    readme = '# DOTA2 TI 2022 BATTLEPASS PREDICTIONS TRACKER\n I made this repo to track progress on the battlepass prediction.\nCurrently in progress.\n### To use:\n1. Run the getmatches.ipynb file.\n2. Run the ti11predictions.ipynb file.\n3. Results will then be shown.'
    readme += f'\n\n*as of {timenow} PHT*'
    readme += f'\n## Heroes'
    for i in hero_list:
        readme += f'\n\n**{i["title"]}**'
        for j in i['result']:
            hero_url = heroes[heroes['localized_name']==j['name']]['url'].to_string(index=False)
            readme += f"\n - <img src='{hero_url}.png' width='50'/> {j['name']} : {round(j['value'],2)}"
    readme += f'\n## Teams'
    for i in team_list:
        readme += f'\n\n**{i["title"]}**'
        for j in i['result']:
            team_url = teams[teams['name']==j['name']]['team_id'].to_string(index=False)
            team_url = 'https://cdn.cloudflare.steamstatic.com/apps/dota2/teamlogos/' + team_url
            try:
                readme += f"\n - <img src='{team_url}.png' width='50'/> {j['name']} : {round(j['value'],2)}"
            except:
                readme += f"\n - <img src='{team_url}.png' width='50'/> {j['name']} : {j['value']}"
    readme += f'\n## Players'
    for i in player_list:
        readme += f'\n\n**{i["title"]}**'
        for j in i['result']:
            readme += f"\n - {j['team_tag']}.{j['name']} : {round(j['value'],2)}"
    readme += f'\n## Tournament'
    for i in tournament_list:
        readme += f'\n\n**{i["title"]}**'
        try:
            readme += f"\n - {round(i['result'],2)}"
        except:
            readme += f"\n - {i['result']}"
    readme_file.write(readme)
    readme_file.close()