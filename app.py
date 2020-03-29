import os
import sys
import json
from github import Github

def readJson(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data

def main():
    try:
        repository = os.environ['GITHUB_REPOSITORY']
        token = os.environ['GITHUB_TOKEN']
        path = os.environ['GITHUB_EVENT_PATH']
        number_commits_diff = int(os.environ['NUMBER_COMMITS_DIFF'])
        prefix_output = '::set-output name=default::'

        event = readJson(path)

        repo = Github(token).get_repo(repository)
        pull_request = repo.get_pull(event['number'])
        compare = repo.compare(pull_request.head.ref, pull_request.base.ref)

        if(compare.total_commits > number_commits_diff):
            print(f'{prefix_output}This is a difference of {number_commits_diff} commits between branches Head and Base')
            sys.exit(1)

        print(f'{prefix_output}Branches Head and Base are up to date')
        sys.exit(0)

    except Exception as err:
        print(f'{prefix_output}Error {str(err)}')
        sys.exit(1)

if __name__ == '__main__':
    main()    