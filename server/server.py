import uvicorn
from fastapi import FastAPI, Request, Response

from models.RunningProcessSnapshot import RunningProcessesSnapshot

ORIGIN_WHITELIST = ['127.0.0.1', 'testclient']

app = FastAPI()


@app.middleware("http")
async def check_origin_whitelist(request: Request, call_next):
    if request.client.host not in ORIGIN_WHITELIST:
        return Response(status_code=401)
    return await call_next(request)


@app.post("/")
async def root(p: RunningProcessesSnapshot, request: Request):
    log_file_name = '%s.log' % request.client.host
    with open(log_file_name, 'a') as file:
        file.write(
            "%s %s \n" %
            (p.timestamp, str(p.running_processes))
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
