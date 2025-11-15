import os
from typing import Dict

import uvicorn
from fastapi import FastAPI, Request

from controllers.ok_controller import ok_router


def main() -> None:
    if "SERVER_PORT" in os.environ:
        server_port = int(os.environ["SERVER_PORT"])
    else:
        server_port = 8000

    app: FastAPI = FastAPI()
    app.include_router(ok_router)
    uvicorn.run(app, host="0.0.0.0", port=server_port, log_config=None)


if __name__ == "__main__":
    main()
