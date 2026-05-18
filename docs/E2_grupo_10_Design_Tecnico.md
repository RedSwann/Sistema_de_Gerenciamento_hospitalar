# Design Técnico e MVP — E2
**Estrutura de Dados**
**Prazo:** 14/05 | **Peso na nota:** 25% da nota final

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Sistema de gerenciamento hospitalar - HealthCore|
| Repositório GitHub | https://github.com/RedSwann/Sistema_de_Gerenciamento_hospitalar |
| Integrante 1 | Breno Ribeiro— 41751809 |
| Integrante 2 | Renata Mayumi Iuvata — 43070981 |

---

## 1. Escolha e Justificativa das Estruturas de Dados

> Preencha um bloco por estrutura escolhida (mínimo 1, máximo 3).
> Copie o bloco abaixo quantas vezes forem necessárias.

---

### Estrutura 1 — [ Lista ]

**Nome completo e categoria:**
Lista Encadeada Simples Ordenada - estrutura linear dinâmica 

**Complexidade das operações principais:**

| Operação | Tempo | Espaço | Observação |
|----------|-------|--------|------------|
| Inserção | O(n) | O(1) | Os pacientes são inseridos ao final ou de forma ordenada|
| Remoção  | O(n) | O(1) | É necessário percorrer a lista para encontrar o cpf|
| Busca    | O(n) | O(1) | Busca linear por CPF percorrendo os nós|
| Acesso   | O(n) | O(1) | 	Não possui acesso direto aos elementos da lista|

**Justificativa de escolha:**
A lista encadeada simples ordenada foi utilizada para armazenar os pacientes em ordem alfabética, facilitando a visualização e organização dos registros no sistema. A estrutura permite inserções dinâmicas sem necessidade de realocação de memória.

**Alternativa descartada:**
Lista Duplamente Encadeada — descartada porque o sistema não necessita navegação bidirecional entre os registros, tornando a estrutura mais complexa e com maior consumo de memória sem necessidade.

**Limitações conhecidas:**
As operações de busca, inserção e remoção possuem complexidade O(n), pois em muitos casos é necessário percorrer parte ou toda a lista para localizar a posição desejada.

**Referência bibliográfica:**
AMOASEI, J. O que são estruturas de dados? Uma introdução a estruturas de dados e algoritmos na programação. ALURA, 2026.

---

### Estrutura 2 — [Fila ] *(se houver)*

**Nome completo e categoria:**
Fila de prioridade  - Estrutura linear dinâmica

**Complexidade das operações principais:**

| Operação |   Tempo  | Espaço | Observação |
|----------|----------|--------|------------|
| Inserção | O(n) | O(1) | O sistema percorre a fila para inserir o nó na posição correta|
| Remoção  | O(1) | O(1) | O sistema remove sempre o primeiro nó|
| Busca    | O(n) | O(1) | Verificação de duplicidade exige o percurso completo |
| Acesso   | O(1) | O(1) | O proximo paciente a ser atendido sempre esta no topo da estrutura.|

**Justificativa de escolha:**
A fila de prioridade foi escolhida para organizar os atendimentos conforme a gravidade e o tempo de espera dos pacientes. Dessa forma, casos mais urgentes recebem prioridade sem que pacientes de menor prioridade permaneçam muito tempo na fila, tornando o sistema mais eficiente e equilibrado.

**Alternativa descartada:**
Fila simples FIFO — descartada porque não permite priorização de pacientes em estado grave.

**Limitações conhecidas:**
As operações de inserção e remoção exigem reorganização da fila conforme a prioridade dos pacientes.

**Referência bibliográfica:**
PYTHON SOFTWARE FOUNDATION. heapq — Heap queue algorithm. Python Documentation, 2026. Disponível em: <https://docs.python.org/3/library/heapq.html> 
---

### Estrutura 3 — [ Pilha ] 

**Nome completo e categoria:**
Pilha de Ações - estrutura linear dinâmica 

**Complexidade das operações principais:**

