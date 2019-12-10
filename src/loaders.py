import pandas as pd
import mmh3

from utils import (
    column_to_datetime,
    column_to_float,
    column_to_int,
    load_dataset,
    to_camel,
)


def load_servidores():
    servidores_df = load_dataset("Cadastro")

    servidores_df["nome_cpf"] = servidores_df["nome"] + servidores_df["cpf"]

    return servidores_df


def load_orgaos():
    servidores_df = load_servidores()
    columns = ["cod_org_exercicio", "org_exercicio", "cod_orgsup_exercicio"]
    df_orgaos = (
        servidores_df.groupby(columns).size().reset_index(name="total_funcionarios")
    )

    return df_orgaos


def load_empresas():
    df = load_dataset("CNPJ")

    return df


def load_licitacoes():
    df = load_dataset("Licitacao")
    df.columns = map(to_camel, df.columns)
    df = column_to_float(df, "valorLicitação")
    df = column_to_datetime(df, "dataResultadoCompra")
    df = column_to_datetime(df, "dataAbertura")
    df["id"] = df["númeroLicitação"] + df["númeroProcesso"] + df["códigoUg"]
    df["id"] = df["id"].map(mmh3.hash)

    return df


# cnpjContratado pode ser um cnpj ou cpf
def load_contratos():
    df = load_dataset("Compras")
    df.columns = map(to_camel, df.columns)

    df = column_to_float(df, "valorInicialCompra")
    df = column_to_float(df, "valorFinalCompra")
    df = column_to_datetime(df, "dataInícioVigência")
    df = column_to_datetime(df, "dataFimVigência")
    df = column_to_datetime(df, "dataAssinaturaContrato")
    df = column_to_datetime(df, "dataPublicaçãoDou")

    df["id"] = df["númeroDoContrato"] + df["códigoUg"] + df["objeto"]
    df["id"] = df["id"].map(mmh3.hash)

    return df


def load_items_licitacao():
    items_licitacao_df = load_dataset("ItemLicitacao")
    items_licitacao_df.columns = map(to_camel, items_licitacao_df.columns)

    items_licitacao_df = column_to_float(items_licitacao_df, "valorItem")
    items_licitacao_df = column_to_int(items_licitacao_df, "quantidadeItem")

    return items_licitacao_df


def load_termos_aditivos():
    df = load_dataset("TermoAditivo")
    df.columns = map(to_camel, df.columns)
    df = column_to_datetime(df, "dataPublicação")

    print(df.sample(10))
    return df

load_termos_aditivos()

def load_participantes_licitacao():
    participantes_licitacao_df = load_dataset("ParticipantesLicitacao")
    participantes_licitacao_df.columns = map(
        to_camel, participantes_licitacao_df.columns
    )

    participantes_licitacao_df["flagVencedor"] = participantes_licitacao_df[
        "flagVencedor"
    ].map({"NÃO": False, "SIM": True})

    return participantes_licitacao_df


def load_socios():
    socios_df = load_dataset("Socios")
    socios_df.columns = map(to_camel, socios_df.columns)
    socios_df = socios_df.rename(columns={"cpf-cnpj": "cpfCnpj"})

    return socios_df
