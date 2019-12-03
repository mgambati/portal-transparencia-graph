from insert_data import (
    insert_contratos,
    insert_empresas,
    insert_items_licitacao,
    insert_licitacoes,
    insert_orgaos,
    insert_participantes_licitacao,
    insert_servidores,
    insert_socios,
)
from indexes import create_indexes

def main():
    insert_servidores()
    insert_empresas()
    insert_orgaos()
    insert_socios()
    insert_licitacoes()
    insert_items_licitacao()
    insert_participantes_licitacao()
    insert_contratos()
    create_indexes()

main()
