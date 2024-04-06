import json


class DB:
  def __init__(self) -> None:
    self.db = {}
    
    try:
      self.__load__()
    except:
      pass

  def __getitem__(self, key):
    return self.db[key]

  def __setitem__(self, key, value):
    if key not in self.db:
      self.db[key] = value
      return True
    else:
      return False

  def __delitem__(self, key):
    del self.db[key]

  def __clear__(self):
    self.db.clear()

  def __save__(self):
    with open("S:\\Currency_Bot\\db.json", "w") as file:
      json.dump(self.db, file)

  def __load__(self):
    with open("S:\\Currency_Bot\\db.json", "r") as file:
      self.db = json.load(file)
