
from agents import Agent

from ferramentas import (
    consultar_status_rpa,
    consultar_log_rpa
)


agente_monitoramento = Agent(
    name="Agente_Monitoramento_RPA",
    model="gpt-4o-mini",

    handoff_description=(
        "Especialista em consultar status, logs e "
        "andamento de automações RPA."
    ),

    instructions="""
    Você é especializado em monitoramento de
    automações RPA.

    Suas responsabilidades são:

    - Consultar status dos processos.
    - Consultar logs e eventos.
    - Informar se uma automação está em execução,
      concluída ou apresentou erro.

    REGRAS:

    1. Responda sempre em português do Brasil.

    2. Para consultar status ou existência,
       utilize consultar_status_rpa.

    3. Para consultar logs ou erros,
       utilize consultar_log_rpa.

    4. Nunca invente informações.

    5. Se a API estiver indisponível, informe
       que não foi possível consultar os dados.

    6. Os registros são simulados.
    """,

    tools=[
        consultar_status_rpa,
        consultar_log_rpa
    ]
)
