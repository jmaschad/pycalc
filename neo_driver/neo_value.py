import pandas as pd

class NeoValue:
  def __init__(self, expr, driver):
    self.expr = expr
    self.driver = driver
    self.frame = None
  
  def to_pandas(self):
    if self.frame is None:
      with self.driver.connection.session() as sess:
        query = self.expr.to_cypher()
        result = sess.run(query)
        self.frame = pd.DataFrame.from_records(list(result), columns=result.keys())
    return self.frame
