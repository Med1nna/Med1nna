# 🏆 Guia de Preparação para Entrevistas em Programação

Este documento lista 30 exemplos reais de perguntas e desafios cobrados em entrevistas técnicas para desenvolvedores, divididos nas três categorias principais de avaliação.

---

## 💻 1. Algoritmos e Estruturas de Dados (Live Coding)
*Estes testes avaliam a sua capacidade de pensar de forma lógica, otimizar código e conhecer as estruturas nativas da linguagem.*

1. **FizzBuzz:** Escrever um loop que imprime números de 1 a 100, mas substitui múltiplos de 3 por "Fizz", múltiplos de 5 por "Buzz" e de ambos por "FizzBuzz".
2. **Two Sum (Soma de Dois):** Dado um array de números e um número-alvo, retorne os índices dos dois números que somados resultam no alvo (espera-se o uso de Hash Maps para otimização).
3. **Validação de Parênteses (Balanced Brackets):** Checar se uma string com `{ [ ( ) ] }` está fechando os pares na ordem correta usando a estrutura de Pilha (Stack).
4. **Verificador de Anagramas:** Identificar se duas palavras possuem exatamente as mesmas letras na mesma quantidade.
5. **Inversão de String / Palíndromo:** Criar uma lógica in-place (usando dois ponteiros) para inverter um texto ou checar se ele é lido igual de trás para frente.
6. **Remoção de Duplicatas:** Remover itens repetidos de uma lista sem criar uma lista nova na memória, ou usando a estrutura de `Set`.
7. **Busca Binária (Binary Search):** Encontrar um elemento específico dentro de um array ordenado reduzindo a área de busca pela metade a cada iteração.
8. **Maior Subarray Contíguo (Algoritmo de Kadane):** Encontrar a sequência de números consecutivos dentro de uma lista que gera a soma máxima.
9. **Mesclagem de Intervalos (Merge Intervals):** Dada uma lista de horários de reunião (ex: 09:00-10:30 e 10:00-11:00), mesclar os horários que se sobrepõem.
10. **Inversão de Lista Encadeada (Linked List):** Manipular os ponteiros (`next`) de nós em uma estrutura de dados de lista ligada para inverter a direção de todos os elementos.

---

## ⚙️ 2. Situações-Problema de Engenharia e Automação
*Perguntas de arquitetura onde os recrutadores avaliam como você constrói sistemas robustos no mundo real, lidando com erros, bases de dados e integrações.*

1. **A Quebra de Seletores (Web Scraping):** Como você garante que sua automação continue funcionando se o desenvolvedor do site alterar a estrutura HTML e quebrar o seu XPath?
2. **Paginação Profunda e Limites:** Como você extrai 10.000 registros de uma API cuja documentação só permite buscar 50 itens por página?
3. **Rate Limiting (429 Too Many Requests):** O servidor bloqueou seu robô por excesso de requisições. Como implementar lógicas de "Exponential Backoff" (espera progressiva) para tentar novamente sem derrubar o site?
4. **Idempotência de Execução:** Se a energia cair e o seu robô rodar duas vezes no mesmo dia, como garantir que ele não fará um pagamento em duplicidade no banco de dados?
5. **Gerenciamento de Credenciais Sensíveis:** Como você estrutura seu projeto para que senhas e chaves de API nunca vazem no GitHub? (Uso de variáveis de ambiente, arquivos `.env`, Key Vaults).
6. **Lidando com Dados Sujos e Não Padronizados:** Como você captura e sanitiza 1.000 planilhas onde a coluna "Valor" mistura números reais, letras e casas decimais separadas por pontos e vírgulas? (Uso de Regex).
7. **Captchas e Bloqueios (Anti-Bot):** Como sua arquitetura contorna proteções como Cloudflare, bloqueios de IP geográficos ou reCAPTCHAs em fluxos de RPA críticos?
8. **Arquitetura de Filas e Paralelismo:** Você tem 50.000 URLs para raspar. Como dividir o trabalho usando Filas (RabbitMQ/Celery) para que múltiplos robôs trabalhem em paralelo?
9. **Deadlocks no Banco de Dados:** O que você faz se o seu script de inserção travar porque dois processos estão tentando atualizar a mesma tabela no banco SQL simultaneamente?
10. **Monitoramento e Alerta Automático:** É sexta-feira à noite e a automação falhou silenciosamente. O que você deveria ter implementado para que a equipe fosse avisada a tempo do erro?

---

## 🗣️ 3. Entrevista Comportamental (Metodologia STAR)
*Perguntas não técnicas focadas nas suas "Soft Skills" (Situação, Tarefa, Ação e Resultado).*

1. **O Bug Crítico em Produção:** "Me conte sobre uma vez em que um código seu subiu com erro e quebrou o processo em produção. Como você descobriu e o que fez?"
2. **Discordância Técnica:** "Descreva uma situação em que você discordou totalmente da abordagem técnica de um colega mais sênior. Como você conduziu o debate?"
3. **Prazos Impossíveis:** "Quando percebeu que a entrega não caberia no prazo estipulado, como você negociou a priorização de tarefas com a área de negócios?"
4. **Curva de Aprendizado Acelerada:** "Me dê um exemplo de um projeto onde você teve que aprender uma linguagem ou ferramenta completamente do zero em poucos dias."
5. **Comunicação com Stakeholders Não-Técnicos:** "Como você explicou um problema sistêmico complexo de infraestrutura para um cliente ou gerente que não entende nada de programação?"
6. **A Iniciativa (Ownership):** "Conte sobre um momento em que você automatizou ou melhorou um processo que ninguém havia pedido, apenas porque percebeu que precisava ser feito."
7. **O Requisito Incompreendido:** "Descreva uma vez em que você entregou exatamente o que foi pedido, mas descobriu na apresentação que não era o que o cliente realmente precisava."
8. **Lidando com Feedback Negativo:** "Fale sobre uma revisão de código (Code Review) rigorosa ou uma avaliação de desempenho onde apontaram falhas suas. Como você reagiu?"
9. **Mentoria e Colaboração:** "Houve alguma ocasião em que você precisou pausar o seu próprio trabalho urgente para ajudar um colega júnior que estava travado?"
10. **Decisão em Meio à Incerteza:** "Fale sobre uma ocasião em que você teve que escolher uma arquitetura ou ferramenta de desenvolvimento, mas não tinha todos os dados ou informações claras no momento. Como mitigou o risco?"
