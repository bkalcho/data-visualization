# Author: Bojan G. Kalicanin
# Date: 28-Dec-2016
# Identify the most starred Python projects on GitHub.

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
#print("Repositories returned:", len(repo_dicts))

#names, plot_dicts = [], []
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    #plot_dict = {
    #    'value': repo_dict['stargazers_count'],
    #    'label': repo_dict['description'],
        #'xlink': repo_dict['html_url'],
    #    }
    #plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

#chart.add('', plot_dicts)
chart.add('', stars)
chart.render_to_file('python_repos.svg')
# Examine the first repository.
#repo_dict = repo_dicts[0]

#print("\nSelected information about each repository:")
#for repo_dict in repo_dicts:
#    print('Name:', repo_dict['name'])
#    print('Owner:', repo_dict['owner']['login'])
#    print('Stars:', repo_dict['stargazers_count'])
#    print('Repository:', repo_dict['html_url'])
#    print('Created:', repo_dict['created_at'])
#    print('Updated:', repo_dict['updated_at'])
#    print('Description:', repo_dict['description'])