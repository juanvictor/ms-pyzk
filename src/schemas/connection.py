from pydantic import BaseModel

class Connection(BaseModel):
  ip: str
  port: int = 4370
  timeout: int = 5
