import json
from typing import Dict

from fastapi import APIRouter, Request
from fastapi.param_functions import Body

from utils.logger import logger as logging

ok_router = APIRouter()


@ok_router.get("/")
async def ok_endpoint(request: Request) -> Dict[str, str]:
    logging.info("ok endpoint called")

    headers = dict(request.headers)
    logging.info(f"request headers: {headers}")

    raw_body = await request.body()
    if raw_body:
        body = json.loads(raw_body)
        resp = body
        logging.info(f"request body: {body}")
    else:
        resp = {"message": "ok"}
        logging.info("request body is empty")

    logging.info(f"response: {resp}")
    return resp
