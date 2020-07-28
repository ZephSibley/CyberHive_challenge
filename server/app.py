from typing import List

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

ORIGIN_WHITELIST = ['127.0.0.1']


class RunningProcessesSnapshot(BaseModel):
    running_processes: List
    timestamp: str


app = FastAPI()


@app.middleware("http")
async def check_origin_whitelist(request: Request, call_next):
    if request.client.host not in ORIGIN_WHITELIST:
        return Response(status_code=401)
    return await call_next(request)


@app.post("/")
async def root(p: RunningProcessesSnapshot):
    with open('process_log.log', 'a') as file:
        file.write(
            "%s %s \n" %
            (p.timestamp, str(p.running_processes))
        )

