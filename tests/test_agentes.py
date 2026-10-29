
from agentes.coordenador import agente_coordenador
from agentes.monitoramento import agente_monitoramento
from agentes.diagnostico import agente_diagnostico


def test_coordenador_possui_dois_handoffs():

    assert len(agente_coordenador.handoffs) == 2

    assert agente_monitoramento in (
        agente_coordenador.handoffs
    )

    assert agente_diagnostico in (
        agente_coordenador.handoffs
    )


def test_monitoramento_possui_ferramentas():

    nomes = [
        ferramenta.name
        for ferramenta in agente_monitoramento.tools
    ]

    assert "consultar_status_rpa" in nomes
    assert "consultar_log_rpa" in nomes


def test_diagnostico_possui_ferramentas():

    nomes = [
        ferramenta.name
        for ferramenta in agente_diagnostico.tools
    ]

    assert "consultar_status_rpa" in nomes
    assert "consultar_log_rpa" in nomes


def test_agentes_possuem_responsabilidades():

    assert agente_coordenador.name == "Coordenador_RPA"

    assert (
        agente_monitoramento.name
        == "Agente_Monitoramento_RPA"
    )

    assert (
        agente_diagnostico.name
        == "Agente_Diagnostico_RPA"
    )
