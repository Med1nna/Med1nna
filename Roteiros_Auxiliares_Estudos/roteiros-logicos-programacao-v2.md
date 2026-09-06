# ROTEIROS LÓGICOS PARA EXERCÍCIOS DE PROGRAMAÇÃO — VERSÃO 2 (REVISADA E EXPANDIDA)

> O que mudou em relação à versão original: cada roteiro ganhou nível de dificuldade e complexidade (Big O); a ordem dentro de cada categoria agora vai do mais simples ao mais difícil; entraram exercícios que preenchem lacunas clássicas (DFS, Merge Sort, Quick Sort, pilha/parênteses balanceados, Kadane, subconjuntos); e no final tem uma seção real de "onde e como praticar".

## COMO USAR ESTE ROTEIRO

1. Leia o roteiro, mas não abra o editor ainda.
2. Escreva o algoritmo em pseudocódigo ou no papel antes de codar.
3. Implemente sem consultar solução pronta. Travar faz parte — é aí que a lógica fixa de verdade.
4. Teste com casos extremos: lista vazia, um único elemento, números negativos, entrada já ordenada.
5. Depois de funcionar, analise a complexidade — é isso que separa "funciona" de "é uma boa solução".
6. Volte no mesmo exercício alguns dias depois, sem olhar o que fez. Repetição espaçada fixa mais do que fazer 10 exercícios diferentes uma única vez.

-------------------------------------------------
CATEGORIA 1: RECURSIVIDADE
-------------------------------------------------

**1. CÁLCULO DE FATORIAL** (Fácil)
1. Defina a função: recebe um inteiro `n`.
2. Caso Base: se `n` for 0 ou 1, retorne 1.
3. Recursão: se `n > 1`, retorne `n` multiplicado pela função(`n - 1`).
- Complexidade: O(n).
- Dica: desenhe a pilha de chamadas para `n = 4` no papel antes de codar; ajuda a visualizar onde a recursão "volta".

**2. SOMA DOS DÍGITOS DE UM NÚMERO** (Fácil) — *novo*
1. Defina a função: recebe um inteiro positivo `n`.
2. Caso Base: se `n` tiver só um dígito (`n < 10`), retorne o próprio `n`.
3. Recursão: retorne o último dígito (`n % 10`) somado à chamada da função com o restante do número (`n // 10`).
- Complexidade: O(d), sendo d a quantidade de dígitos.

**3. SOMA DOS ELEMENTOS DE UMA LISTA** (Fácil/Médio)
1. Defina a função: recebe uma lista de números.
2. Caso Base: se a lista estiver vazia, a soma é 0.
3. Recursão: retorne o primeiro elemento somado à chamada da função passando o "resto" da lista.
- Complexidade: O(n).
- Dica: fatiar a lista a cada chamada (`lista[1:]`) tem custo de cópia em algumas linguagens; numa versão mais avançada, passe um índice em vez de fatiar.

**4. POTENCIAÇÃO RECURSIVA** (Médio)
1. Defina a função: recebe `base` e `expoente`.
2. Caso Base: se `expoente == 0`, retorne 1.
3. Recursão: se `expoente > 0`, retorne `base` multiplicada pela função(`base`, `expoente - 1`).
- Complexidade: O(n) na versão simples.
- Desafio extra: implemente a exponenciação rápida, dividindo o expoente por 2 a cada chamada em vez de subtrair 1 — cai para O(log n).

**5. SEQUÊNCIA DE FIBONACCI** (Médio)
1. Defina a função: recebe a posição `n`.
2. Casos Base: se `n = 0`, retorna 0; se `n = 1`, retorna 1.
3. Dupla Recursão: se `n > 1`, retorne função(`n - 1`) + função(`n - 2`).
- Complexidade: O(2^n) na versão ingênua — recalcula os mesmos valores várias vezes.
- Desafio extra: implemente memoização (cache dos resultados já calculados) e veja a complexidade cair para O(n). É a porta de entrada para Programação Dinâmica.

