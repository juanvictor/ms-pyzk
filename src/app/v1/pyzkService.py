from fastapi import Depends
from zk import ZK

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

    response.error    = False
    response.message  = 'Se logró obtener la fecha y hora del biométrico' + ip + '.'
    response.response = time
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