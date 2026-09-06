# ROTEIROS LÓGICOS PARA PRATICAR BANCOS DE DADOS

-------------------------------------------------
CATEGORIA 1: CONSULTAS (SELECT)
-------------------------------------------------

**1. SELECT BÁSICO E FILTROS** (Fácil)
1. Base: use uma tabela simples `funcionarios` (id, nome, cargo, salario, departamento).
2. Seleção: escreva um SELECT retornando só `nome` e `salario`.
3. Filtro: adicione um WHERE trazendo só quem ganha acima de um valor.
4. Ordenação: ordene do maior para o menor salário com ORDER BY.

**2. AGRUPAMENTO E FUNÇÕES DE AGREGAÇÃO** (Médio)
1. Agrupe: use GROUP BY `departamento`.
2. Agregue: calcule média (AVG), total (SUM) e contagem (COUNT) por departamento.
3. Filtro pós-agrupamento: use HAVING para mostrar só departamentos com média acima de um valor — diferente de WHERE, que filtra antes de agrupar.

**3. JOINS (Relacionando tabelas)** (Médio)
1. Cenário: `pedidos` (id, cliente_id, valor) e `clientes` (id, nome).
2. INNER JOIN: traga só pedidos com cliente correspondente.
3. LEFT JOIN: traga todos os clientes, mesmo os que nunca fizeram pedido (valor NULL nesse caso).
4. Múltiplos joins: adicione uma terceira tabela (`produtos`) e uma tabela de ligação (`itens_pedido`) simulando um relacionamento N:N.

**4. SUBCONSULTAS (Subqueries)** (Médio/Difícil)
1. Subquery no WHERE: encontre clientes que fizeram pelo menos um pedido acima de X, usando uma subconsulta dentro do WHERE.
2. Subquery no FROM: calcule o total gasto por cliente numa subconsulta e filtre esse resultado na consulta externa.
3. EXISTS: reescreva a mesma lógica usando EXISTS no lugar de IN e compare a legibilidade.

-------------------------------------------------
CATEGORIA 2: MANIPULAÇÃO DE DADOS (DML)
-------------------------------------------------

**5. INSERT, UPDATE, DELETE COM SEGURANÇA** (Médio)
1. INSERT: insira múltiplos registros de uma vez (multi-row insert).
2. UPDATE condicional: atualize o salário de um grupo específico (ex: +10% no departamento X) — sempre com WHERE, nunca sem.
3. DELETE seguro: antes de qualquer DELETE, escreva o mesmo filtro como SELECT primeiro, para conferir exatamente quais linhas serão afetadas.
4. Transação: envolva um conjunto de alterações em uma transação (BEGIN/COMMIT/ROLLBACK) para poder desfazer se algo der errado.

-------------------------------------------------
CATEGORIA 3: MODELAGEM E CRIAÇÃO DE BANCO (DDL + REGRAS DE DESIGN)
-------------------------------------------------

**6. ROTEIRO PARA MODELAR UM BANCO DO ZERO** (Médio/Difícil)
1. Levantamento: liste todas as entidades do domínio (ex: numa loja — Cliente, Produto, Pedido).
2. Atributos: para cada entidade, liste os atributos e identifique a chave primária (PK).
3. Relacionamentos: defina como as entidades se relacionam (1:1, 1:N, N:N) e desenhe um DER antes de criar qualquer tabela.
4. Normalização: revise o modelo até a 3ª Forma Normal (3FN) — sem dados repetidos desnecessariamente, sem dependências parciais ou transitivas.
5. Chaves estrangeiras: toda relação vira uma FK apontando para a PK do lado "1"; relacionamentos N:N viram uma tabela associativa própria.
6. Tipos e restrições: escolha tipos de dado adequados (não use texto genérico para tudo) e defina restrições (NOT NULL, UNIQUE, CHECK) já na criação da tabela.
7. Índices: identifique colunas muito buscadas/filtradas (ex: e-mail, CPF) e crie índices para elas.

**7. REGRAS QUE NÃO DÁ PARA ESQUECER AO CRIAR UM BANCO PARA UMA APLICAÇÃO REAL**
- **Integridade referencial**: nunca permita uma FK "órfã"; configure `ON DELETE`/`ON UPDATE` (CASCADE, RESTRICT, SET NULL) pensando no que faz sentido para o negócio.
- **Evite redundância**: dado que pode ser calculado a partir de outros geralmente não deve ser armazenado duplicado (exceto por performance, e de forma consciente).
- **Nomenclatura consistente**: escolha um padrão (singular/plural, snake_case) e siga em todas as tabelas.
- **Nunca guarde senha em texto puro**: sempre hash (bcrypt, Argon2), nunca a senha original.
- **Backup e migrations**: use ferramentas de migration (Flyway, Liquibase, Alembic ou as do seu framework) para versionar mudanças de schema — nunca altere o banco de produção "na mão".
- **Escalabilidade**: pense se uma tabela vai crescer muito (ex: logs) e considere particionamento/arquivamento já no design.

**8. ROTEIRO DE OTIMIZAÇÃO DE CONSULTAS (para um banco que já existe)** (Difícil)
1. Meça antes de otimizar: use `EXPLAIN` (ou `EXPLAIN PLAN` no Oracle) para ver como o banco está executando a consulta.
2. Índices: confira se as colunas usadas em WHERE, JOIN e ORDER BY têm índice.
3. Evite `SELECT *`: traga só as colunas que você vai realmente usar.
4. Problema N+1: identifique se o código está fazendo uma consulta para cada item de uma lista (clássico em APIs) — resolva trazendo tudo de uma vez com JOIN ou uma consulta em lote.

-------------------------------------------------
ONDE E COMO PRATICAR BANCOS DE DADOS
-------------------------------------------------

- **SQLZoo** — tutoriais + exercícios interativos com feedback imediato; ótimo para começar ou revisar do zero.
- **DB Fiddle** — playground online (MySQL, PostgreSQL, SQLite) para testar consultas sem instalar nada.
- **Oracle Live SQL** — já que você mexe com Oracle no dia a dia, vale a pena para treinar SQL e PL/SQL específicos do Oracle sem precisar de instalação local.
- **LeetCode** (seção Database) e **HackerRank** (domínio SQL) — consultas mais desafiadoras, estilo entrevista técnica.
- **Beecrowd** — também tem uma categoria de exercícios de SQL.
- **DBeaver** — ferramenta visual gratuita para modelar, consultar e explorar seus próprios bancos (PostgreSQL, MySQL, Oracle, SQLite etc.).

**Como praticar no VSCode:**
- Instale a extensão oficial do seu SGBD (ex: "Oracle Developer Tools", "PostgreSQL", "SQLite Viewer") para rodar consultas direto no editor.
- Monte um banco local (SQLite não precisa de servidor) a partir de um DER que você mesmo desenhou — modelar do zero fixa muito mais do que só responder exercícios de consulta prontos.