| Operação | Tempo | Espaço | Observação |
|----------|-------|--------|------------|
| Inserção | O(1) | O(1) | Inserção no topo da pilha|
| Remoção  | O(1) | O(1) | Remove o último elemento inserido|
| Busca    | O(n) | O(1) | É necessário percorrer os elementos|
| Acesso   | O(1) | O(1) | Acesso direto ao topo|

**Justificativa de escolha:**
A pilha foi escolhida para implementar o desfazer ações no sistema, pois segue a lógica LIFO, permitindo recuperar rapidamente a última ação realizada pelo usuário.
**Alternativa descartada:**
Fila - descartada porque o sistema precisa desfazer a ação mais recente primeiro. Uma fila removeria as ações mais antigas antes das recentes, o que não corresponde ao comportamento esperado da funcionalidade de desfazer.
**Limitações conhecidas:**
A pilha permite desfazer apenas a última ação realizada e possui busca linear O(n). Além disso, o uso contínuo pode aumentar o consumo de memória do sistema.
**Referência bibliográfica:**
UNIVERSIDADE DE SÃO PAULO (USP). Pilhas. Instituto de Matemática e Estatística, 2026. Disponível em: <https://www.ime.usp.br/~pf/algoritmos/aulas/pilha.html>
---

## 2. Arquitetura em Camadas

**Diagrama:**
```
╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                     CAMADA DE APRESENTAÇÃO (UI/CLI)                               ║
║               ┌─────────────────┐  ┌────────────────────┐  ┌──────────────────┐                   ║
║               │  Menu Principal │  │  Cadastro Pac.     │  │  Fila Atendimento│                   ║
║               │                 │  │                    │  │                  │                   ║
║               │ • Cadastrar     │  │ • Nome             │  │ • Visualizar     │                   ║
║               │ • Fila          │  │ • Idade            │  │ • Chamar Próx.   │                   ║
║               │                 │  │ • CPF              │  │ • Remover        │                   ║
║               │                 │  │ • Telefone         │  │ • Atualizar      │                   ║
║               │                 │  │ • portador de      │  │                  │                   ║
║               │                 │  │   deficiencia      │  │                  │                   ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝
                                              │
                                              ▼ Chamadas de Métodos
                  ╔═══════════════════════════════════════════════════════════════════╗
                  ║                      CAMADA DE APLICAÇÃO (Service)                ║
                  ║  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ║
                  ║  │PacienteService  │  │AtendimentoService│  │PrioridadeService │  ║
                  ║  │                 │  │                  │  │                  │  ║
                  ║  │ +cadastrar()    │  │ +adicionarFila() │  │ +calcular()      │  ║
                  ║  │ +buscar()       │  │ +chamarProximo() │  │ +reorganizar()   │  ║
                  ║  │ +validar()      │  │ +remover()       │  │ +atualizarTempo()│  ║
                  ║  │ +listar()       │  │ +listar()        │  │ +verificar()     │  ║
                  ║  │ +atualizar()    │  │                  │  │                  │  ║
                  ║  └─────────────────┘  └──────────────────┘  └──────────────────┘  ║
                  ╚═══════════════════════════════════════════════════════════════════╝
                                              │
                                              ▼ Manipulação de Dados
                  ╔══════════════════════════════════════════════════════════════════╗
                  ║                      CAMADA DE DOMÍNIO (Core)                    ║
                  ║  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐   ║
                  ║  │  ListaEncadeada │  │ FilaPrioridade  │  │     Pilha       │   ║
                  ║  │                 │  │                 │  │                 │   ║
                  ║  │ +inserir()      │  │ +enqueue()      │  │ +push()         │   ║
                  ║  │ +remover()      │  │ +dequeue()      │  │ +pop()          │   ║
                  ║  │ +buscar()       │  │ +peek()         │  │ +top()          │   ║
                  ║  │ +percorrer()    │  │ +reorganizar()  │  │ +isEmpty()      │   ║
                  ║  │ +ordenar()      │  │ +priorizar()    │  │ +size()         │   ║
                  ║  └─────────────────┘  └─────────────────┘  └─────────────────┘   ║
                  ╚══════════════════════════════════════════════════════════════════╝


```

