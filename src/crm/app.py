from fastapi import FastAPI
from .api import router

app = FastAPI(title="Click Crm", description="Тестовое задание. Выполнил Денис Иванов")
app.include_router(router)