**6. TORRE DE HANÓI** (Difícil)
1. Defina a função: precisa de `n` discos e três pinos (origem, destino, auxiliar).
2. Caso Base: se `n = 1`, mova da origem para o destino e encerre.
3. Primeira Recursão: se `n > 1`, mova `n-1` discos da origem para o auxiliar.
4. Ação Principal: mova o maior disco da origem para o destino.
5. Segunda Recursão: mova os `n-1` discos do auxiliar para o destino.
- Complexidade: O(2^n) movimentos — é o mínimo matematicamente necessário.

-------------------------------------------------
CATEGORIA 2: BUSCA E OTIMIZAÇÃO
-------------------------------------------------

**1. BUSCA LINEAR (Sequencial)** (Fácil)
1. O Loop: percorra a lista do índice 0 até o último.
2. A Checagem: em cada passo, "esse é o item que eu procuro?".
3. Sucesso: se for igual, retorne o índice atual.
4. Falha: se o loop terminar sem achar, retorne -1.
- Complexidade: O(n).

**2. BUSCA BINÁRIA** (Médio)
- Requisito: lista precisa estar em ordem crescente.
1. Fronteiras: `inicio` (0) e `fim` (tamanho - 1).
2. Loop: enquanto `inicio <= fim`.
3. Meio: calcule o índice do meio e veja o valor.
4. Opções: achou → retorne a posição; é menor → `fim = meio - 1`; é maior → `inicio = meio + 1`.
- Complexidade: O(log n).
- Atenção: só funciona em lista ordenada — em lista desordenada o resultado é indefinido.

**3. BUSCA EM PROFUNDIDADE (DFS)** (Médio) — *novo*
- Ideal para explorar todos os caminhos possíveis ou checar se existe conexão entre dois pontos.
1. A pilha (ou recursão): comece pelo ponto de partida, usando uma pilha explícita ou a própria pilha de chamadas.
2. Controle de repetição: marque cada ponto como "visitado" assim que for processado.
3. Exploração: visite um vizinho não visitado e aprofunde-se o máximo possível antes de voltar (backtrack) para tentar outro caminho.
4. Comparação: depois de pronto, compare a ordem de visita entre DFS e BFS no mesmo grafo — BFS "espalha", DFS "aprofunda".
- Complexidade: O(V + E).

**4. BUSCA EM LARGURA (BFS)** (Médio)
- Ideal para encontrar a rota mais curta em redes/grafos não ponderados.
1. A Fila: crie uma fila e coloque o ponto de partida nela.
2. Controle de repetição: crie uma lista/conjunto de "visitados".
3. Loop de Expansão: enquanto a fila não estiver vazia, tire o primeiro item.
4. Verificação: é o destino? Retorne o caminho até aqui.
5. Vizinhos: senão, pegue os vizinhos ainda não visitados, adicione-os no fim da fila e marque-os como visitados.
- Complexidade: O(V + E).

-------------------------------------------------
CATEGORIA 3: ALGORITMOS DE ORDENAÇÃO
-------------------------------------------------

**1. BUBBLE SORT** (Fácil)
1. Loop Externo: roda uma quantidade de vezes igual ao tamanho da lista.
2. Loop Interno: passa do começo até o limite dos já ordenados.
3. Troca: se o item atual for maior que o da direita, troque-os.
4. Otimização: se um loop interno inteiro passar sem trocar nada, pare (já ordenou).
- Complexidade: O(n²) pior caso, O(n) melhor caso (com a otimização).

**2. SELECTION SORT** (Fácil)
1. Loop de Posições: percorra a lista do início ao fim; o índice atual é o "alvo".
2. Buscando o Menor: do "alvo" até o final, ache o menor número.
3. A Troca Única: troque o menor encontrado com a posição "alvo".
4. Repetição: avance o "alvo". Os menores vão se acumulando no começo.
- Complexidade: O(n²) sempre, mesmo com entrada já ordenada.

