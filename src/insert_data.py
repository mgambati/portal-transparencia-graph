import json

from db import run_queries
from loaders import *
from nodes import *


def insert_servidores():
    servidores_df = load_servidores()
    run_queries(servidores_df, add_servidor, "Servidores")


def insert_empresas():
    empresas_df = load_empresas()
    run_queries(empresas_df, add_empresa, "Empresas")


def insert_orgaos():
    orgaos_df = load_orgaos()
    run_queries(orgaos_df, add_orgao, "Orgãos")


def insert_licitacoes():
    licitacoes_df = load_licitacoes()
    run_queries(licitacoes_df, add_licitacao, "Licitações")


def insert_contratos():
    contratos_df = load_contratos()
    run_queries(contratos_df, add_contrato, "Contratos")


def insert_items_licitacao():
    items_licitacao_df = load_items_licitacao()
    run_queries(items_licitacao_df, add_items_licitacao, "Items Licitação")


def insert_termos_aditivos():
    termos_aditivos_df = load_termos_aditivos()
    run_queries(termos_aditivos_df, add_termo_aditivo, "Termos Aditivos")


def insert_participantes_licitacao():
    participantes_licitacao_df = load_participantes_licitacao()
    run_queries(
        participantes_licitacao_df,
        add_participante_licitacao,
        "Participantes Licitação",
    )


def insert_socios():
    socios_df = load_socios()
    run_queries(socios_df, add_socio, "Sócios")
