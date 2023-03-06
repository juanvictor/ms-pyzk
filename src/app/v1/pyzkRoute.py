from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from zk import ZK

routerV1 = APIRouter()
tag = 'PyZK'

async def zkServiceV1(ip: str, port: int = 4370, timeout: int = 5):
  # VARIABLE INITIALIZATION
  response = {
    'error'   : True,
    'message' : 'Existe problemas en el servicio zkServiceV1.',
    'response': {},
    'status'  : 422,
  }

  zk   = ZK(ip, port = port, timeout = timeout)
  conn = None

  # OPERATION
  try:
    conn = zk.connect()
    time = conn.get_time()
    conn.enable_device()

    print(time)

    response.error    = False
    response.message  = 'Se logró obtener la fecha y hora del biométrico' + ip + '.'
    response.response = conn
    response.status   = 200
  except Exception as e:
    response.error    = True
    response.message  = 'Error de conexión al biométrico ' + ip + '.'
    response.response = e.args
    response.status   = 500
  finally:
    if conn:
        conn.disconnect()


  # RESPONSE
  return response

@routerV1.get(
  '/v1/get-time',
  tags = [tag],
  summary = 'Servicio para obtener la fecha y la hora del dispositivo biométrico.'
)
async def getTimeRouteV1( response: dict = Depends(zkServiceV1)):
  # VARIABLE INITIALIZATION
  # response = {
  #   'error'   : True,
  #   'message' : 'Existe problemas en el servicio getTimeRouteV1.',
  #   'response': {},
  #   'status'  : 422,
  # }

  # OPERATION
  # getTimeServiceV1()

  # RESPONSE
  return JSONResponse(
    content     = response,
    status_code = response['status']
  )
