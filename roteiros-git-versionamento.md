# ROTEIROS LÓGICOS PARA PRATICAR GIT E VERSIONAMENTO

-------------------------------------------------
CATEGORIA 1: FUNDAMENTOS
-------------------------------------------------

**1. PRIMEIRO REPOSITÓRIO LOCAL** (Fácil)
1. Configure sua identidade: `git config --global user.name "seu nome"` e `git config --global user.email "seu@email.com"` — usado para assinar seus commits.
2. Inicialize: dentro de uma pasta de projeto, rode `git init`.
3. Área de staging: crie um arquivo qualquer, rode `git status` (aparece como "untracked") e adicione-o com `git add nome-do-arquivo` (ou `git add .` para tudo).
4. Primeiro commit: `git commit -m "mensagem descrevendo a mudança"` — salva uma "fotografia" permanente do estado atual.
5. Histórico: `git log` mostra a lista de commits, cada um com hash único, autor e data.
- Quando usar: sempre que terminar uma unidade lógica de trabalho — não espere terminar o projeto inteiro para commitar.

**2. IGNORANDO ARQUIVOS** (Fácil)
1. Crie um arquivo `.gitignore` na raiz do projeto.
2. Liste padrões: `node_modules/`, `.env`, `*.log` para tudo que nunca deve ir ao repositório.
3. Verifique: `git status` não deve mais listar esses arquivos como "untracked".
- Quando usar: desde o primeiro commit — credenciais (`.env`) e pastas geradas automaticamente nunca deveriam entrar no controle de versão.

-------------------------------------------------
CATEGORIA 2: BRANCHES (RAMIFICAÇÕES)
-------------------------------------------------

**3. CRIANDO E TROCANDO DE BRANCH** (Fácil/Médio)
1. Crie: `git branch nome-da-feature`.
2. Troque: `git checkout nome-da-feature` (ou `git switch nome-da-feature`).
3. Atalho: `git checkout -b nome-da-feature` cria e já troca em um único comando.
4. Trabalhe isolado: commite nessa branch, volte para `main` (`git checkout main`) e repare que a mudança "some" da main.
- Quando usar: toda funcionalidade nova, correção de bug ou experimento nasce em sua própria branch, nunca direto na main/master.

**4. MESCLANDO BRANCHES (MERGE)** (Médio)
1. Volte para a branch de destino: `git checkout main`.
2. Mescle: `git merge nome-da-feature`.
3. Fast-forward vs merge commit: se a main não teve commit novo desde a criação da branch, o Git só avança o ponteiro; se teve, cria um commit de merge.
4. Limpeza: `git branch -d nome-da-feature` depois de confirmar que deu certo.
- Quando usar: quando a funcionalidade está pronta e testada, e precisa entrar na branch principal.

**5. RESOLVENDO CONFLITOS DE MERGE** (Médio/Difícil)
1. Provoque um conflito de propósito: edite a mesma linha do mesmo arquivo de formas diferentes em duas branches e tente mesclar.
2. Leia o conflito: o Git marca os trechos com `<<<<<<<`, `=======` e `>>>>>>>`.
3. Decida e edite: apague as marcações e deixe o conteúdo final que você quer.
4. Finalize: `git add` no arquivo resolvido e depois `git commit`.
- Quando usar: aprenda cedo — conflito é normal em qualquer trabalho em equipe, não é sinal de erro.

-------------------------------------------------
CATEGORIA 3: DESFAZENDO MUDANÇAS
-------------------------------------------------

**6. DESFAZENDO COM SEGURANÇA** (Médio)
1. Ainda não commitou: `git restore nome-do-arquivo` descarta mudanças não commitadas (destrutivo, sem "desfazer" depois).
2. Já commitou, quer editar o último commit: `git commit --amend` (só se o commit ainda não foi enviado a um repositório compartilhado).
3. Quer desfazer mantendo histórico visível: `git revert <hash>` cria um novo commit que desfaz o commit indicado — seguro para histórico compartilhado.
4. Quer apagar commits do histórico local (com cautela): `git reset --soft` (mantém mudanças no staging), `git reset --mixed` (mantém mudanças, tira do staging) ou `git reset --hard` (apaga de vez).
- Quando usar: `revert` em histórico já compartilhado/enviado; `reset` só em commits que ainda estão apenas na sua máquina.

-------------------------------------------------
CATEGORIA 4: REPOSITÓRIOS REMOTOS E COLABORAÇÃO
-------------------------------------------------

