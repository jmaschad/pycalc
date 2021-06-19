import unittest

from pycalc import dc, Scheduler
from mongo_driver import MongoDriver, MongoPipeline

class TestMongo(unittest.TestCase):

  def test_scan(self):
    memo = dc.scan("mon", "nation", as_="n").to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(MongoDriver("mon", dbname="tpch"))
    
    res = scheduler.schedule(memo)
    self.assertIsInstance(res.expr, MongoPipeline)
    pipeline = res.expr
    self.assertEqual(pipeline.collection, "nation")
    self.assertEqual(len(pipeline.stages), 0)
    
  def test_select_where(self):
    memo = dc.scan("mon", "lineitem", as_="l").filter(
      dc.ctx("l", "l_discount") < dc.float(0.3)
    ).select({
      "id": dc.ctx("l", "l_id"),
      "quantity": dc.ctx("l", "l_quantity"),
      "discount": dc.ctx("l", "l_discount")
    }).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(MongoDriver("mon", dbname="tpch"))
    
    res = scheduler.schedule(memo)
    self.assertIsInstance(res.expr, MongoPipeline)
    pipeline = res.expr
    self.assertEqual(pipeline.collection, "lineitem")
    self.assertEqual(pipeline.stages[0], {
      "$match": { "$expr": { "$lt": ["$l_discount", { "$literal": 0.3 }] }}
    })

  @unittest.skip("Requires an active MongoDB")
  def test_execute(self):
    memo = dc.scan("mon", "parts", as_="p").select({
      "manufacturer": dc.ctx("p", "category.manufacturer")
    }).to_memo()
    
    scheduler = Scheduler()
    scheduler.add_driver(MongoDriver("mon", dbname="catalog"))
    
    res = scheduler.schedule(memo)
    rows = list(res)
    self.assertTrue(rows)
    for row in res:
      self.assertEquals(list(row.keys()), ["_id", "manufacturer"])
