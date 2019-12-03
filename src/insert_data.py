import json

from loaders import (
    load_contratos,
    load_empresas,
    load_items_licitacao,
    load_licitacoes,
    load_orgaos,
    load_participantes_licitacao,
    load_servidores,
    load_termos_aditivos,
    load_socios
)

from queries import (
    create_contrato_node,
    create_empresa_node,
    create_items_licitacao_node,
    create_licitacao_node,
    create_orgao_node,
    create_participante_licitacao_node,
    create_servidor_node,
    create_termo_aditivo_node,
    create_socio_node
)
from utils import run_queries, to_neotime_date


def insert_servidores():
    servidores_df = load_servidores()
    run_queries(servidores_df, create_servidor_node, 'Servidores')


def insert_empresas():
    empresas_df = load_empresas()
    run_queries(empresas_df, create_empresa_node, 'Empresas')


def insert_orgaos():
    orgaos_df = load_orgaos()
    run_queries(orgaos_df, create_orgao_node, 'Orgãos')


def insert_licitacoes():
    licitacoes_df = load_licitacoes()
    run_queries(licitacoes_df, create_licitacao_node, 'Licitações')


def insert_contratos():
    contratos_df = load_contratos()
    run_queries(contratos_df, create_contrato_node, 'Contratos')


def insert_items_licitacao():
    items_licitacao_df = load_items_licitacao()
    run_queries(items_licitacao_df, create_items_licitacao_node, 'Items Licitação')


def insert_termos_aditivos():
    termos_aditivos_df = load_termos_aditivos()
    run_queries(termos_aditivos_df, create_termo_aditivo_node, 'Termos Aditivos')


def insert_participantes_licitacao():
    participantes_licitacao_df = load_participantes_licitacao()
    run_queries(participantes_licitacao_df, create_participante_licitacao_node, 'Participantes Licitação')


def insert_socios():
    socios_df = load_socios()
    run_queries(socios_df, create_socio_node, 'Sócios')