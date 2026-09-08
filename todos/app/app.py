from fastapi import FastAPI

from app.core.database import create_table
from app.routes.todo_routes import router

app = FastAPI(
    title = "Todo API"
)

create_table()

app.include_router(router)