from typing import List
from pydantic import BaseModel


class RunningProcessesSnapshot(BaseModel):
    running_processes: List
    timestamp: str
