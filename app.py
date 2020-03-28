import os
import re
from github import Github
from subprocess import check_output
import datetime

def regex_function(expression, txt):
    if(expression == ""):
        return True
    return not(re.search(expression, txt))

def delete_branch(branch):
    return check_output('git branch -D %s' % branch, shell=True).strip()


def main():
    try:
        time_now = datetime.datetime.now()
        repository = "hipersoftware/Hiper.Windows.Legado" #os.environ['GITHUB_REPOSITORY']
        token = "97006c480aa631de634c69ce54a9bae37719fa19"#os.environ['INPUT_GITHUB_TOKEN']
        days = 180 #os.environ['DAYS']
        regex_protected_branchs = "" #os.environ['REGEX_PROTECTED_BRANCHS']
        count = 0

        #github_connection = Github(token)

        repo = Github(token).get_repo(repository)

        default_branch = repo.default_branch

        # for x in repo.get_branches():
        #     commit_date = x.commit.commit.committer.date
        #     age = time_now - commit_date
        #     if age > datetime.timedelta(days=days) and regex_function(regex_protected_branchs, x.name) and x.name != default_branch:
        #         print("%s - %s" % (x.name, commit_date))
        #         count+=1
        
        # print("%s branches selecionados" % count)

        delete_branch("dalsenter-ajuste-shared")


    except Exception as err:
        print("Error: %s" % str(err))



if __name__ == "__main__":
    main()    