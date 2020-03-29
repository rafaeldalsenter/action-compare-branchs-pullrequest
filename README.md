# action-compare-branchs-pullrequest
🐱‍👤 Github Action para comparar timelines no Pull-request

A intenção dessa Action é criar um controle para que valide a cada pull-request se o branch head está muito "atrasado" em relação ao branch base, estimulando assim, que os desenvolvedores façam merge e mantenham seus branches atualizados.

## Uso

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
