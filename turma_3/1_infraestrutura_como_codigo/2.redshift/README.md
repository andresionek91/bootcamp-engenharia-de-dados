# Criando um Cluster Redshift

Para criar um cluster Redshift precisamos primeiro criar alguns recursos adicionais para suportar o nosso banco de dados. São eles:
* VPC
* Subnet
* Route Table
* Internet Gateway
* Security Group
* Redshift Parameter Group
* Redshift Subnet Group
* Redshift Cluster


Para o Deploy:
1. Navegue até a página do Cloudformation no seu console AWS
1. Clique em create stack -> with new resources
1. Faça o upload do arquivo e siga as instruções para fazer o deploy