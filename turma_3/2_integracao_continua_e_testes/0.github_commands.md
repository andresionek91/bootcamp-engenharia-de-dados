# Introdução bem básica e superficial ao Git

Durante as aulas usamos o git para fazer o controle de versão de nosso código. Seguem alguns comandos importantes que utilizamos:

1. Inicializa um repositório git no diretório atual: `git init`
1. Adiciona todos os arquivos para staging: `git add --all`
1. Addiciona arquivos para staging no modo interativo: `git add -i` 
1. Nome do arquivo onde listamos os arquivos e diretórios que devem ser ignorados: `.gitignore`
1. Exibe os arquivos que estão em staging: `git `
1. Cria um commit com os arquivos que estão em staging: `git commit`
1. Exibe o log de commits: `git log`
1. Cria um novo branch a partir do branch atual: `git checkout -b nome-do-branch`
1. Troca de branch: `git checkout nome-do-branch`
1. Exibe os branches (com * no branch atual): `git branch`
1. Seta um repositório remoto: `git remote add origin https://github.com/seu-usuario/seu-repo.git`
1. Faz o download de mudanças do repositório remoto para o local: `git pull`
1. Faz o upload de mudanças do repositório local para o remoto: `git push`
1. Faz push e seta um branch remoto para o seu branch local (necessário no primeiro push de um novo branch): `git push --set-upstream origin <branch>`
1. Rebase interativo: `git rebase -i HEAD~5` (faz o rebase interativo de 5 commits antes de HEAD)
1. Force push do seu repo local para o remoto (sobrescreve o branch remoto com o branch local). NUNCA FAÇA NA MASTER! `git push --force`
1. Reseta o seu branch local para uma origem remota (perde todas as mudanças locais): `git reset --hard origin/nome-do-branch-que-quer-resetar`

## Apêndice:
**Se você ficar preso na tela de commit é porque vc entrou no VIM e não sabe como sair. Boa sorte :P**

Eu utilizo o nano como meu editor padrão do git. Não gosto do VIM (ok me apedrejem). Para trocar o editor padrão para o nano:
```
git config --global core.editor "/nano"
```

Para sair de algumas telas do git você precisa apertar a tecla `Q`.

Você também pode utilizar uma IDE:
* O próprio PyCharm e os VSCode possuem add-ons e suporte para git
* Também existem softwares específicos como o [GitKraken](https://www.gitkraken.com/)
