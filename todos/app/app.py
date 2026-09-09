from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.exception.todo_exception import TodoNotFoundError
from app.core.database import create_table
from app.routes.todo_routes import router

app = FastAPI(
    title = "Todo API"
)

@app.exception_handler(TodoNotFoundError)
async def todo_not_found_error(request : Request, exc : TodoNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"details" : str(exc)}
    )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error. Please try again later."}
    )

create_table()

app.include_router(router)