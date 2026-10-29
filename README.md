# 🤖 Sistema Multiagente RPA com OpenAI Agents SDK

Sistema multiagente desenvolvido em Python para monitoramento e diagnóstico de automações RPA utilizando **OpenAI Agents SDK, handoffs, Function Tools e integração HTTP com FastAPI**.

O projeto demonstra como agentes especializados podem colaborar em uma arquitetura organizada, encaminhando solicitações de acordo com suas responsabilidades e consultando serviços externos para obter informações.

> **Projeto educacional:** as automações e seus logs são simulados. O sistema não realiza operações reais de reinício ou modificação de processos.

## 🚀 Funcionalidades

- Interpretação de solicitações em linguagem natural.
- Roteamento entre agentes especializados por handoffs.
- Consulta do status de automações RPA.
- Consulta de logs e identificação de falhas.
- Diagnóstico técnico com sugestões de investigação.
- Integração com API REST por meio de HTTPX.
- Validação de identificadores de processos.
- Tratamento de falhas HTTP, timeout e indisponibilidade.
- Testes automatizados com Pytest.
- Separação entre agentes, ferramentas e serviços HTTP.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| OpenAI Agents SDK | Criação e execução de agentes |
| GPT-4o mini | Modelo de linguagem |
| Handoffs | Transferência de tarefas entre agentes |
| Function Tools | Execução de funções Python |
| HTTPX | Integração com API REST |
| FastAPI | Serviço externo de monitoramento |
| Pytest | Testes automatizados |
| python-dotenv | Carregamento de variáveis de ambiente |

## 🏗️ Arquitetura

O sistema possui três agentes especializados.

### Agente Coordenador

Recebe a solicitação do usuário e encaminha a tarefa ao agente mais adequado por meio de handoffs.

### Agente de Monitoramento

Responsável por consultar o status e os logs das automações RPA.

### Agente de Diagnóstico

Responsável por consultar evidências de falhas, apresentar hipóteses técnicas e sugerir verificações e medidas preventivas.

```text
              Usuário
                 |
                 v
         Agente Coordenador
                 |
           Handoff
            /       \
           v         v
    Monitoramento  Diagnóstico
           \         /
            \       /
             v     v
         Function Tools
                 |
                 v
               HTTPX
                 |
                 v
       API de Monitoramento
          FastAPI :8002
                 |
                 v
        Dados RPA simulados
```

O especialista selecionado assume a execução da tarefa e produz a resposta final.

## 📂 Estrutura do projeto

```text
agents-python/
├── agentes/
│   ├── __init__.py
│   ├── coordenador.py
│   ├── monitoramento.py
│   └── diagnostico.py
├── tests/
│   ├── test_agentes.py
│   └── test_cliente_rpa.py
├── main.py
├── ferramentas.py
├── cliente_rpa.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/luisalvs/rpa-multiagente-openai.git
cd rpa-multiagente-openai
```

### 2. Criar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a OpenAI

Crie um arquivo `.env`:

```env
OPENAI_API_KEY=sua_chave_openai_aqui
```

O arquivo `.env` deve permanecer fora do versionamento.

## 🔗 Dependência externa: API de monitoramento

Este projeto utiliza uma API FastAPI local, desenvolvida separadamente.

Repositório:

https://github.com/luisalvs/assistente-rpa-function-calling

Clone o projeto de monitoramento e instale suas dependências.

Em um terminal, dentro do projeto de monitoramento:

```bash
python -m uvicorn api_monitoramento:app --port 8002
```

O serviço deverá ficar disponível em:

```text
http://127.0.0.1:8002
```

Os endpoints utilizados são:

| Método | Endpoint | Finalidade |
|---|---|---|
| GET | `/health` | Verificar disponibilidade |
| GET | `/rpas/{codigo}` | Consultar status |
| GET | `/rpas/{codigo}/logs` | Consultar logs |

