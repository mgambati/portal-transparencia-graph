import db


def create_relationships():
    with db.connect() as driver:
        queries = [
            "MATCH (org:Orgao), (licitacao:Licitacao {orgId:org.id}) CREATE (org)-[:LICITOU]->(licitacao)",
            "MATCH (o:Orgao), (s:Servidor { orgExercicioId: o.id }) CREATE (s)-[:TRABALHA]->(o)",
        ]

        with driver.session() as session:
            tx = session.begin_transaction()
            for query in queries:
                tx.run(query)
            tx.commit()
