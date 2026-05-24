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
```txt
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CAMADA DE APRESENTAÇÃO (UI/STREAMLIT)                     ║
║                                                                              ║
║  ┌──────────────────┐   ┌──────────────────┐   ┌─────────────────────────┐   ║
║  │  menu_inicial.py │   │ menu_cadastro.py │   │      menu_fila.py       │   ║
║  │                  │   │                  │   │                         │   ║
║  │ • Navegação      │   │ • Cadastro       │   │ • Adicionar paciente    │   ║
║  │ • Seleção telas  │   │ • Editar         │   │ • Atender próximo       │   ║
║  │ • Histórico      │   │ • Remover        │   │ • Atualizar fila        │   ║
║  │                  │   │ • Listar         │   │ • Desfazer ação         │   ║
║  │                  │   │ • Validações UI  │   │ • Exibir fila           │   ║
║  └──────────────────┘   └──────────────────┘   └─────────────────────────┘   ║
╚══════════════════════════════════════════════════════════════════════════════╝
                                       │
                                       ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║                       CAMADA DE APLICAÇÃO (SERVICE)                          ║
║                                                                              ║
║   ┌─────────────────────────┐      ┌─────────────────────────┐               ║
║   │   paciente_service.py   │      │     fila_service.py     │               ║
║   │                         │      │                         │               ║
║   │ • cadastrar()           │      │ • adicionar()           │               ║
║   │ • editar()              │      │ • atender_proximo()     │               ║
║   │ • remover()             │      │ • remover()             │               ║
║   │ • buscar()              │      │ • atualizar_fila()      │               ║
║   │ • listar()              │      │ • desfazer()            │               ║
║   │ • validar_dados()       │      │ • listar()              │               ║
║   └─────────────────────────┘      └─────────────────────────┘               ║
╚══════════════════════════════════════════════════════════════════════════════╝
                                       │
                                       ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║                          CAMADA DE DOMÍNIO (CORE)                            ║
║                                                                              ║
║  ┌────────────────────┐  ┌────────────────────┐  ┌──────────────────────┐    ║
║  │    paciente.py     │  │ fila_atendimento.py│  │    pilha_acoes.py    │    ║
║  │                    │  │                    │  │                      │    ║
║  │ • Lista encadeada  │  │ • Fila prioridade  │  │ • Histórico ações    │    ║
║  │ • Inserção         │  │ • Inserção orden.  │  │ • Desfazer cadastro  │    ║
║  │ • Remoção          │  │ • Remoção          │  │ • Desfazer fila      │    ║
║  │ • Busca por CPF    │  │ • Atualização      │  │ • empilhar()         │    ║
║  │ • Persistência JSON│  │ • Prioridades      │  │ • desempilhar()      │    ║
║  │                    │  │                    │  │ • vazia()            │    ║
║  └────────────────────┘  └────────────────────┘  └──────────────────────┘    ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### Descrição das camadas

| Camada | Componentes | Responsabilidade |
|--------|-------------|------------------|
| Apresentação (UI) | `menu_inicial.py`, `menu_cadastro.py`, `menu_fila.py` | Responsável pela interação com o usuário utilizando Streamlit, exibindo formulários, tabelas, mensagens de erro, mensagens de sucesso e botões de navegação. |
| Aplicação (Service) | `paciente_service.py`, `fila_service.py` | Implementa as regras de negócio do sistema, valida os dados recebidos da interface e coordena as operações realizadas nas estruturas de dados. |
| Domínio (Core) | `paciente.py`, `fila_atendimento.py`, `pilha_acoes.py` | Implementa as estruturas de dados principais do sistema: lista encadeada, fila de prioridade e pilha de ações. Também realiza a persistência dos dados em JSON. |

### Como as camadas se comunicam

O usuário interage inicialmente com a interface desenvolvida em Streamlit, localizada na camada de apresentação. Essa interface coleta os dados digitados nos formulários, como nome, CPF, idade, telefone, deficiência e nível de emergência.

Em seguida, essas informações são enviadas para a camada de aplicação, onde os Services validam os dados e aplicam as regras de negócio. Por exemplo, o `PacienteService` valida campos obrigatórios, CPF com 11 dígitos, telefone com 11 dígitos e idade válida. Já o `FilaService` controla a entrada dos pacientes na fila, o atendimento do próximo paciente, a atualização da fila e o desfazer da última ação.

Após a validação, os Services chamam a camada de domínio, onde ficam as estruturas de dados:

- Lista encadeada para armazenar e gerenciar os pacientes cadastrados;
- Fila de prioridade para organizar a ordem de atendimento;
- Pilha de ações para armazenar o histórico e permitir desfazer a última ação realizada.

A pilha de ações (`pilha_acoes.py`) funciona como histórico do sistema. Sempre que uma ação importante é realizada, como cadastrar um paciente ou adicionar um paciente à fila, essa ação é armazenada na pilha. Quando o usuário clica em “Desfazer”, o sistema consulta esse histórico e remove a última ação registrada, seguindo a lógica LIFO.

A camada Core também realiza a persistência dos dados em arquivos JSON localizados na pasta `src/data/`.

---


## 3. Estrutura de Diretórios

```txt
/
├── src/
│   ├── app.py
│   ├── core/
│   │   ├── fila_atendimento.py
│   │   ├── paciente.py
│   │   └── pilha_acoes.py
│   ├── data/
│   │   ├── pacientes.json
│   │   └── historico_acoes.json
│   ├── service/
│   │   ├── fila_service.py
│   │   └── paciente_service.py
│   └── ui/
│       ├── menu_cadastro.py
│       ├── menu_fila.py
│       ├── menu_historico.py
│       └── menu_inicial.py
├── tests/
│   ├── test_fila.py
│   ├── test_paciente.py
│   └── test_pilha.py
├── README.md
└── executar.bat
```

**Justificativa de desvios (se houver):**
Sem desvios.

---


## 4. Backlog do Projeto

### In-Scope — O que será implementado

> Mínimo 5 itens. Cada item deve ter um critério de aceite no formato Dado / Quando / Então.

---

**Item 1:** Cadastro de pacientes

Critério de aceite:
Dado um usuário preenchendo nome, idade, CPF, telefone e deficiência, quando o cadastro for confirmado, então o sistema deve validar os campos, inserir o paciente na lista encadeada utilizando `inserir()` e exibir a confirmação do cadastro.

---

**Item 2:** Busca de pacientes

Critério de aceite:
Dado pacientes cadastrados na lista encadeada, quando o usuário pesquisar um CPF, então o sistema deve localizar o paciente utilizando `buscar()` e exibir seus dados na tela.

---

**Item 3:** Organização da fila de atendimento

Critério de aceite:
Dado múltiplos pacientes com diferentes níveis de emergência, quando um novo paciente entrar na fila, então a fila de prioridade deve inserir o paciente na posição correta conforme sua pontuação.

---

**Item 4:** Chamada de pacientes

Critério de aceite:
Dado uma fila contendo pacientes aguardando atendimento, quando o usuário executar “Atender próximo”, então o sistema deve remover o primeiro paciente da fila de prioridade utilizando `atender_proximo()` e exibir seus dados.

---

**Item 5:** Remoção de pacientes da fila

Critério de aceite:
Dado uma fila contendo pacientes aguardando atendimento, quando o usuário solicitar a remoção de um paciente, então o sistema deve removê-lo da fila utilizando `remover()` e atualizar a ordem da fila.

---

**Item 6:** Visualização da fila

Critério de aceite:
Dado pacientes adicionados à fila de atendimento, quando o usuário acessar a tela da fila, então o sistema deve exibir a ordem atual dos pacientes e seus respectivos níveis de emergência.

---

**Item 7:** Desfazer última ação

Critério de aceite:
Dado um histórico de ações armazenado na pilha, quando o usuário clicar em “Desfazer última ação”, então o sistema deve remover a última ação registrada utilizando `desempilhar()` e restaurar o estado anterior da operação realizada.

---

**Item 8:** Histórico de ações

Critério de aceite:
Dado ações realizadas no sistema, quando o usuário acessar o histórico, então o sistema deve exibir as ações registradas em arquivo JSON, permitindo acompanhar as operações recentes.

---

### Out-of-Scope — O que não será implementado

| Funcionalidade | Motivo de exclusão |
|----------------|--------------------|
| Controle financeiro e faturamento | Funcionalidades relacionadas a pagamentos, convênios e emissão de cobranças não agregam ao aprendizado do conteúdo de Estrutura de Dados. |
| Histórico médico completo dos pacientes | Possui complexidade elevada. O sistema armazenará apenas informações necessárias para o atendimento atual e gerenciamento da fila. |
| Aplicação em nuvem | Fora do escopo do semestre e de alta complexidade de implementação. O projeto será executado localmente, sem hospedagem online. |

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
py -m streamlit run src/app.py
]
```

