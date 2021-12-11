from typing import Optional
from fastapi import FastAPI, Request
from datetime import datetime, timezone, timedelta
import socket
#import logging

app = FastAPI()
tz = timezone(timedelta(hours=+8))

#logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
#logger = logging.getLogger(__name__)

@app.get("/v1/status")
def read_v1_status(request: Request):
    print("INFO:     (Request from reverse proxy)Client: ",request.headers.get("x-forwarded-for")) # must be lowwer case
    #logger.info("(Request from reverse proxy)Client: ", request.headers.get("x-forwarded-for"))
    return {"hostname": socket.gethostname(), "status": "ok", "time": datetime.now(tz)}
