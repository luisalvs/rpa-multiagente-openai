import re
import httpx


API_BASE = "http://127.0.0.1:8002"


def consultar_api_rpa(codigo: str, recurso: str = "status") -> dict:

    codigo = codigo.strip().upper()

    if not re.fullmatch(r"RPA-\d{3}", codigo):
        return {
            "codigo": codigo,
            "erro": "CODIGO_INVALIDO",
            "mensagem": "Utilize o formato RPA-101."
        }

    if recurso not in ("status", "logs"):
        return {
            "codigo": codigo,
            "erro": "RECURSO_INVALIDO"
        }

    if recurso == "status":
        endpoint = f"{API_BASE}/rpas/{codigo}"
    else:
        endpoint = f"{API_BASE}/rpas/{codigo}/logs"

    try:
        response = httpx.get(
            endpoint,
            timeout=5.0
        )

        if response.status_code == 404:
            return {
                "codigo": codigo,
                "status": "NAO_ENCONTRADO"
            }

        response.raise_for_status()

        dados = response.json()

        if not isinstance(dados, dict):
            return {
                "codigo": codigo,
                "erro": "RESPOSTA_INVALIDA"
            }

        return dados

    except httpx.TimeoutException:
        return {
            "codigo": codigo,
            "erro": "TIMEOUT_API",
            "mensagem": "A API demorou para responder."
        }

    except httpx.HTTPStatusError as erro:
        return {
            "codigo": codigo,
            "erro": "ERRO_HTTP",
            "status_http": erro.response.status_code
        }

    except httpx.RequestError:
        return {
            "codigo": codigo,
            "erro": "FALHA_CONEXAO",
            "mensagem": "Não foi possível acessar a API."
        }

    except ValueError:
        return {
            "codigo": codigo,
            "erro": "JSON_INVALIDO"
        }
