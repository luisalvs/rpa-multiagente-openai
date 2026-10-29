
from agents import Agent
from agentes.monitoramento import agente_monitoramento
from agentes.diagnostico import agente_diagnostico


agente_coordenador = Agent(
    name="Coordenador_RPA",
    model="gpt-4o-mini",

    instructions="""
    Você é o coordenador de uma equipe de
    agentes especializados em RPA.

    Sua responsabilidade é identificar
    qual especialista deve atender o usuário.

    REGRAS:

    1. Perguntas sobre status, logs, existência
       ou andamento de automações devem ser
       encaminhadas ao Agente de Monitoramento RPA.

    2. Perguntas sobre causas de falhas,
       investigação, diagnóstico ou possíveis
       soluções devem ser encaminhadas
       ao Agente de Diagnóstico RPA.

    3. Se a solicitação incluir status e
       diagnóstico de um erro, escolha
       o Agente de Diagnóstico RPA.

    4. Não invente dados de processos.

    5. Se faltar o código necessário para
       consultar uma automação, solicite-o.

    6. Responda em português do Brasil.
    """,

    handoffs=[
        agente_monitoramento,
        agente_diagnostico
    ]
)
