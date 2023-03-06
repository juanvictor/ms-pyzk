from pydantic import BaseModel

class Response(BaseModel):
  error  : bool    = True
  message: str     = 'Existe problemas en el servicio.'
  response         = {}
  status : int     = 422
