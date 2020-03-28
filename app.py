import os
from github import Github

def main():
    try:
        repository = os.environ['GITHUB_REPOSITORY']
        token = os.environ['GITHUB_TOKEN']
        pr_number = os.environ['PR_NUMBER']
        number_commits_diff = os.environ['NUMBER_COMMITS_DIFF']

        repo = Github(token).get_repo(repository)
        pull_request = repo.get_pull(pr_number)
        compare = repo.compare(pull_request.head.ref, pull_request.base.ref)

        if(compare.total_commits > number_commits_diff):
            print(f"::set-output name=defaultOutput::Há uma diferença entre mais de {number_commits_diff} commits entre o branch Head e Base")
            return 1

        print(f"::set-output name=defaultOutput::Branchs Head e Base alinhados!")
        return 0

    except Exception as err:
        print(f"::set-output name=defaultOutput::Erro {str(err)}")
        return 1

if __name__ == "__main__":
    main()    