from sqlalchemy import create_engine
import pandas as pd

class PgValue:
  def __init__(self, expr, driver):
    self.expr = expr
    self.driver = driver
    self.frame = None

  def to_sql(self):
    return self.driver.to_query(self.expr).get_sql()

  def to_pandas(self):
    if self.frame is None:
      engine = create_engine('postgresql+psycopg2://', creator=lambda: self.driver.connection)
      self.frame = pd.read_sql_query(self.to_sql(), engine)
    return self.frame
