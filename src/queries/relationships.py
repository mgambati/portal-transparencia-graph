import db


def create_relationships():
    with db.connect() as driver:
        queries = [
            "MATCH (org:Orgao), (licitacao:Licitacao { orgId:org.id }) CREATE (org)-[:LICITOU]->(licitacao)",
            "MATCH (o:Orgao), (c:Contrato { orgId:o.id }) CREATE (o)-[:ASSINOU]->(c)",
            "MATCH (o:Orgao), (s:Servidor { orgId: o.id }) CREATE (s)-[:TRABALHA]->(o)",
            "MATCH (c:Contrato), (e:Empresa { cnpj: c.cnpjContratado }) CREATE (e)-[:CONTRATADO]->(c)",
            "MATCH (l:Licitacao), (il:ItemLicitacao { licitacao: l.licitacao, processo: l.processo }) CREATE (l)-[:POSSUI]->(il)",
            "MATCH (c:Contrato), (ta:TermoAditivo { contrato: c.numero }) CREATE (c)-[:PUBLICOU]->(ta)",
        ]

        with driver.session() as session:
            tx = session.begin_transaction()
            for query in queries:
                tx.run(query)
            tx.commit()