A URL da API está configurada na constante `API_BASE` do arquivo `cliente_rpa.py`.

## ▶️ Executar o sistema multiagente

Com a API de monitoramento funcionando, execute:

```bash
python main.py
```

O programa iniciará um terminal interativo.

## 💬 Exemplos de utilização

### Consulta de status

**Pergunta:**

```text
Qual é o status da RPA-101?
```

**Comportamento esperado:**

O coordenador encaminha a tarefa ao agente de monitoramento, que consulta a API e retorna o status da automação.

### Investigação de falha

**Pergunta:**

```text
Por que a RPA-103 apresentou erro e como posso investigar?
```

**Comportamento esperado:**

O coordenador encaminha a tarefa ao agente de diagnóstico, que consulta status e logs antes de sugerir verificações técnicas.

### Diagnóstico de timeout

**Pergunta:**

```text
Analise a falha da RPA-103 e me diga como evitar que aconteça novamente.
```

O agente apresenta:

- Evidência encontrada nos logs.
- Três hipóteses técnicas.
- Duas verificações práticas.
- Uma recomendação preventiva.

O agente diferencia informações comprovadas de possíveis causas.

## 🧰 Ferramentas Python

### consultar_status_rpa

Consulta o status de uma automação pelo identificador.

### consultar_log_rpa

Consulta o último evento e os erros registrados.

Ambas são implementadas usando o decorador `@function_tool` do OpenAI Agents SDK.

As ferramentas utilizam o cliente HTTP definido em `cliente_rpa.py`.

## 🛡️ Tratamento de erros

O cliente HTTP trata:

- Identificadores RPA inválidos.
- Recursos não autorizados.
- Processos inexistentes.
- Timeouts de comunicação.
- Falhas de conexão.
- Erros HTTP.
- Respostas JSON inválidas.

O agente é instruído a não confundir uma falha na comunicação com a API com um erro da automação monitorada.

O projeto ainda não possui autenticação e autorização de usuários, portanto não deve ser exposto publicamente como um serviço de produção.

## 🧪 Testes automatizados

O projeto utiliza Pytest para validar o comportamento do cliente HTTP e a configuração dos agentes.

Execute:

```bash
python -m pytest -v tests/
```

Os testes incluem:

1. Consulta de status bem-sucedida.
2. Consulta de logs bem-sucedida.
3. Rejeição de código inválido.
4. Tratamento de processo inexistente.
5. Tratamento de falha de conexão.
6. Tratamento de timeout.
7. Rejeição de recurso inválido.
8. Configuração dos handoffs do coordenador.
9. Ferramentas do agente de monitoramento.
10. Ferramentas do agente de diagnóstico.
11. Verificação dos nomes e responsabilidades dos agentes.

**Resultado obtido durante o desenvolvimento:**

```text
11 passed in 0.69s
```

Os testes utilizam mocks para evitar requisições HTTP reais e chamadas à OpenAI.

Os testes de configuração não substituem avaliações do comportamento real do modelo.

## 📈 Melhorias futuras

- Adicionar tracing e observabilidade dos agentes.
- Implementar avaliações automatizadas das decisões de handoff.
- Adicionar histórico de conversas.
- Persistir dados em PostgreSQL.
- Implementar autenticação e autorização.
- Integrar serviços reais de monitoramento.
- Disponibilizar o sistema através de FastAPI.
- Preparar deploy com Docker e infraestrutura cloud.

## 🎯 Objetivo

Este projeto faz parte de um roteiro prático de evolução de **Desenvolvimento Python e RPA para Engenharia de IA e Automação Inteligente**.

Seu objetivo é demonstrar como estruturar agentes especializados, executar ferramentas Python, integrar serviços HTTP e aplicar testes automatizados.

## 👨‍💻 Autor

**Luis Alves**

Desenvolvedor Python | RPA | APIs REST | Automação Inteligente

GitHub: https://github.com/luisalvs
