from insert_data import *
from queries.indexes import create_indexes
from queries.relationships import create_relationships

def main():
    insert_servidores()
    insert_empresas()
    insert_orgaos()
    insert_socios()
    insert_licitacoes()
    insert_items_licitacao()
    insert_participantes_licitacao()
    insert_contratos()
    insert_termos_aditivos()
    create_relationships()


if __name__ == '__main__':
    main()