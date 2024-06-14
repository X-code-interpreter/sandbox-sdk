import os

SANDBOX_REFRESH_PERIOD = 5  # seconds

TIMEOUT = 60


SECURE = os.getenv("SANDBOX_SDK_SECURE", "FALSE").upper() == "TRUE"
DEBUG = os.getenv("SANDBOX_SDK_DEBUG") or False
PROTOCOL = "https" if SECURE and not DEBUG else "http"


# BACKEND_ADDR is used to
# 1. connect to service inside sandbox
# 2. connect to orchestrator to manage the sandbox
BACKEND_ADDR = os.getenv("SANDBOX_BACKEND_ADDR") or "39.105.171.207"
# SANDBOX_PORT is used to connect to service inside sandbox
SANDBOX_PORT = os.getenv("SANDBOX_PROXY_PORT") or 6666
# ORCHESTRATOR_PORT is used to connect to orchestrator
ORCHESTRATOR_PORT = 5000
GUEST_KERNEL_VERSION = "5.10.186"

ENVD_PORT = 49982
WS_ROUTE = "/ws"
FILE_ROUTE = "/file"
