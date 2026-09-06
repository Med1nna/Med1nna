# ROTEIROS LÓGICOS PARA PRATICAR APIs (CONSUMIR E CRIAR)

-------------------------------------------------
CATEGORIA 1: CONSUMINDO APIs (LADO CLIENTE)
-------------------------------------------------

**1. PRIMEIRA REQUISIÇÃO GET** (Fácil)
1. Escolha uma API pública gratuita sem chave (ex: JSONPlaceholder).
2. Faça uma requisição GET para `/posts` e imprima o resultado bruto.
3. Parse: converta o JSON retornado em uma estrutura nativa da sua linguagem (dict/objeto/lista).
4. Extração: percorra a lista e imprima apenas o título de cada post.

**2. PARÂMETROS DE QUERY E FILTROS** (Fácil/Médio)
1. Escolha um endpoint que aceite filtro via query string (ex: `/comments?postId=1`).
2. Monte a URL adicionando o parâmetro dinamicamente, sem escrever o valor fixo na string.
3. Trate o resultado vazio: e se o filtro não retornar nada? O código não pode quebrar.

**3. REQUISIÇÕES POST (Enviando dados)** (Médio)
1. Monte o corpo (body): um objeto/dicionário com os dados a enviar (ex: título e conteúdo de um post novo).
2. Cabeçalhos: configure `Content-Type: application/json`.
3. Envie a requisição POST com o corpo serializado em JSON.
4. Valide a resposta: confira o status code (201 esperado) e leia o corpo retornado (o recurso criado, geralmente com um novo ID).

**4. TRATAMENTO DE ERROS E STATUS CODES** (Médio)
1. Faça uma requisição para um endpoint inexistente (ex: `/postss`) e observe o status (404).
2. Trate faixas de status: 2xx (sucesso), 4xx (erro do cliente), 5xx (erro do servidor).
3. Timeout: configure um limite de espera pela resposta e trate a exceção se o servidor demorar demais.
4. Retry (avançado): implemente uma lógica que tenta de novo até 3 vezes em caso de erro 5xx ou instabilidade de infraestrutura (ex: 520 vindo de proxy/CDN), com um pequeno intervalo entre tentativas — é exatamente o tipo de lógica usada em integrações com APIs de terceiros nem sempre estáveis.

**5. AUTENTICAÇÃO (API Key e Token)** (Médio)
1. Escolha uma API que exija chave/token (ex: reqres.in simula login).
2. Fluxo de login: envie usuário/senha via POST ao endpoint de login e receba um token de volta.
3. Reutilização: armazene esse token e envie-o no header `Authorization: Bearer <token>` nas próximas requisições protegidas.
4. Segurança básica: nunca deixe chave/token escritos direto no código-fonte; use variáveis de ambiente (arquivo `.env`).

**6. CONSUMINDO DADOS RELACIONADOS (Requisições encadeadas)** (Médio)
1. Busque um usuário pelo ID (ex: `/users/1`).
2. Com o resultado, faça uma segunda requisição usando um dado do primeiro (ex: buscar os posts desse usuário em `/posts?userId=1`).
3. Combine: monte um único objeto de saída juntando usuário e sua lista de posts.

-------------------------------------------------
CATEGORIA 2: CRIANDO SUA PRÓPRIA API (LADO SERVIDOR)
-------------------------------------------------

**7. ROTEIRO PARA SUA PRIMEIRA API REST** (Médio/Difícil)
1. Escolha um framework leve (Flask ou FastAPI em Python, Express em Node.js).
2. Defina o recurso: algo simples para modelar (ex: uma lista de tarefas — "tasks").
3. Rota GET: retorna todas as tarefas em JSON.
4. Rota GET por ID: retorna uma tarefa pelo identificador; 404 se não existir.
5. Rota POST: recebe um corpo JSON e adiciona uma nova tarefa (pode começar como uma lista em memória).
6. Rota PUT/PATCH: permite atualizar uma tarefa existente.
7. Rota DELETE: permite remover uma tarefa.
8. Teste tudo: use Postman, Insomnia ou a extensão REST Client do VSCode para testar cada rota manualmente antes de conectar a um front-end.

**8. BOAS PRÁTICAS AO PROJETAR UMA API (o que observar)**
- **Nomenclatura de rotas**: substantivos no plural (`/tasks`, não `/getTasks`) — o verbo HTTP já indica a ação.
- **Status codes corretos**: 200 (ok), 201 (criado), 204 (sem conteúdo, ex: delete), 400 (erro de validação), 401/403 (autenticação/permissão), 404 (não encontrado), 500 (erro interno).
- **Validação de entrada**: nunca confie no que chega; valide tipos, campos obrigatórios e tamanhos antes de processar.
- **Versionamento**: prefixe rotas (ex: `/api/v1/`) para evoluir sem quebrar quem já consome sua API.
- **Documentação**: use um padrão como OpenAPI/Swagger para documentar os endpoints automaticamente.
- **Segurança**: nunca exponha senhas/dados sensíveis nas respostas; use HTTPS; limite taxa de requisições (rate limiting) para evitar abuso.
- **Consistência**: mantenha um único padrão de nomenclatura (camelCase ou snake_case) e um formato de erro padronizado em toda a API.

**9. ROTEIRO DE AUTENTICAÇÃO NA SUA PRÓPRIA API** (Difícil)
1. Rota de registro: recebe usuário/senha e salva o usuário — nunca a senha em texto puro (use hash, ex: bcrypt).
2. Rota de login: verifica usuário/senha e, se válido, gera um token (ex: JWT).
3. Middleware de proteção: cria uma verificação que roda antes das rotas protegidas, checando se o token enviado é válido.
4. Teste o fluxo completo: registre, faça login, pegue o token e use-o para acessar uma rota protegida.

-------------------------------------------------
ONDE E COMO PRATICAR APIs
-------------------------------------------------

**Para consumir (praticar como cliente):**
- **JSONPlaceholder** (jsonplaceholder.typicode.com) — fake REST API clássica, sem cadastro, com relacionamentos entre recursos.
- **reqres.in** e **DummyJSON** — simulam fluxo de login/token e CRUD completo; boas para praticar autenticação sem montar um backend próprio.
- Nenhuma delas persiste dados de verdade (um POST "cria" mas some ao atualizar a página) — é esperado, o foco é o fluxo da requisição.

**Ferramentas para testar (cliente e servidor):**
- **Postman** ou **Insomnia** — interface visual para montar e salvar coleções de requisições.
- Extensão **REST Client** ou **Thunder Client** do VSCode — testa direto no editor, escrevendo a requisição num arquivo `.http`.

**Para criar sua própria API:**
- **Swagger Editor / OpenAPI** — desenhar o contrato da API antes de implementar (design-first).
- **FastAPI** (Python) gera documentação interativa automaticamente a partir do código — ótimo para ver na prática o que uma boa documentação de API parece.

**Como praticar no VSCode:**
- Crie um arquivo `requests.http` no seu projeto e use a extensão REST Client para disparar requisições sem sair do editor.
- Monte um pequeno projeto fim a fim: uma API própria (Categoria 2) consumida por uma página simples em HTML/JS (veja o roteiro de HTML/CSS/JS) — isso fecha o ciclo cliente → servidor de forma muito mais real do que exercícios isolados.
