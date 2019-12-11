import pandas as pd
import mmh3

from utils import (
    column_to_datetime,
    column_to_float,
    column_to_int,
    load_dataset,
    to_camel,
    remove_cnpj_formating,
    hash_nome_cpf,
)


def load_servidores():
    df = load_dataset("Cadastro")
    df["id"] = df.apply(lambda x: hash_nome_cpf(x["nome"], x["cpf"]), axis=1)

    return df


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


def load_socios():
    df = load_dataset("Socios")
    df.columns = map(to_camel, df.columns)
    df = df.rename(columns={"cpf-cnpj": "cpfCnpj"})
    df["nome"] = df["nome"].astype(str)
    df["cpfCnpj"] = df["cpfCnpj"].astype(str)
    df["cpfCnpj"] = df["cpfCnpj"].map(remove_cnpj_formating)

    df["servidorId"] = df.apply(
        lambda x: hash_nome_cpf(x["nome"], x["cpfCnpj"]), axis=1
    )

    return df


def load_licitacoes():
    df = load_dataset("Licitacao")
    df.columns = map(to_camel, df.columns)
    df = column_to_float(df, "valorLicitação")
    df = column_to_datetime(df, "dataResultadoCompra")
    df = column_to_datetime(df, "dataAbertura")

    df["id"] = df.apply(
        lambda x: mmh3.hash(x["númeroLicitação"] + x["númeroProcesso"] + x["códigoUg"]),
        axis=1,
    )

    return df.drop_duplicates(subset='id', keep='last')


def load_contratos():
    df = load_dataset("Compras")
    df.columns = map(to_camel, df.columns)

    df = column_to_float(df, "valorInicialCompra")
    df = column_to_float(df, "valorFinalCompra")
    df = column_to_datetime(df, "dataInícioVigência")
    df = column_to_datetime(df, "dataFimVigência")
    df = column_to_datetime(df, "dataAssinaturaContrato")
    df = column_to_datetime(df, "dataPublicaçãoDou")

    df["id"] = df.apply(
        lambda x: mmh3.hash(x["númeroDoContrato"] + x["códigoUg"] + x["objeto"]), axis=1
    )

    return df.drop_duplicates(subset='id', keep='last')


def load_items_licitacao():
    df = load_dataset("ItemLicitacao")
    df.columns = map(to_camel, df.columns)
    df = column_to_float(df, "valorItem")
    df = column_to_int(df, "quantidadeItem")
    df["licitacaoId"] = df.apply(
        lambda x: mmh3.hash(x["númeroLicitação"] + x["númeroProcesso"] + x["códigoUg"]),
        axis=1,
    )

    return df



def load_termos_aditivos():
    df = load_dataset("TermoAditivo")
    df.columns = map(to_camel, df.columns)
    df = column_to_datetime(df, "dataPublicação")

    return df


def load_participantes_licitacao():
    df = load_dataset("ParticipantesLicitacao")
    df.columns = map(to_camel, df.columns)

    df["flagVencedor"] = df["flagVencedor"].map({"NÃO": False, "SIM": True})

    df["licitacaoId"] = df.apply(
        lambda x: mmh3.hash(x["númeroLicitação"] + x["númeroProcesso"] + x["códigoUg"]),
        axis=1,
    )

    return df
