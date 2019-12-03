import pandas as pd

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
    empresas_df = load_dataset("CNPJ")
    return empresas_df


def load_licitacoes():
    licitacoes_df = load_dataset("Licitacao")
    licitacoes_df.columns = map(to_camel, licitacoes_df.columns)
    licitacoes_df = column_to_float(licitacoes_df, "valorLicitação")
    licitacoes_df = column_to_datetime(licitacoes_df, "dataResultadoCompra")
    licitacoes_df = column_to_datetime(licitacoes_df, "dataAbertura")
    
    return licitacoes_df


load_licitacoes()


def load_contratos():
    contratos_df = load_dataset("Compras")
    contratos_df.columns = map(to_camel, contratos_df.columns)

    contratos_df = column_to_float(contratos_df, "valorInicialCompra")
    contratos_df = column_to_float(contratos_df, "valorFinalCompra")
    contratos_df = column_to_datetime(contratos_df, "dataInícioVigência")
    contratos_df = column_to_datetime(contratos_df, "dataFimVigência")
    contratos_df = column_to_datetime(contratos_df, "dataAssinaturaContrato")
    contratos_df = column_to_datetime(contratos_df, "dataPublicaçãoDou")

    return contratos_df


def load_items_licitacao():
    items_licitacao_df = load_dataset("ItemLicitacao")
    items_licitacao_df.columns = map(to_camel, items_licitacao_df.columns)

    items_licitacao_df = column_to_float(items_licitacao_df, "valorItem")
    items_licitacao_df = column_to_int(items_licitacao_df, "quantidadeItem")

    return items_licitacao_df


def load_termos_aditivos():
    termos_aditivos_df = load_dataset("TermoAditivo")
    termos_aditivos_df.columns = map(to_camel, termos_aditivos_df.columns)
    termos_aditivos_df = column_to_datetime(termos_aditivos_df, "dataPublicação")

    return termos_aditivos_df


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
