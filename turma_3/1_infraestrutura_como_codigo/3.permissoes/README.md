# Gerenciando acessos e permissões com IAM

Deploy:
1. Navegue até a página do Cloudformation no seu console AWS
1. Clique em create stack -> with new resources
1. Faça o upload do arquivo e siga as instruções para fazer o deploy

Para testar:
1. Com um acesso admin, crie um usuário e o adicione ao grupo `iam-group-data-engineer`
1. Entre no seu painel AWS com as credenciais desse novo usuário que foi adicionado ao grupo.
1. Clique no nome do seu usuário no menu superior direito
1. Clique em Switch Roles
1. Preencha os campos:
    1. Account: número da sua conta AWS (12 dígitos)
    1. Role: `role-production-data-engineer`
    1. Display Name: Nome da sua escolha ex: `Data Engineer`
    
Agora esse usuário assumiu o role `role-production-data-engineer` e só tem as permissões descritas dentro da política `IamPolicyDataEngineer`. 

Use isso para separar permissões para grupos diferentes de usuários: Analistas, Desenvolvedores, Cientistas de Dados, Admins, etc.