from pydantic import BaseModel

class todosSchema(BaseModel):
    title: str
    description: str
