import pandas as pd, datetime



hero_list = pd.read_json('hero_list.json')
hero_list = hero_list.to_dict('records')
timenow = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
readme_file = open("README.md","w")
readme = '# DOTA2 TI 2022 BATTLEPASS PREDICTIONS TRACKER\n I made this repo to track progress on the battlepass prediction.\nCurrently in progress.\n### To use:\n1. Run the getmatches.ipynb file.\n2. Run the ti11predictions.ipynb file.\n3. Results will then be shown.'
readme += f'\n\n*as of {timenow} PHT*'
readme += f'\n## Heroes'
for i in hero_list:
    readme += f'\n### {i["title"]}'
    for j in i['result']:
        readme += f"\n - {j['name']} : {round(j['value'],2)}"
readme_file.write(readme)
readme_file.close()
