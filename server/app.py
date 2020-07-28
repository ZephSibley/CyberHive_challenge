from typing import List

from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def root(process_list: List):
    with open('process_log.txt', 'a') as file:
        file.write(str(process_list) + '\n')
