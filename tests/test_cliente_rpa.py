import httpx
from cliente_rpa import consultar_api_rpa

def test_consultar_status_sucesso(monkeypatch):

    def mock_get(url, timeout):
        assert url.endswith("/rpas/RPA-101")

        return httpx.Response(
            status_code=200,
            json={
                "codigo": "RPA-101",
                "status": "CONCLUIDO"
            },
            request=httpx.Request("GET", url)
        )

    monkeypatch.setattr(httpx, "get", mock_get)

    resultado = consultar_api_rpa("rpa-101")

    assert resultado["codigo"] == "RPA-101"
    assert resultado["status"] == "CONCLUIDO"


def test_consultar_logs_sucesso(monkeypatch):

    def mock_get(url, timeout):
        assert url.endswith("/rpas/RPA-103/logs")

        return httpx.Response(
            status_code=200,
            json={
                "codigo": "RPA-103",
                "erro": "Timeout externo"
            },
            request=httpx.Request("GET", url)
        )

    monkeypatch.setattr(httpx, "get", mock_get)

    resultado = consultar_api_rpa(
        "RPA-103",
        recurso="logs"
    )

    assert resultado["erro"] == "Timeout externo"


def test_codigo_invalido(monkeypatch):

    def falhar_se_chamar_http(*args, **kwargs):
        raise AssertionError(
            "Código inválido não deve chamar HTTP."
        )

    monkeypatch.setattr(
        httpx, "get", falhar_se_chamar_http
    )

    resultado = consultar_api_rpa("RPA-ABC")

    assert resultado["erro"] == "CODIGO_INVALIDO"


def test_rpa_nao_encontrada(monkeypatch):

    def mock_get(url, timeout):
        return httpx.Response(
            status_code=404,
            request=httpx.Request("GET", url)
        )

    monkeypatch.setattr(httpx, "get", mock_get)

    resultado = consultar_api_rpa("RPA-999")

    assert resultado["status"] == "NAO_ENCONTRADO"


def test_api_indisponivel(monkeypatch):

    def mock_get(url, timeout):
        raise httpx.ConnectError(
            "Conexão recusada",
            request=httpx.Request("GET", url)
        )

    monkeypatch.setattr(httpx, "get", mock_get)

    resultado = consultar_api_rpa("RPA-101")

    assert resultado["erro"] == "FALHA_CONEXAO"


def test_timeout_api(monkeypatch):

    def mock_get(url, timeout):
        raise httpx.ReadTimeout(
            "Tempo limite excedido",
            request=httpx.Request("GET", url)
        )

    monkeypatch.setattr(httpx, "get", mock_get)

    resultado = consultar_api_rpa("RPA-103")

    assert resultado["erro"] == "TIMEOUT_API"


def test_recurso_invalido(monkeypatch):

    def falhar_se_chamar_http(*args, **kwargs):
        raise AssertionError(
            "Recurso inválido não deve chamar HTTP."
        )

    monkeypatch.setattr(
        httpx, "get", falhar_se_chamar_http
    )

    resultado = consultar_api_rpa(
        "RPA-101",
        recurso="excluir"
    )

    assert resultado["erro"] == "RECURSO_INVALIDO"