**Descrição das camadas:**

| Camada                | Nome no seu projeto                                                             | Responsabilidade |
|-----------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Apresentação (UI/CLI) | Menu Principal, Cadastro de Pacientes, Fila de Atendimento | Realiza a interação com o usuário através de menus/telas, recebendo dados digitados e exibindo informações do sistema.|

| Aplicação (Service)   | PacienteService, AtendimentoService e PrioridadeService                         | Controla as regras de negócio, valida os dados recebidos da interface e coordena as operações realizadas nas estruturas de dados. |

| Domínio (Core)        | Lista Encadeada, FilaPrioridade e Pilha                                         | Implementa as estruturas de dados principais do sistema e executa operações como inserção, remoção, organização da fila e armazenamento das últimas ações. |

**Como as camadas se comunicam:**
Primeiramente, a camada de apresentação (UI/CLI) recebe as informações digitadas pelo usuário, como cadastro de paciente(nome, cpf, idade, telefone e se possui alguma deficiência). Essas informações são enviadas para a camada de aplicação (Service), responsável por validar os dados e definir qual operação deve ser executada. Após a validação, o Service chama os métodos da camada de domínio (Core), onde estão implementadas as estruturas de dados do sistema.
---

## 3. Estrutura de Diretórios

```
/
├── src/
│   └── core/
│       ├── fila_atendimento.py
│       ├── paciente.py
│       └── pilha_acoes.py
│   └── service/
│           fila_service.py
│           paciente_service.py
│   └── ui/  
│       ├── menu_fila.py
│       ├── menu_cadastro.py
│       └── menu_inicial.py
├── tests
│      test_fila.py
│      test_paciente.py
│      test_pilha.py
└── README.md
```

**Justificativa de desvios (se houver):**
Sem desvios

---

## 4. Backlog do Projeto

### In-Scope — O que será implementado

> Mínimo 5 itens. Cada item deve ter um critério de aceite no formato Dado / Quando / Então.

---

**Item 1:** [Nome curto da funcionalidade] Cadastro de pacientes

Critério de aceite:
Dado um usuário preenchendo nome, idade, CPF e gênero, quando o cadastro for confirmado, então o sistema deve inserir o paciente na ListaEncadeada utilizando inserir() e exibir a confirmação do cadastro.

---

**Item 2:** busca de pacientes 

Critério de aceite:
Dado pacientes cadastrados na ListaEncadeada, quando o usuário pesquisar um CPF, então o sistema deve localizar o paciente utilizando buscar() e exibir seus dados na tela.

---

**Item 3:** Organização da fila de atendimento

Critério de aceite:
Dado múltiplos pacientes com diferentes níveis de emergência, quando um novo paciente entrar na fila, então a FilaPrioridade deve reorganizar os pacientes utilizando priorizar() e reorganizar().


---

**Item 4:** Chamada de pacientes

Critério de aceite:
Dado uma fila contendo pacientes aguardando atendimento, quando o usuário executar “Chamar Próximo”, então o sistema deve remover o primeiro paciente da FilaPrioridade utilizando dequeue() e exibir seus dados.

---

**Item 5:** Remoção de pacientes da fila

Critério de aceite:
Dado uma fila contendo pacientes aguardando atendimento, quando o usuário solicitar a remoção de um paciente, então o sistema deve removê-lo da FilaPrioridade utilizando dequeue() ou remover() e atualizar a ordem da fila.

---

**Item 6:** Visualização da fila

Critério de aceite:
Dado um histórico de ações armazenado na pilha, quando o usuário clicar em “Desfazer”, então o sistema deve remover a última ação registrada utilizando pop() e restaurar o estado anterior da operação realizada.

---
**Item 7:** Desfazer última ação

Critério de aceite:
Dado um paciente já cadastrado na ListaEncadeada, quando o usuário atualizar suas informações, então o sistema deve localizar o registro utilizando buscar() e alterar os dados armazenados.

---

