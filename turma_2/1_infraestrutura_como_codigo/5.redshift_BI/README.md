# Integrando Redshift a uma ferramenta de BI

O processo de conexão do Redshift a uma ferramenta de BI é sempre muito parecido, independente da ferramenta que você utilize.
Aqui vamos utilizar o [Metabase](https://www.metabase.com/start/oss/) com Docker.

```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

1. Acesse o Metabase em `localhost:3000`
1. Pegue o host do seu Redshift no painel da AWS (lembre que a senha e usuário estão hardcoded no template de Redshift por enquanto)
1. No passo 3 da configuração do Metabase, adicione os seus dados.
![](metabase.png)
1. Crie suas queries e dashboards!

