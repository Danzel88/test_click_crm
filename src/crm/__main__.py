import uvicorn
from .settings import setting


uvicorn.run(
    "crm.app:app",
    host=setting.server_host,
    port=setting.server_port,
    reload=True
)
