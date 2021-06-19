import unittest

from pycalc import dc, Scheduler
from pg_driver import PgDriver

class TestPG(unittest.TestCase):

  def test_scan(self):
    memo = dc.scan("pg", "nation", as_="n").to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(PgDriver("pg"))
    
    res = scheduler.schedule(memo)
    self.assertEqual(res.to_sql(), '''SELECT * FROM "nation" "n"''')

  def test_select_from_where(self):
    memo = dc.scan("pg", "nation", as_="n").cross_join(
      dc.scan("pg", "region", as_="r")
    ).filter(
      dc.ctx("n", "nationkey") == dc.ctx("r", "nationkey")
    ).select({
      "nation": dc.ctx("n", "name"),
      "region": dc.ctx("r", "name")
    }).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(PgDriver("pg"))
    
    res = scheduler.schedule(memo)
    self.assertEqual(
      res.to_sql(), 
      ('''SELECT "n"."name" "nation","r"."name" "region" ''' +
      '''FROM "nation" "n","region" "r" ''' +
      '''WHERE "n"."nationkey"="r"."nationkey"''')
    )

  @unittest.skip("Requires an active PostgreSQL with tpc-h data")
  def test_execute(self):
    memo = dc.scan("pg", "items", as_="i").filter(
      dc.ctx("i", "extended_price") < dc.float(5000)
    ).select({
      "price": dc.ctx("i", "extended_price")
    }).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(PgDriver("pg", dbname="items"))
    
    res = scheduler.schedule(memo)
    self.assertIsNotNone(res)  
    for row in res:
      row["price"] < 5000
