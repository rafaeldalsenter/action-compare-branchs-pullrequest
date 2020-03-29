import os
import sys
import json
from github import Github

def main():
    try:
        repository = os.environ['GITHUB_REPOSITORY']
        token = os.environ['GITHUB_TOKEN']
        event = json.load(os.environ['GITHUB_EVENT_PATH'])
        number_commits_diff = os.environ['NUMBER_COMMITS_DIFF']

        repo = Github(token).get_repo(repository)
        pull_request = repo.get_pull(event["pull_request"]["number"])
        compare = repo.compare(pull_request.head.ref, pull_request.base.ref)

        if(compare.total_commits > number_commits_diff):
            print(f"Há uma diferença entre mais de {number_commits_diff} commits entre o branch Head e Base")
            sys.exit(1)

        print(f"Branchs Head e Base alinhados!")
        sys.exit(0)

    except Exception as err:
        print(f"Erro {str(err)}")
        sys.exit(1)

if __name__ == "__main__":
    main()    