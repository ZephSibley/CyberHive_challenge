from typing import List

from fastapi import FastAPI, Request, Response

app = FastAPI()

ORIGIN_WHITELIST = ['']


@app.middleware("http")
async def check_origin_whitelist(request: Request, call_next):
    if request.client.host not in ORIGIN_WHITELIST:
        response = Response(status_code=401)
    else:
        response = await call_next(request)
    return response


@app.post("/")
async def root(process_list: List):
    with open('process_log.log', 'a') as file:
        file.write(str(process_list) + '\n')