---

## 6. Implementação do Núcleo

### 6.1 Estrutura implementada: Fila prioritaria

**Linguagem:** Python 3.11

**Localização no repositório:** `src/core/fila_atendimento.py`

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
 
### 6.2 Estrutura implementada: Lista
Linguagem: Python 3.11
Localização no repositório: src/core/paciente.py

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
Esse trecho representa a lógica da lista encadeada de pacientes, responsável por inserir pacientes em ordem alfabética.

```python
def _inserir_sem_salvar(self, nome, cpf, idade, telefone, deficiencia):
    novo = NoPaciente(nome, cpf, idade, telefone, deficiencia)

    if self.inicio is None:
        self.inicio = novo
        return True

    if nome.lower() < self.inicio.nome.lower():
        novo.proximo = self.inicio
        self.inicio = novo
        return True

    atual = self.inicio

    while atual.proximo and atual.proximo.nome.lower() < nome.lower():
        atual = atual.proximo

    novo.proximo = atual.proximo
    atual.proximo = novo

    return True
```


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
src/core/pilha_acoes.py

**Operações implementadas:**

| Operação | Implementada? | Observação |
|----------|---------------|------------|
| empilhar | ✅ | Adiciona uma ação realizada ao topo da pilha |
| desempilhar | ✅ | Remove e retorna a última ação realizada |
| vazia | ✅ | Verifica se existe alguma ação armazenada |

