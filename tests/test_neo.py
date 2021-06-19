import unittest

from pycalc import dc, Scheduler
from neo_driver import NeoDriver

class TestNeo(unittest.TestCase):

  def test_match(self):
    memo = dc.match(
        "neo",
        dc.node("a", "Person").rel("ACTED_IN").to(dc.node("m", "Movie"))
    ).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(NeoDriver("neo"))
    
    res = scheduler.schedule(memo)
    self.assertEqual(res.expr.to_cypher(), '''MATCH (a:Person)-[:ACTED_IN]->(m:Movie) RETURN a, m''')
    
  def test_match_select_where(self):
    memo = dc.match(
      "neo",
      dc.node("a", "Person").rel("ACTED_IN").to(dc.node("m", "Movie")),
      dc.node("d", "Person").rel("DIRECTED").to(dc.node("m"))
    ).filter(
        dc.ctx("m", "title") == dc.string("The Matrix")
    ).select({
      "actor": dc.ctx("a", "name"),
      "director": dc.ctx("d", "name")
    }).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(NeoDriver("neo"))
    
    res = scheduler.schedule(memo)
    self.assertEqual(
      res.expr.to_cypher(), (
        '''MATCH (a:Person)-[:ACTED_IN]->(m:Movie), (d:Person)-[:DIRECTED]->(m) ''' +
        '''WHERE m.title = "The Matrix" ''' +
        '''RETURN a.name AS actor, d.name AS director'''
      )
    )

  @unittest.skip("Requires an active Neo4j")
  def test_execute(self):
    memo = dc.match(
      "neo",
      dc.node("c", "Customer").rel("REGISTERED_IN").to(dc.node("n", "Nation"))
    ).select({
      "customer": dc.ctx("c", "name"),
      "nation": dc.ctx("n", "name")
    }).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(NeoDriver("neo", "bolt://localhost:7687", auth=("neo4j", "pycalc"), encrypted=False))
    
    res = scheduler.schedule(memo)
    rows = list(res)
    self.assertIsNotNone(rows)
    for row in res:
      self.assertEquals(list(row.keys()), ["customer", "nation"])
