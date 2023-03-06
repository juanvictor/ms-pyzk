from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime

from app.v1.pyzkRoute import routerV1
from schemas.response import Response

app = FastAPI(
  title = 'ms-pyzk',
  description = 'Microservicio para gestionar dispositivos ZK',
  version = '0.0.1',
  # terms_of_service = "https://ms-pyzk.jvsc.com",
  contact = {
    'name' : 'Juan Victor Serrudo Chavez',
    'url'  : 'https://www.linkedin.com/in/juan-victor-serrudo-chavez-437a21211/',
    'email': 'juan.vsc@gmail.com',
  },
  license_info = {
    'name': 'MIT',
    'url' : 'https://opensource.org/licenses/MIT',
  },
  openapi_tags = [
    {
      'name'       : 'Home',
      'description': 'Servicios que permite opciones del servicio.',
    },
    {
      'name'        : 'PyZK',
      'description' : 'Servicios de la libreria PyZK.',
      'externalDocs': {
          'description': 'Documentación PyZK',
          'url'        : 'https://pyzk.readthedocs.io/en/stable',
      },
    }
  ],
  docs_url = '/api'
)

@app.get(
  '/',
  tags           = ['Home'],
  summary        = 'Servicio para verificar ms-pyzk',
  response_model = Response,
  status_code    = status.HTTP_422_UNPROCESSABLE_ENTITY
)
def getHome():
  # VARIABLE INITIALIZATION
  response = {
    'error'   : True,
    'message' : 'Existe problemas en el servicio getHome.',
    'response': {},
    'status'  : 422,
  }

  # OPERATION
  response['error']    = False
  response['message']  = 'Bienvenido a MS-PYZK, basado ​​en principios REST, devuelve metadatos JSON - Copyright © Juan Victor Serrudo Chavez'
  response['response'] = {
    'nameApp'       : 'ms-pyzk',
    'version'       : '0.0.1',
    # 'dateTimeServer': (datetime.now()).strftime('%Y-%m-%d %H:%M:%S'),
    'dateTimeServer': (datetime.now()).isoformat()
  }
  response['status']   = 200

  # RESPONSE
  return JSONResponse(
    content     = response,
    status_code = response['status']
  )

app.include_router( routerV1 )
