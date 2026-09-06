# ROTEIROS LÓGICOS PARA PRATICAR POO (PROGRAMAÇÃO ORIENTADA A OBJETOS)

## OS QUATRO PILARES (RESUMO RÁPIDO)
- **Encapsulamento**: esconder os detalhes internos de um objeto, expondo só o que é necessário via métodos.
- **Abstração**: focar no "o quê" um objeto faz, escondendo o "como" (classes abstratas, interfaces).
- **Herança**: uma classe filha reaproveita atributos e métodos de uma classe pai, podendo especializar comportamento.
- **Polimorfismo**: objetos de classes diferentes respondem de formas diferentes à mesma chamada de método.

## COMO USAR ESTE ROTEIRO
1. Antes de codar, desenhe um diagrama de classes simples (retângulos com nome, atributos e métodos, e linhas indicando herança/composição) — no papel, no draw.io/diagrams.net, ou em um diagrama Mermaid direto num arquivo `.md` do projeto.
2. Implemente uma classe por vez, testando isoladamente antes de conectar com as outras.
3. Pergunte-se sempre: "isso é um atributo (o que o objeto TEM) ou um método (o que o objeto FAZ)?"
4. Ao herdar, pergunte: "a subclasse realmente 'é um tipo de' superclasse?" Se a resposta for forçada, composição provavelmente é mais adequada.

-------------------------------------------------
CATEGORIA 1: CLASSES, OBJETOS E ATRIBUTOS
-------------------------------------------------

**1. CONTA BANCÁRIA (Encapsulamento básico)** (Fácil)
1. Defina a classe: crie `ContaBancaria` com atributos `titular` e `saldo`.
2. Construtor: ao criar a conta, exija o nome do titular; o saldo inicial deve começar em 0.
3. Encapsulamento: torne `saldo` privado; crie métodos `depositar(valor)` e `sacar(valor)`.
4. Regra de negócio: em `sacar`, verifique se há saldo suficiente antes de permitir a operação; caso contrário, recuse e informe o motivo.
5. Consulta: crie `consultarSaldo()` que retorna o saldo sem permitir alteração direta.

**2. CONTADOR DE INSTÂNCIAS (Atributo de Classe vs Instância)** (Fácil/Médio)
1. Cenário: modele `Produto` com atributos de instância `nome` e `preco`.
2. Atributo de classe: adicione um atributo compartilhado `quantidadeTotalDeProdutos`, começando em 0.
3. Incremento automático: a cada novo `Produto` criado (no construtor), incremente esse contador de classe.
4. Verificação: crie vários produtos e confirme que o contador é compartilhado entre todos os objetos, diferente dos atributos de instância (individuais de cada um).

-------------------------------------------------
CATEGORIA 2: HERANÇA E POLIMORFISMO
-------------------------------------------------

**3. HIERARQUIA DE VEÍCULOS (Herança Simples)** (Fácil/Médio)
1. Superclasse: crie `Veiculo` com `marca`, `modelo`, `velocidadeAtual` e método `acelerar()`.
2. Subclasses: crie `Carro` e `Moto`, que herdam de `Veiculo`.
3. Atributo específico: adicione um atributo exclusivo em cada subclasse (ex: `numeroDePortas` em Carro, `cilindradas` em Moto).
4. Reaproveitamento: use o construtor da superclasse (`super()`) para inicializar os atributos comuns dentro das subclasses.

**4. FORMAS GEOMÉTRICAS (Polimorfismo com Classe Abstrata)** (Médio)
1. Classe base: crie a classe abstrata `FormaGeometrica` com o método abstrato `calcularArea()` (sem implementação definida).
2. Implementações concretas: crie `Retangulo`, `Circulo` e `Triangulo`, cada uma implementando seu próprio cálculo de área.
3. Lista polimórfica: crie uma lista de `FormaGeometrica` contendo objetos de tipos concretos diferentes.
4. Teste: percorra a lista chamando `calcularArea()` em cada elemento — o mesmo código funciona para todas as formas, sem saber o tipo exato de cada uma.

**5. FORMAS DE PAGAMENTO (Interfaces / Contratos de Comportamento)** (Médio)
1. Interface: defina `Pagavel` com o método `processarPagamento(valor)`.
2. Múltipla implementação: crie `CartaoCredito`, `Boleto` e `Pix`, cada uma implementando a interface com sua própria lógica.
3. Diferença conceitual: registre em comentário por que aqui uma Interface faz mais sentido (comportamento sem estado compartilhado) do que uma Classe Abstrata (que guardaria atributos comuns).
4. Uso desacoplado: crie uma função `finalizarCompra(Pagavel formaDePagamento)` que aceita qualquer objeto que implemente `Pagavel`, sem saber qual é.

-------------------------------------------------
CATEGORIA 3: COMPOSIÇÃO E DESIGN
-------------------------------------------------

**6. CARRO E MOTOR (Composição: "tem um" vs "é um")** (Médio)
1. Cenário: modele `Motor` com atributos como `potencia` e `tipoCombustivel`.
2. Composição: `Carro` deve "ter um" `Motor` como atributo (não herdar dele).
3. Delegação: o método `ligar()` de `Carro` deve chamar internamente um método do objeto `Motor`.
4. Reflexão: pense em quando usar herança ("Carro é um Veículo") e quando usar composição ("Carro tem um Motor") — o que muda na flexibilidade do código.

**7. PROJETO INTEGRADOR: RPG DE TEXTO SIMPLES** (Difícil)
1. Classe base: crie a classe abstrata `Personagem` com `nome`, `vida`, `ataque` e o método abstrato `atacar(alvo)`.
2. Hierarquia: crie `Guerreiro`, `Mago` e `Arqueiro`, cada um com lógica de ataque diferente (ex: Mago gasta "mana").
3. Encapsulamento: a vida nunca deve ficar negativa; encapsule a redução de vida em `receberDano(valor)`.
4. Composição: dê a cada Personagem um `Inventario` (outra classe) que guarda uma lista de Itens.
5. Polimorfismo em ação: monte uma batalha entre personagens de tipos diferentes, chamando `atacar()` de forma genérica.
6. Encerramento: verifique a vida de cada personagem a cada turno e remova da batalha quem chegar a 0.

-------------------------------------------------
ONDE E COMO PRATICAR POO
-------------------------------------------------

- **Exercism** — trilhas de Java, Python, C#, Kotlin etc. com bastante exercício de modelagem e mentoria humana gratuita.
- **Codewars** — filtre por "Fundamentals" ou busque por "OOP"; tem bastante kata de modelagem de classes.
- **Refactoring.Guru** — depois de dominar o básico, é a referência para estudar Design Patterns (Factory, Strategy, Observer etc.), o passo natural seguinte depois de herança/polimorfismo.
- **Projeto próprio**: o mais eficiente para fixar POO costuma ser modelar um sistema pequeno seu (o RPG acima, um sistema de biblioteca, um cardápio de restaurante) e ir refatorando conforme aprende conceitos novos — mais fixador do que exercícios soltos.

**Como praticar no VSCode:**
- Esboce um diagrama de classes em Mermaid num arquivo `.md` junto do projeto antes de codar, para visualizar a hierarquia.
- Ative um linter (Pylint, ESLint etc.) — vários avisos (atributo não usado, método que deveria ser estático) ensinam boas práticas de POO na prática.