### Out-of-Scope — O que não será implementado

| Funcionalidade | Motivo de exclusão |
|----------------|--------------------|
| Controle financeiro e faturamento      | Funcionalidades relacionadas a pagamentos, convênios e emissão de cobranças não agrega ao aprendizado do conteúdo de ED. |
| Histórico médico completo dos pacientes| Tem uma complexidade de implementação elevada. O sistema armazenará apenas informações necessárias para o atendimento atual e gerenciamento da fila |
| Aplicação em nuvem                     |Fora do escopo do semestre e alta complexidade de implementação. O projeto será executado localmente, sem hospedagem online.|

---

## 5. Repositório GitHub

**Link do repositório:** [https://github.com/RedSwann/Sistema_de_Gerenciamento_hospitalar]

**Checklist do repositório:**

- [ ✔ ] Repositório público com nome descritivo
- [ ✔ ] `.gitignore` configurado para a linguagem escolhida
- [ ✔ ] `README.md` com nome, descrição e instruções de execução
- [ ✔ ] Mínimo de 5 commits com prefixos semânticos (`feat:`, `fix:`, `test:`, `docs:`, `refactor:`)

**O que não deve subir no repositório**:

Variáveis de ambiente → .env, .env.local
Credenciais e chaves → secrets.json, arquivos de certificado
Dependências → node_modules/, venv/
Builds gerados → dist/, build/
Arquivos do sistema → .DS_Store, Thumbs.db
Logs → *.log

**Como executar o projeto** *(resumo — o completo deve estar no README.md)*:

```
[Criamos um executavel .bat que roda o seguinte comando:
  cd /d "%~dp0"
py -m streamlit run menu.py
]
```

---

## 6. Implementação do Núcleo

### 6.1 Estrutura implementada: Fila prioritaria

**Linguagem:** Python 3.11

**Localização no repositório:** `src/core/fila_prioritaria.py`

**Operações implementadas:**

| Operação | Implementada? | Observação |
|----------|---------------|------------|
| adicionar| ✅            | Insere pacientes na fila conforme a pontuação de prioridade|
| proximo  | ✅            | Remove o primeiro paciente da fila|
| remover  | ✅            | Remove um paciente específico da fila |
| atualizar| ✅            | Atualiza o tempo de espera e recalcula prioridades|
| verificar vazio| ✅      | Verifica se existe pacientes na fila para serem chamados|


**Trecho representativo do código** *(operação principal)*:


Esse trecho representa a principal lógica da fila de prioridade, responsável por inserir os pacientes na posição correta de acordo com a pontuação calculada pelo sistema.

INSERÇÃO ORDENADA POR PRIORIDADE
def _inserir_ordenado(self, inicio, novo):

    if not inicio or novo.pontuacao > inicio.pontuacao:
        novo.proximo = inicio
        return novo

    atual = inicio

    while atual.proximo and atual.proximo.pontuacao >= novo.pontuacao:
        atual = atual.proximo

    novo.proximo = atual.proximo
    atual.proximo = novo

    return inicio

---
 
### 6.2 Estrutura implementada: Fila prioritaria
Linguagem: Python 3.11
Localização no repositório: src/core/pilha_navegacao.py

**Operações implementadas:**

| Operação | Implementada? | Observação |
|----------|---------------|------------|
| adicionar| ✅            | Adiciona novos pacientes na lista de cadastrados|
| buscar   | ✅            | Procura pacientes pelo CPF|
| remover  | ✅            | Remove pacientes cadastrados |
| editar   | ✅            | Edita a informações do paciente|
| verificar vazio| ✅      | Verifica se existem pacientes cadastrados|
| listar   | ✅            | Exibe todos os pacientes cadastrados|

**Trecho representativo do código** *(operação principal)*:
Esse trecho representa a principal lógica da lista de pacientes, responsável por armazenar os pacientes cadastrados no sistema para posterior consulta e utilização.

#ADIÇÃO DE PACIENTES NA LISTA

def adicionar_paciente(self, paciente):

    self.pacientes.append(paciente)

    return {
        "mensagem": "Paciente cadastrado com sucesso."
    }


**Leitura de arquivo:**
O sistema realiza a leitura de dados utilizando arquivos no formato JSON. 
Os arquivos são armazenados na pasta `data/`, sendo o principal arquivo utilizado `data/pacientes.json`.
A estrutura do arquivo consiste em uma lista de objetos JSON, onde cada objeto representa um paciente contendo os seguintes campos:
- nome
- cpf
- idade
- telefone
- deficiencia

Exemplo de arquivo de entrada (`data/pacientes.json`):
[
  {
    "nome": "Mariana Souza",
    "cpf": "12345678900",
    "idade": 68,
    "telefone": "(11) 99999-9999",
    "deficiencia": "Sim"
  }
]

### 6.3 Estrutura implementada: Pilha
Linguagem: Python 3.11
Localização no repositório: src/core/pilha_navegacao.py

**Operações implementadas:**

| Operação | Implementada? | Observação |
|----------|---------------|------------|
| push| ✅                 | Adiciona uma ação realizada ao topo da pilha|
| pop  | ✅                | Remove a última ação realizada|
| topo  | ✅               | Retorna a última ação registrada |
| verificar vazio| ✅      | Verifica se existe alguma ação armazenada|

**Trecho representativo do código** *(operação principal)*:
Esse trecho representa a principal lógica da pilha de ações, responsável por armazenar o histórico de operações realizadas no sistema seguindo o conceito LIFO (Last In, First Out), permitindo desfazer a última ação executada.

EMPILHAR AÇÕES REALIZADAS
def push(self, acao):

    self.historico.append(acao)

    return {
        "mensagem": f"Ação '{acao}' adicionada ao histórico."
    }



## 7. MVP — Mínimo Produto Viável

### 7.1 Tipo de interface

- [ ] CLI (linha de comando)
- [✔] GUI desktop (Tkinter, JavaFX, outro: Streamlit)
- [ ] Web (HTML/JS, outro: __________)

### 7.2 Tela 1 — Boas-vindas / Menu Principal

**Descrição:** 
A tela inicial do sistema funciona como um menu de navegação principal. Nela, o usuário pode escolher entre acessar o banco de pacientes ou visualizar a fila de atendimento. Essa tela centraliza as funcionalidades do sistema e facilita a navegação entre as operações disponíveis.
```
[Cole aqui um print da tela ou uma representação ASCII do que é exibido]

┌──────────────────────┬──────────────────────────────────────────────────────────────────────────────┐
│                      │                                                                              │
│  > menu              │   Sistema de atendimento - HealthCore                                        │
│                      │                                                                              │
│  cadastro            │   ┌──────────────────────────────┐  ┌──────────────────────────────┐         │
│                      │   │      Banco de Pacientes      │  │      Fila de Atendimento     │         │
│  fila                │   └──────────────────────────────┘  └──────────────────────────────┘         │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
└──────────────────────┴──────────────────────────────────────────────────────────────────────────────┘
```

**Comportamentos implementados nesta tela:**
- [✔] Nome do sistema exibido
- [✔] Lista de operações disponíveis
- [ ] Opção de sair

---

### 7.3 Tela 2 — Entrada de Dados

**Descrição:** 
Nesta tela, o usuário informa os dados do paciente por meio de um formulário de cadastro. São preenchidos campos como nome, CPF, idade, telefone e informação sobre deficiência. Após inserir os dados, o usuário clica no botão “Salvar” para registrar o paciente no sistema. Também existe a opção “Desfazer”, que utiliza a estrutura de pilha para remover a última ação realizada.

**Print ou representação textual:**
```
[Cole aqui um print da tela ou representação do prompt/formulário de entrada]
┌──────────────────────┬──────────────────────────────────────────────────────────────────────────────┐
│                      │                                                                              │
│  menu                │   Cadastro de Pacientes                                                      │
│                      │                                                                              │
│  > cadastro          │   Novo Paciente                                                              │
│                      │   ┌──────────────────────────────────────────────────────────────────────┐   │
│  fila                │   │ Nome        CPF         Idade       Telefone     Portador deficiência│   │
│                      │   │ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐      ┌──────────────┐    │   │
│                      │   │ │        │ │        │ │        │ │        │      │ Não        ▼ │    │   │
│                      │   │ └────────┘ └────────┘ └────────┘ └────────┘      └──────────────┘    │   │
│                      │   │                                                                      │   │
│                      │   │ [ Salvar ]                                                           │   │
│                      │   └──────────────────────────────────────────────────────────────────────┘   │
│                      │                                                                              │
│                      │   [ Desfazer ]                                                               │
│                      │                                                                              │
│                      │   ──────────────────────────────────────────────────────────────────────     │
│                      │                                                                              │
│                      │   Pacientes Cadastrados                                                      │
│                      │   ┌──────────────────────────────────────────────────────────────────────┐   │
│                      │   │ Nenhum paciente cadastrado.                                          │   │
│                      │   └──────────────────────────────────────────────────────────────────────┘   │
│                      │                                                                              │
└──────────────────────┴──────────────────────────────────────────────────────────────────────────────┘
```

**Comportamentos implementados nesta tela:**
- [✔] Campo ou prompt para inserir valor
- [ ] Opção de carregar arquivo
- [✔] Confirmação da ação antes de executar

---

### 7.4 Tela 3 — Resultado

**Descrição:** 
Após o cadastro, o usuário pode visualizar a fila de atendimento do sistema. Nessa tela, os pacientes aparecem organizados conforme a prioridade definida pelas regras da fila prioritária, considerando fatores como idade ou deficiência. O usuário consegue acompanhar a ordem de atendimento e visualizar qual será o próximo paciente chamado.

**Print ou representação textual:**
```
[Cole aqui um print da tela ou representação do resultado exibido]
┌──────────────────────┬──────────────────────────────────────────────────────────────────────────────┐
│                      │                                                                              │
│  menu                │   Fila de Atendimento - HealthCore                                           │
│                      │                                                                              │
│  cadastro            │   Adicionar Paciente na Fila                                                 │
│                      │   ┌──────────────────────────────────────────────────────────────────────┐   │
│  > fila              │   │ CPF do Paciente                                                      │   │
│                      │   │ ┌────────────────────────────────────────────────────────────────┐   │   │
│                      │   │ │                                                                │   │   │
│                      │   │ └────────────────────────────────────────────────────────────────┘   │   │
│                      │   │                                                                      │   │
│                      │   │ Nível de Emergência                                                  │   │
│                      │   │ ┌────────────────────────────────────────────────────────────────┐   │   │
│                      │   │ │ Vermelho                                                   ▼   │   │   │
│                      │   │ └────────────────────────────────────────────────────────────────┘   │   │
│                      │   │                                                                      │   │
│                      │   │ [ Adicionar ]                                                        │   │
│                      │   └──────────────────────────────────────────────────────────────────────┘   │
│                      │                                                                              │
│                      │   [ Atualizar fila ]                                                         │
│                      │                                                                              │
│                      │   [ Atender próximo ]                                                        │
│                      │                                                                              │
│                      │   [ Desfazer última ação da fila ]                                           │
│                      │    ───────────────────────────────────────────────────────────────────────── │
│                      │    FILA DE ATENDIMENTO                                                       │
│                      │                                                                              │
│                      │    ┌────────────────────────────────────────────────────────────────┐        │
│                      │    │Fila vazia.                                                     │        │
│                      │    └────────────────────────────────────────────────────────────────┘        │
└──────────────────────┴──────────────────────────────────────────────────────────────────────────────┘
```

**Comportamentos implementados nesta tela:**
- [✔] Resultado da operação executada
- [✔] Estado atual completo da estrutura
- [✔] Mensagem de erro para operações inválidas (ex.: pop em pilha vazia)

---

### 7.5 Fluxo completo demonstrado

> Descreva um cenário de uso de ponta a ponta, mostrando as 3 telas em sequência.

**Cenário:** [Usuario cadastra paciente, insere ele na fila de atendimento e Chama para atendimento.]

```
[Cole aqui a saída real do programa, do início ao fim do cenário descrito]
Tela 1 - menu
┌──────────────────────┬──────────────────────────────────────────────────────────────────────────────┐
│                      │                                                                              │
│  > menu              │   Sistema de atendimento - HealthCore                                        │
│                      │                                                                              │
│  cadastro            │   ┌──────────────────────────────┐  ┌──────────────────────────────┐         │
│                      │   │      Banco de Pacientes      │  │      Fila de Atendimento     │         │
│  fila                │   └──────────────────────────────┘  └──────────────────────────────┘         │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
│                      │                                                                              │
└──────────────────────┴──────────────────────────────────────────────────────────────────────────────┘

Tela 2 - Cadastro
┌──────────────────────┬───────────────────────────────────────────────────────────────────────────────────┐
│                      │                                                                                   │
│  menu                │   Cadastro de Pacientes                                                           │
│                      │                                                                                   │
│  > cadastro          │   Novo Paciente                                                                   │
│                      │   ┌───────────────────────────────────────────────────────────────────────────┐   │
│  fila                │   │ Nome        CPF           Idade       Telefone       Portador deficiência │   │
│                      │   │ ┌────────┐ ┌───────────┐ ┌────────┐  ┌───────────┐      ┌──────────────┐  │   │
│                      │   │ │Aline   │ │12345678901│ │ 35     │  │11999999999│      │ Não        ▼ │  │   │
│                      │   │ └────────┘ └───────────┘ └────────┘  └───────────┘      └──────────────┘  │   │
│                      │   │                                                                           │   │
│                      │   │ [ Salvar ]                                                                │   │
│                      │   └───────────────────────────────────────────────────────────────────────────┘   │
│                      │                                                                                   │
│                      │   [ Desfazer ]                                                                    │
│                      │                                                                                   │
│                      │   ──────────────────────────────────────────────────────────────────────          │
│                      │                                                                                   │
│                      │   Pacientes Cadastrados                                                           │
│                      │   ┌──────────────────────────────────────────────────────────────────────┐        │
│                      │   │Aline      1234567      20         1199999          Não               │        │
│                      │   └──────────────────────────────────────────────────────────────────────┘        │
│                      │                                                                                   │
└──────────────────────┴───────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────┬──────────────────────────────────────────────────────────────────────────────┐
│                      │                                                                              │
│  menu                │   Fila de Atendimento - HealthCore                                           │
│                      │                                                                              │
│  cadastro            │   Adicionar Paciente na Fila                                                 │
│                      │   ┌──────────────────────────────────────────────────────────────────────┐   │
│  > fila              │   │ CPF do Paciente                                                      │   │
│                      │   │ ┌────────────────────────────────────────────────────────────────┐   │   │
│                      │   │ │12345678901                                                     │   │   │
│                      │   │ └────────────────────────────────────────────────────────────────┘   │   │
│                      │   │                                                                      │   │
│                      │   │ Nível de Emergência                                                  │   │
│                      │   │ ┌────────────────────────────────────────────────────────────────┐   │   │
│                      │   │ │ Vermelho                                                   ▼   │   │   │
│                      │   │ └────────────────────────────────────────────────────────────────┘   │   │
│                      │   │                                                                      │   │
│                      │   │ [ Adicionar ]                                                        │   │
│                      │   └──────────────────────────────────────────────────────────────────────┘   │
│                      │                                                                              │
│                      │   [ Atualizar fila ]                                                         │
│                      │                                                                              │
│                      │   [ Atender próximo ]                                                        │
│                      │                                                                              │
│                      │   [ Desfazer última ação da fila ]                                           │
│                      │    ───────────────────────────────────────────────────────────────────────── │
│                      │    FILA DE ATENDIMENTO                                                       │
│                      │                                                                              │
│                      │    ┌────────────────────────────────────────────────────────────────┐        │
│                      │    │1. Aline|CPF:12345678901 |Nível: Vermelho                       │        │
│                      │    └────────────────────────────────────────────────────────────────┘        │
└──────────────────────┴──────────────────────────────────────────────────────────────────────────────┘

```

---

## 8. Testes Unitários

**Framework de testes utilizado:** [ unittest ]

**Localização:** `tests/[test_fila_atendimento.py]`

### Estrutura testada: [Fila de atendimento]

---

**Teste 1 — Caso base**

Descrição: [Verifica se o paciente é inserido corretamente na fia de atendimento]

```[python]
[
        import unittest
    from structures.fila_atendimento import FilaAtendimento
    from models.paciente import Paciente


    class TestFilaAtendimento(unittest.TestCase):

        def test_adicionar_paciente(self):
            fila = FilaAtendimento()

            paciente = Paciente("Breno", "123")
            fila.adicionar(paciente, "Amarelo")

            self.assertIsNotNone(fila.inicio)
]
```

Resultado: ✅ Passando

---

**Teste 2 — Caso vazio**

Descrição: [Verifica o comportamento do sistema ao tentar atender um paciente quando a fila está vazia.]

```[Python]
[
    def test_fila_vazia(self):
    fila = FilaAtendimento()

    paciente = fila.atender_proximo()

    self.assertIsNone(paciente)
]
```

Resultado: ✅ Passando

---

**Teste 3 — Caso com múltiplos elementos**

Descrição: [Verifica o comportamento do sistema ao tentar atender um paciente quando a fila está vazia.]

```[Python]
[
    def test_ordem_atendimento(self):
    fila = FilaAtendimento()

    p1 = Paciente("Ana", "111")
    p2 = Paciente("Carlos", "222")

    fila.adicionar(p1, "Verde")
    fila.adicionar(p2, "Verde")

    primeiro = fila.atender_proximo()

    self.assertEqual(primeiro.paciente.nome, "Ana")
]
```

Resultado: ✅ Passando

---

## Checklist de Autoavaliação

Antes de entregar, verifique se você:

**Seção 1 — Estruturas**
- [ ✔ ] Big-O preenchido para inserção, remoção, busca e acesso de cada estrutura
- [ ✔ ] Pelo menos 1 alternativa descartada com justificativa técnica
- [ ✔ ] Limitações conhecidas descritas
- [ ✔ ] Referência bibliográfica fornecida

**Seção 2 — Arquitetura**
- [ ✔ ] Diagrama com as 3 camadas visíveis
- [ ✔ ] Fluxo de comunicação entre camadas descrito

**Seção 3 — Diretórios**
- [ ✔ ] Árvore de diretórios presente
- [ ✔ ] Desvios do modelo justificados (ou "Nenhum desvio" declarado)

**Seção 4 — Backlog**
- [ ✔ ] 5 ou mais itens In-Scope com critério de aceite no formato Dado/Quando/Então
- [ ✔ ] 3 ou mais itens Out-of-Scope com justificativa

**Seção 5 — Repositório**
- [ ✔ ] Link do repositório público informado
- [ ✔ ] README.md com instruções de execução
- [ ✔ ] Mínimo de 5 commits semânticos

**Seção 6 — Núcleo**
- [ ✔ ] Pelo menos 1 estrutura completamente implementada
- [ ✔ ] Leitura de arquivo funcionando
- [ ✔ ] Trecho de código representativo incluído no template

**Seção 7 — MVP**
- [ ✔ ] 3 telas documentadas com print ou representação textual
- [ ✔ ] Fluxo completo de ponta a ponta demonstrado
- [ ✔ ] Mensagem de erro para operação inválida implementada
- [ ✔ ] Loop de menu funcionando (programa não encerra após 1 operação)

**Seção 8 — Testes**
- [ ✔ ] 3 testes por estrutura documentados neste template
- [ ✔ ] Resultado de cada teste indicado (✅ / ❌)

---

*Nome do arquivo de entrega: `E2_<grupo>_Design_Tecnico.md`*
*Este arquivo deve estar na pasta `/doc` do repositório.*