**Trecho representativo do código** *(operação principal)*:
Esse trecho representa a principal lógica da pilha de ações, responsável por armazenar o histórico de operações realizadas no sistema seguindo o conceito LIFO (Last In, First Out), permitindo desfazer a última ação executada.

```python
def empilhar(self, acao):
    self.itens.append(acao)

def desempilhar(self):
    if self.vazia():
        return None

    return self.itens.pop()

def vazia(self):
    return len(self.itens) == 0
```



## 7. MVP — Mínimo Produto Viável

### 7.1 Tipo de interface

- [ ] CLI (linha de comando)
- [✔] GUI desktop (Tkinter, JavaFX, outro: Streamlit)
- [ ] Web (HTML/JS, outro: __________)

### 7.2 Tela 1 — Boas-vindas / Menu Principal

**Descrição:** 
A tela inicial do sistema funciona como um menu de navegação principal. Nela, o usuário pode escolher entre acessar o banco de pacientes, visualizar a fila de atendimento ou consultar o histórico de ações. Essa tela centraliza as funcionalidades do sistema e facilita a navegação entre as operações disponíveis.
```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   Sistema de Atendimento - HealthCore                                        │
│                                                                              │
│   ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐   │
│   │ Banco de Pacientes   │  │ Fila de Atendimento  │  │ Histórico Ações  │   │
│   └──────────────────────┘  └──────────────────────┘  └──────────────────┘   │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Comportamentos implementados nesta tela:**
- [✔] Nome do sistema exibido
- [✔] Lista de operações disponíveis
- [✔] Navegação para Banco de Pacientes, Fila de Atendimento e Histórico de Ações
- [ ] Opção de sair

---

### 7.3 Tela 2 — Entrada de Dados

**Descrição:** 
Nesta tela, o usuário informa os dados do paciente por meio de um formulário de cadastro. São preenchidos campos como nome, CPF, idade, telefone e informação sobre deficiência. Após inserir os dados, o usuário clica no botão “Salvar” para registrar o paciente no sistema. O sistema também exibe mensagens de erro quando algum campo obrigatório fica vazio ou quando CPF/telefone não possuem 11 dígitos.

**Print ou representação textual:**
```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [⬅ Voltar ao Menu]                                                          │
│                                                                              │
│   Cadastro de Pacientes                                                      │
│                                                                              │
│   ┌──────────────────────────────────────────────────────────────────────┐   │
│   │ Nome      CPF             Idade    Telefone        Portador defic.   │   │
│   │ ┌──────┐  ┌───────────┐   ┌───┐    ┌───────────┐   ┌────────────┐    │   │
│   │ │      │  │           │   │   │    │           │   │ Não      ▼ │    │   │
│   │ └──────┘  └───────────┘   └───┘    └───────────┘   └────────────┘    │   │
│   │                                                                      │   │
│   │ [ Salvar ]                                                           │   │
│   └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│                                                                              │
│   ──────────────────────────────────────────────────────────────────────     │
│   Pacientes Cadastrados                                                      │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Comportamentos implementados nesta tela:**
- [✔] Campo ou prompt para inserir valor
- [ ] Opção de carregar arquivo
- [✔] Confirmação da ação antes de executar