**3. INSERTION SORT** (Fácil/Médio)
1. A Premissa: a primeira carta já está "ordenada".
2. Selecionando: a partir da segunda posição, guarde o valor atual em uma "chave".
3. O Recuo: enquanto os números à esquerda forem maiores que a chave, empurre-os uma posição à direita.
4. A Inserção: encontrado um número menor (ou o início), coloque a chave no espaço livre.
- Complexidade: O(n²) pior caso, mas O(n) se a lista já estiver quase ordenada — o mais eficiente dos três "simples" nesse cenário.

**4. MERGE SORT** (Médio/Difícil) — *novo*
- Estratégia "dividir para conquistar".
1. Caso Base: lista com 0 ou 1 elemento já está ordenada.
2. Divisão: corte a lista ao meio, gerando duas metades.
3. Conquista: chame o próprio Merge Sort para ordenar cada metade separadamente.
4. Combinação (Merge): una as duas metades ordenadas comparando sempre o menor elemento de cada uma.
- Complexidade: O(n log n) sempre, independente da entrada.

**5. QUICK SORT** (Médio/Difícil) — *novo*
1. Escolha do Pivô: selecione um elemento (primeiro, último ou aleatório).
2. Particionamento: rearranje a lista para que os menores que o pivô fiquem à esquerda e os maiores à direita.
3. Recursão: aplique o mesmo processo nas sublistas da esquerda e da direita.
4. Caso Base: sublista com 0 ou 1 elemento já está ordenada.
- Complexidade: O(n log n) em média, O(n²) no pior caso — por isso a escolha do pivô importa.

-------------------------------------------------
CATEGORIA 4: LÓGICA DE POSIÇÃO E MANIPULAÇÃO
-------------------------------------------------

**1. VERIFICADOR DE PALÍNDROMOS** (Fácil)
1. Tratamento: remova espaços e use só letras minúsculas.
2. Ponteiros: `esquerda` (0) e `direita` (último índice).
3. Loop: enquanto `esquerda < direita`.
4. Teste: se as letras forem diferentes, retorne Falso.
5. Avanço: se iguais, `esquerda + 1`, `direita - 1`.
6. Sucesso: se o loop terminar, retorne Verdadeiro.
- Complexidade: O(n).

**2. INVERSÃO DE ARRAY / LISTA (In-place)** (Fácil)
1. Ponteiros: `inicio` (0) e `fim` (último índice).
2. Loop: enquanto `inicio < fim`.
3. Troca: troque o valor de `inicio` com o de `fim`.
4. Encontro: avance `inicio` (+1), recue `fim` (-1). Quando se cruzarem, a lista está invertida.
- Complexidade: O(n).

**3. VERIFICAÇÃO DE PARÊNTESES BALANCEADOS** (Médio) — *novo, usa Pilha (Stack)*
1. Estrutura: crie uma pilha vazia.
2. Percorra a string: símbolo de abertura `( [ {` → empilhe.
3. Fechamento: símbolo de fechamento → verifique se o topo da pilha é o par correspondente; se sim, desempilhe; se não (ou pilha vazia), é inválido.
4. Verificação final: pilha vazia no fim → balanceado; sobrou algo → inválido.
- Complexidade: O(n).
- Por que importa: é um dos exercícios mais cobrados em entrevistas e a porta de entrada natural para a estrutura de dados Pilha.

**4. SOMA DE DOIS ALVOS (Two Sum com Dois Ponteiros)** (Médio)
- Requisito: array ordenado.
1. Ponteiros: `esq` no começo, `dir` no fim.
2. Loop: enquanto `esq < dir`.
3. Soma: `array[esq] + array[dir]`.
4. Ajuste: igual ao alvo → retorne; menor → avance `esq`; maior → recue `dir`.
- Complexidade: O(n) — bem melhor que testar todos os pares, O(n²).

**5. MAIOR SOMA DE SUBSEQUÊNCIA CONTÍGUA (Algoritmo de Kadane)** (Médio/Difícil) — *novo*
1. Variáveis: `somaAtual` e `melhorSoma`, ambas iniciando com o primeiro elemento.
2. Percorra a lista a partir do segundo elemento.
3. Decisão: para cada elemento, `somaAtual = máximo(elemento sozinho, somaAtual + elemento)`.
4. Atualização: se `somaAtual > melhorSoma`, atualize `melhorSoma`.
5. Resultado: ao final, `melhorSoma` é a resposta.
- Complexidade: O(n) — surpreendente para um problema que parece exigir testar todas as combinações.

