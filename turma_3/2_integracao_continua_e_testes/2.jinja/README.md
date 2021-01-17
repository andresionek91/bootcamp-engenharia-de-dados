# Utilizando GitHub Actions

Como usar:
1. Defina as suas credenciais da AWS dentro do seu repositório no GitHub.
    1. Acesse o repositório e vá em settings -> secrets
    1. Adicione as credenciais de um usuário que tenha permissões suficientes para fazer deploy de templates Cloudformation
        1. `AWS_ACCESS_KEY_ID`
        1. `AWS_DEFAULT_REGION`
        1. `AWS_SECRET_ACCESS_KEY`
    1. Adicione as variáveis de ambiente necessárias
        1. `redshiftClusterMasterUsername`
        1. `redshiftClusterMasterUserPassword`

## Deploy para staging
1. Crie um branch chamado `2.jinja_staging`
    1. `git checkout -b 2.jinja_staging`
1. O arquivo que vai controlar este workflow está em `.github/workflows/2.jinja_staging.yml`
    1. Crie um comit e faça push para o seu repositório remoto
    1. O workflow será executado ao fazer push para o branch `2.jinja_staging`
1. Veja o GitHub fazer deploy da sua infraestrutura dentro da aba **Actions**


## Deploy para production
1. Crie um branch chamado `2.jinja_production`
    1. `git checkout -b 2.jinja_production`
1. O arquivo que vai controlar este workflow está em `.github/workflows/2.jinja_production.yml`
    1. Crie um comit e faça push para o seu repositório remoto
    1. O workflow será executado ao fazer push para o branch `2.jinja_production`
1. Veja o GitHub fazer deploy da sua infraestrutura dentro da aba **Actions**


**Lembre de sembre deletar os seus stacks depois da aula para evitar custos inesperados na sua fatura da AWS!**