---

### 7.4 Tela 3 — Resultado

**Descrição:** 
Após o cadastro, o usuário pode visualizar a fila de atendimento do sistema. Nessa tela, os pacientes aparecem organizados conforme a prioridade definida pelas regras da fila prioritária, considerando o nível de emergência informado. O usuário consegue acompanhar a ordem de atendimento e visualizar qual será o próximo paciente chamado.

**Print ou representação textual:**
```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [⬅ Voltar ao Menu]                                                          │
│                                                                              │
│   Fila de Atendimento                                                        │
│                                                                              │
│   Adicionar Paciente                                                         │
│   ┌──────────────────────────────────────────────────────────────────────┐   │
│   │ CPF do Paciente                                                      │   │
│   │ ┌────────────────────────────────────────────────────────────────┐   │   │
│   │ │                                                                │   │   │
│   │ └────────────────────────────────────────────────────────────────┘   │   │
│   │                                                                      │   │
│   │ Nível de Emergência                                                  │   │
│   │ ┌────────────────────────────────────────────────────────────────┐   │   │
│   │ │ Vermelho                                                   ▼   │   │   │
│   │ └────────────────────────────────────────────────────────────────┘   │   │
│   │                                                                      │   │
│   │ [ Adicionar ]                                                        │   │
│   └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│       [ Atualizar fila ]                         [ Atender próximo ]         │
│                                                                              │
│                          [ Desfazer última ação ]                            │
│                                                                              │
│   ──────────────────────────────────────────────────────────────────────     │
│   Fila Atual                                                                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
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
Tela 1 - Menu Principal
┌──────────────────────────────────────────────────────────────────────────────┐
│   Sistema de Atendimento - HealthCore                                        │
│                                                                              │
│   [ Banco de Pacientes ]   [ Fila de Atendimento ]   [ Histórico de Ações ]  │
└──────────────────────────────────────────────────────────────────────────────┘

Tela 2 - Cadastro de Pacientes
┌──────────────────────────────────────────────────────────────────────────────┐
│ [⬅ Voltar ao Menu]                                                          │
│                                                                              │
│   Cadastro de Pacientes                                                      │
│                                                                              │
│   Nome      CPF           Idade   Telefone      Portador deficiência         │
│   Aline     12345678901   35      11999999999   Não                          │
│                                                                              │
│   [ Salvar ]                                                                 │
│                                                                              │
│   Paciente cadastrado com sucesso.                                           │
│                                                                              │
│   Pacientes Cadastrados                                                      │
│   Aline | CPF: 12345678901 | Idade: 35 | Tel: 11999999999 | Não | [Editar]   │
│                                                                   [Excluir]  │
└──────────────────────────────────────────────────────────────────────────────┘

Tela 3 - Fila de Atendimento
┌──────────────────────────────────────────────────────────────────────────────┐
│ [⬅ Voltar ao Menu]                                                          │
│                                                                              │
│   Fila de Atendimento                                                        │
│                                                                              │
│   CPF do Paciente: 12345678901                                               │
│   Nível de Emergência: Vermelho                                              │
│                                                                              │
│   [ Adicionar ]                                                              │
│   ✅ Paciente adicionado à fila com sucesso.                                │
│                                                                              │
│   [ Atualizar fila ]   [ Atender próximo ]                                   │
│   [ Desfazer última ação ]                                                   │
│                                                                              │
│   Fila Atual                                                                 │
│   1. Aline | CPF: 12345678901 | Nível: Vermelho                              │
└──────────────────────────────────────────────────────────────────────────────┘

Tela 4 - Histórico de Ações
┌──────────────────────────────────────────────────────────────────────────────┐
│ [⬅ Voltar ao Menu]                                                          │
│                                                                              │
│   Histórico de Ações                                                         │
│   Exibe as ações mais recentes.                                              │
│                                                                              │
│   Total de ações salvas: 1 / 50                                              │
│                                                                              │
│   tipo             cpf           nivel                                       │
│   adicionar_fila   12345678901   Vermelho                                    │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Testes Unitários

**Framework de testes utilizado:** `unittest`

**Localização dos testes:**

```txt
tests/test_fila.py
tests/test_paciente.py
tests/test_pilha.py
```

### Estrutura testada: Fila de atendimento

---

**Teste 1 — Adicionar paciente na fila**

Descrição: Verifica se o paciente é inserido corretamente na fila de atendimento.

```python
import unittest
from src.core.fila_atendimento import FilaAtendimento
from src.core.paciente import NoPaciente