-------------------------------------------------
CATEGORIA 5: BACKTRACKING E CAMINHOS
-------------------------------------------------

**1. GERADOR DE SUBCONJUNTOS (Power Set)** (Médio) — *novo, aquecimento antes de Permutações*
1. Estado: uma lista para o subconjunto sendo formado e o índice do próximo elemento a considerar.
2. Caso Base: índice passou do último elemento → salve/imprima o subconjunto atual (mesmo vazio).
3. As Duas Escolhas: para o elemento atual, existem sempre 2 caminhos: incluí-lo ou não incluí-lo.
4. Backtrack: explore os dois ramos (com e sem o elemento), desfazendo a escolha entre um e outro.
- Complexidade: O(2^n) — existem exatamente 2^n subconjuntos possíveis.

**2. RESOLVEDOR DE LABIRINTOS** (Difícil)
1. Parâmetro: matriz e coordenada X, Y.
2. Falha: fora do mapa, parede ou já visitado → retorne Falso.
3. Sucesso: é a saída → retorne Verdadeiro.
4. Migalha: marque X, Y como "visitado".
5. Tentativas: chame recursivamente para Cima, Baixo, Esquerda, Direita.
6. Backtrack: se nenhum vizinho retornar Verdadeiro, desmarque X, Y e retorne Falso.

**3. O PROBLEMA DAS N-RAINHAS** (Difícil)
1. Parâmetro: a linha atual onde você tenta colocar uma rainha.
2. Caso Base: passou da última linha → posicionou todas!
3. Loop das Colunas: na linha atual, tente a primeira coluna.
4. Verificação: existe rainha na mesma coluna ou diagonal? Se sim, tente a próxima coluna.
5. Backtracking: se seguro, posicione e recorra para a próxima linha; se falhar, tire a rainha e tente a próxima coluna.

**4. GERADOR DE PERMUTAÇÕES** (Difícil)
1. Estado: a string/lista sendo formada e os itens ainda disponíveis.
2. Caso Base: string do mesmo tamanho da original → salve/imprima e retorne.
3. Loop de Escolhas: para cada item disponível ainda não usado:
4. Escolha e Backtrack: adicione o item, explore recursivamente, depois remova-o e marque como livre novamente.

-------------------------------------------------
ONDE E COMO PRATICAR — LÓGICA E ALGORITMOS
-------------------------------------------------

- **Beecrowd** (ex-URI Online Judge) — plataforma brasileira, mais de mil problemas em português, organizados por categoria e nível. Ótima para fixar lógica pura em várias linguagens.
- **VisuAlgo** (visualgo.net) — visualiza passo a passo algoritmos de ordenação, busca, grafos e recursão. Use depois de implementar para conferir se seu entendimento bate com a execução real.
- **LeetCode** — o mais usado para treino estilo entrevista técnica; filtro por assunto (arrays, recursão, DP, grafos) e por dificuldade.
- **HackerRank** — parecido, com trilhas de "Problem Solving" separadas por estrutura de dados.
- **Codewars** — desafios em formato "kata"; depois de resolver, você vê as soluções de outras pessoas — ótimo para aprender formas diferentes de pensar o mesmo problema.
- **Exercism** — trilhas por linguagem com mentoria humana gratuita e feedback real sobre o código, não só "passou/não passou".
- **Curso em Vídeo** (Gustavo Guanabara) — se a lógica de alguma categoria não fizer sentido, os cursos de Lógica de Programação e Python dele (em português) são uma ótima base para revisar do zero.

**Como praticar pelo VSCode:**
- Crie uma pasta `roteiros-logica` com uma subpasta por categoria.
- Use a extensão **Code Runner** para rodar o arquivo com um atalho, sem abrir terminal toda vez.
- Escreva testes simples com `assert` no fim de cada arquivo (ex: `assert fatorial(5) == 120`) — dá feedback imediato se algo quebrar ao tentar otimizar depois.
