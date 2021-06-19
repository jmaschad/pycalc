import pandas as pd

class MongoPipeline:
    def __init__(self, collection):
        self.collection = collection
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def __str__(self):
        if not self.stages:
            return self.collection + '.find()'
        else:
            return self.collection + '.aggregate(' + str(self.stages) + ')'

class MongoValue:
  def __init__(self, expr, driver):
    self.expr = expr
    self.driver = driver
    self.frame = None

  def to_pandas(self):
    if self.frame is None:
      if not isinstance(self.expr, MongoPipeline):
        raise RuntimeError
      pipeline = self.expr
      coll = self.driver.database[pipeline.collection]
      cursor = coll.aggregate(pipeline.stages) if pipeline.stages else coll.find()
      frame = pd.DataFrame.from_records(list(cursor))
      del frame['_id']
      self.frame = frame

    return frame
