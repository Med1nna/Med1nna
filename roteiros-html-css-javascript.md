# ROTEIROS LÓGICOS PARA PRATICAR HTML, CSS E JAVASCRIPT

-------------------------------------------------
CATEGORIA 1: HTML — ESTRUTURA E SEMÂNTICA
-------------------------------------------------

**1. PÁGINA SEMÂNTICA BÁSICA** (Fácil)
1. Estrutura: monte o esqueleto de uma página (um "sobre mim" ou currículo) usando tags semânticas — `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` — evite usar só `<div>` para tudo.
2. Hierarquia de títulos: use `<h1>` uma única vez por página; organize o resto com `<h2>`, `<h3>` respeitando a hierarquia (não pule níveis só pelo tamanho da fonte).
3. Formulário simples: adicione um formulário de contato com `<label>` associado a cada `<input>` (via `for`/`id`) e ao menos um campo obrigatório (`required`).
4. Validação: teste enviar o formulário vazio e veja a validação nativa do navegador funcionar sem nenhuma linha de JavaScript.
- Por que importa: HTML semântico melhora acessibilidade (leitores de tela) e SEO — não é só estética.

-------------------------------------------------
CATEGORIA 2: CSS — LAYOUT E ESTILO
-------------------------------------------------

**2. CENTRALIZANDO E ALINHANDO COM FLEXBOX** (Fácil/Médio)
1. Container: crie uma `<div>` com 3+ "cartões" filhos.
2. Ative o Flexbox: aplique `display: flex` no container.
3. Alinhamento: use `justify-content` (horizontal) e `align-items` (vertical).
4. Responsividade básica: adicione `flex-wrap: wrap` e veja os cartões se reorganizarem em tela estreita.

**3. GRID PARA LAYOUTS COMPLEXOS** (Médio)
1. Defina o grid: `display: grid` no container e colunas com `grid-template-columns` (ex: `repeat(3, 1fr)`).
2. Áreas nomeadas: use `grid-template-areas` para nomear regiões (header, sidebar, conteúdo, footer) e posicione cada filho com `grid-area`.
3. Espaçamento: use `gap` em vez de margin manual em cada item.
4. Responsivo: use `@media` para trocar de 3 colunas para 1 coluna em telas pequenas.

**4. RESPONSIVIDADE COM MEDIA QUERIES** (Médio)
1. Mobile-first: escreva primeiro o CSS pensando na tela pequena, sem nenhuma media query.
2. Breakpoints: adicione `@media (min-width: 768px)` e `@media (min-width: 1024px)`, acrescentando estilos conforme a tela cresce.
3. Unidades relativas: troque `px` fixo por `rem`, `%` ou `vw`/`vh` onde fizer sentido, respeitando preferências de fonte do usuário.
4. Teste real: use o modo de dispositivo do DevTools (F12) em pelo menos 3 tamanhos de tela diferentes.

-------------------------------------------------
CATEGORIA 3: JAVASCRIPT — FUNDAMENTOS
-------------------------------------------------

**5. MANIPULAÇÃO DO DOM** (Fácil/Médio)
1. Seleção: `document.querySelector`/`querySelectorAll` para pegar elementos da página.
2. Evento: adicione `addEventListener('click', ...)` em um botão.
3. Alteração: ao clicar, altere conteúdo (`textContent`), uma classe (`classList.toggle`) ou estilo de outro elemento.
4. Criação dinâmica: crie um elemento com `document.createElement`, preencha e adicione à página com `appendChild`.
- Projeto sugerido: uma lista de tarefas (to-do list) — adicionar, marcar como concluída e remover itens — cobre praticamente tudo isso de uma vez.

**6. FORMULÁRIOS E VALIDAÇÃO COM JAVASCRIPT** (Médio)
1. Capture o envio: listener no evento `submit` do formulário, com `event.preventDefault()` para impedir o recarregamento da página.
2. Leia os valores: `input.value` de cada campo.
3. Valide: campo vazio, formato de e-mail, tamanho mínimo de senha — mostre mensagens específicas por campo que falhar.
4. Feedback visual: adicione/remova uma classe CSS (ex: `.erro`) nos campos inválidos.

-------------------------------------------------
CATEGORIA 4: JAVASCRIPT — ASSÍNCRONO E INTEGRAÇÃO
-------------------------------------------------

**7. CONSUMINDO UMA API COM FETCH** (Médio)
1. Requisição: `fetch(url)` para buscar dados de uma API pública (ex: JSONPlaceholder).
2. Promise: trate o resultado com `.then()` (ou `async/await`, mais legível) e converta a resposta em JSON.
3. Renderização: percorra os dados e crie elementos HTML dinamicamente na página (não use só `console.log`).
4. Tratamento de erro: `.catch()` (ou try/catch com `async/await`) para mostrar mensagem amigável se a requisição falhar.
- Veja também: o roteiro de APIs tem uma trilha completa sobre esse tema.

**8. PROJETO INTEGRADOR: LANDING PAGE RESPONSIVA COM INTERATIVIDADE** (Difícil)
1. Estrutura: monte uma landing page de página única (header fixo, hero, funcionalidades/produtos, formulário de contato, footer) com HTML semântico.
2. Estilo: Flexbox/Grid, mobile-first, funcionando bem em mobile e desktop.
3. Interatividade: adicione ao menos 2 comportamentos com JavaScript (menu hambúrguer, carrossel simples, acordeão de perguntas frequentes).
4. Dados reais: busque algo de uma API pública (cotação, frase aleatória, clima) e exiba dinamicamente.
5. Publicação: suba o projeto no GitHub Pages, Vercel ou Netlify (gratuitos) para ter um link real no portfólio.

-------------------------------------------------
ONDE E COMO PRATICAR HTML, CSS E JAVASCRIPT
-------------------------------------------------

- **Frontend Mentor** — desafios com design real (Figma/imagens) para reproduzir com código; ótimo para sair de "eu sei CSS" para "eu entrego uma tela real".
- **CSS Battle** — replicar uma imagem usando o mínimo de código CSS possível; ótimo para "malhar" CSS puro.
- **Flexbox Froggy** e **Grid Garden** — jogos curtos e gratuitos que ensinam Flexbox e Grid de forma bem visual.
- **freeCodeCamp** — currículo gratuito completo com certificação, do zero a projetos maiores.
- **MDN Web Docs** — não é uma plataforma de exercícios, mas é a referência oficial que você vai consultar toda hora; vale o hábito de ler ali em vez de só copiar de fóruns.
- **JavaScript30** (Wes Bos, gratuito) — 30 projetos pequenos em JavaScript puro, muito bom para fixar DOM e eventos.

**Como praticar no VSCode:**
- Extensão **Live Server** — abre sua página com recarregamento automático a cada salvamento, sem configurar servidor.
- DevTools do navegador (F12) é sua ferramenta de debug número 1 para CSS/JS — acostume-se a inspecionar elementos e ver erros no console desde já.
