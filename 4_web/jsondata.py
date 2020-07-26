import json
import urllib.request


# Get all my repos
def get_data(relative_path=''):
    url = 'https://api.github.com/users/avlye' + relative_path
    request = urllib.request.urlopen(url)
    data = json.loads(request.read())
    return data


def get_repos():
    repos = get_data('/repos')
    return repos


def show_info(data):
    print('Name:', data['name'])
    print('Bio:', data['bio'])

    repos = get_repos()
    print('{} repos found'.format(len(repos)))
    for repo in repos:
        print(repo['full_name'], end='', ')


data = get_data()
show_info(data)