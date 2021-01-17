# Utilizando GitHub Actions

Como usar:
1. Defina as suas credenciais da AWS dentro do seu repositório no GitHub.
    1. Acesse o repositório e vá em settings -> secrets
    1. Adicione as credenciais de um usuário que tenha permissões suficientes para fazer deploy de templates Cloudformation
        1. AWS_ACCESS_KEY_ID
        1. AWS_DEFAULT_REGION
        1. AWS_SECRET_ACCESS_KEY
    ![](segredos.png)
1. Crie um branch chamado `1.github_actions`
    1. `git checkout -b 1.github_actions`
1. O arquivo que vai controlar este workflow está em `.github/workflows/1.github_actions.yml`
    1. O workflow será executado ao fazer push para o branch `1.github_actions`
        1. `git push --set-upstream origin 1.github_actions`
1. Veja o GitHub fazer deploy da sua infraestrutura dentro da aba **Actions**


**Lembre de sembre deletar os seus stacks depois da aula para evitar custos inesperados na sua fatura da AWS!**