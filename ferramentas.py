
from agents import function_tool
from cliente_rpa import consultar_api_rpa


@function_tool
def consultar_status_rpa(codigo: str) -> dict:
    """
    Consulta o status atualizado de uma automação RPA
    através da API de monitoramento.

    Args:
        codigo: Código da automação, como RPA-103.
    """

    print(f"[TOOL HTTP] Consultando status: {codigo}")

    resultado = consultar_api_rpa(
        codigo=codigo,
        recurso="status"
    )

    return resultado


@function_tool
def consultar_log_rpa(codigo: str) -> dict:
    """
    Consulta os logs e possíveis erros de uma
    automação RPA através da API de monitoramento.

    Args:
        codigo: Código da automação, como RPA-103.
    """

    print(f"[TOOL HTTP] Consultando logs: {codigo}")

    resultado = consultar_api_rpa(
        codigo=codigo,
        recurso="logs"
    )

    return resultado
