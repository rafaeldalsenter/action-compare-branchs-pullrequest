# action-compare-branchs-pullrequest
🐱‍👤 Github Action to compare timeline between branches of a pull-request

This action validates in the pull-request if the branch Head is obsolete in relation to the Base branch. Validation is done through the parameter `NUMBER_COMMITS_DIFF`, encouraging developers to keep their BRANCHES up to date.

## Usage

```yaml
on: [pull_request]
jobs:
  compare:
    runs-on: ubuntu-latest
    steps:
    - uses: docker://rafaeldalsenter/action-compare-branchs-pullrequest:latest
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        NUMBER_COMMITS_DIFF: 10
```
