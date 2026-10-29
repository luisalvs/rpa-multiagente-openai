
import os
from dotenv import load_dotenv
from agents import Runner
from agentes.coordenador import agente_coordenador

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "Configure OPENAI_API_KEY no arquivo .env"
    )


def main():

    print("=" * 55)
    print("SISTEMA MULTIAGENTE RPA - OPENAI AGENTS SDK")
    print("=" * 55)
    print("Digite 'sair' para encerrar.")

    while True:

        pergunta = input(
            "\nDigite sua pergunta: "
        ).strip()

        if pergunta.lower() == "sair":
            break

        if not pergunta:
            continue

        try:

            resultado = Runner.run_sync(
                agente_coordenador,
                pergunta,
                max_turns=8
            )

            print("\n" + "=" * 55)
            print(
                f"[AGENTE RESPONSÁVEL] "
                f"{resultado.last_agent.name}"
            )
            print("=" * 55)

            print("\nRESPOSTA:")
            print(resultado.final_output)

        except Exception as erro:

            print(
                f"Erro: {type(erro).__name__}: {erro}"
            )


if __name__ == "__main__":
    main()