class TestFilaAtendimento(unittest.TestCase):

    def test_adicionar_paciente(self):
        fila = FilaAtendimento()
        paciente = NoPaciente("Breno", "12345678901", 20, "11999999999", "Não")

        fila.adicionar(paciente, "Amarelo")

        self.assertIsNotNone(fila.inicio)
```

Resultado: ✅ Passando

---

**Teste 2 — Fila vazia**

Descrição: Verifica o comportamento do sistema ao tentar atender um paciente quando a fila está vazia.

```python
def test_fila_vazia(self):
    fila = FilaAtendimento()

    paciente = fila.atender_proximo()

    self.assertIsNone(paciente)
```

Resultado: ✅ Passando

---

**Teste 3 — Ordem de atendimento**

Descrição: Verifica se a fila mantém a ordem correta de atendimento de acordo com a entrada e prioridade dos pacientes.

```python
def test_ordem_atendimento(self):
    fila = FilaAtendimento()

    p1 = NoPaciente("Ana", "11111111111", 30, "11999999999", "Não")
    p2 = NoPaciente("Carlos", "22222222222", 40, "11988888888", "Não")

    fila.adicionar(p1, "Verde")
    fila.adicionar(p2, "Verde")

    primeiro = fila.atender_proximo()

    self.assertEqual(primeiro.paciente.nome, "Ana")
```

Resultado: ✅ Passando

### Observação sobre os testes

O projeto possui testes automatizados para fila, pacientes e pilha. Na última execução realizada, os testes passaram corretamente.

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
- [ ✔ ] Testes automatizados documentados neste template
- [ ✔ ] Resultado dos testes indicado (✅ / ❌)

---

*Nome do arquivo de entrega: `E2_<grupo>_Design_Tecnico.md`*
*Este arquivo deve estar na pasta `/doc` do repositório.*