**7. CONECTANDO A UM REPOSITÓRIO REMOTO** (Fácil/Médio)
1. Crie um repositório vazio no GitHub (ou GitLab/Bitbucket).
2. Conecte: `git remote add origin <url>`.
3. Envie: `git push -u origin main` (o `-u` guarda essa relação para os próximos `push` sem repetir o destino).
4. Atualize localmente: `git pull` traz e já mescla as mudanças enviadas por outras pessoas.
- Quando usar: `pull` antes de começar a trabalhar; `push` depois de commitar.

**8. FLUXO DE COLABORAÇÃO COM PULL REQUESTS** (Médio)
1. Branch própria: crie a partir da main atualizada, para sua tarefa.
2. Push da branch: `git push -u origin nome-da-branch`.
3. Abra o Pull Request (PR): pedindo para mesclar sua branch na main, descrevendo o que foi feito.
4. Revisão: peça (ou simule) revisão de código antes de mesclar.
5. Merge do PR: pela interface do GitHub, depois delete a branch remota.
- Quando usar: é o fluxo padrão em praticamente qualquer empresa que usa Git em equipe — vale muito praticar isso, não só os comandos isolados.

-------------------------------------------------
CATEGORIA 5: HISTÓRICO E INVESTIGAÇÃO
-------------------------------------------------

**9. INVESTIGANDO O HISTÓRICO** (Médio)
1. `git log --oneline --graph --all` — histórico compacto e visual, com ramificações.
2. `git diff` — mostra o que mudou em arquivos não commitados; `git diff <c1> <c2>` compara dois pontos do histórico.
3. `git blame nome-do-arquivo` — mostra quem alterou cada linha por último e em qual commit.
4. `git stash` — guarda mudanças não commitadas temporariamente, permitindo trocar de branch sem perder o trabalho; `git stash pop` traz de volta.
- Quando usar: sempre que precisar investigar uma mudança, trocar de contexto rápido sem perder trabalho, ou entender a origem de um bug.

-------------------------------------------------
TABELA RÁPIDA — QUANDO USAR CADA COMANDO
-------------------------------------------------

| Comando | O que faz | Quando usar |
|---|---|---|
| `git init` | Cria um repositório novo | Início de um projeto |
| `git clone` | Copia um repositório remoto existente | Começar a trabalhar em projeto já existente |
| `git status` | Mostra o estado atual dos arquivos | Antes de qualquer add/commit |
| `git add` | Move mudanças para a staging area | Depois de editar, antes de commitar |
| `git commit` | Salva uma "fotografia" permanente | Ao concluir uma unidade lógica de trabalho |
| `git push` | Envia commits locais para o remoto | Depois de commitar, para compartilhar |
| `git pull` | Traz e mescla mudanças do remoto | Antes de começar a trabalhar |
| `git branch` | Cria/lista branches | Iniciar uma nova funcionalidade |
| `git checkout`/`switch` | Troca de branch | Alternar contexto de trabalho |
| `git merge` | Junta o histórico de duas branches | Incorporar uma funcionalidade pronta |
| `git rebase` | Reaplica commits sobre outra base | Manter histórico linear (cuidado em branches compartilhadas) |
| `git revert` | Desfaz um commit criando um novo commit | Desfazer algo já compartilhado/em produção |
| `git reset` | Move o ponteiro da branch para outro commit | Desfazer commits ainda locais |
| `git stash` | Guarda mudanças não commitadas temporariamente | Trocar de branch sem perder trabalho |
| `git log` | Mostra o histórico de commits | Investigar o que já foi feito |

-------------------------------------------------
ONDE E COMO PRATICAR GIT
-------------------------------------------------

- **Learn Git Branching** (learngitbranching.js.org) — visualiza branches/merges/rebases graficamente; praticamente o padrão-ouro para aprender Git de forma interativa.
- **GitHub Skills** (skills.github.com) — cursos guiados dentro de repositórios reais do GitHub, do primeiro Pull Request até GitHub Actions.
- **Oh My Git!** — jogo educativo que ensina Git através de mecânicas de jogo; bom complemento visual.
- **Prática real**: crie um repositório pessoal só para "treino de Git" e provoque de propósito os cenários difíceis (conflito de merge, precisar reverter algo, recuperar um commit "perdido") — é a única forma de perder o medo desses comandos.

**Como praticar no VSCode:**
- A aba **Source Control** (`Ctrl+Shift+G`) cobre add/commit/push/pull visualmente — bom no dia a dia, mas pratique os comandos no terminal integrado também, porque nem todo ambiente de trabalho tem uma IDE gráfica disponível.
- A extensão **GitLens** adiciona um "blame" inline (quem/quando mudou cada linha) e um histórico visual mais rico direto no editor.
