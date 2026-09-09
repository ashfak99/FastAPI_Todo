from pydantic import BaseModel

class todosSchema(BaseModel):
    title : str
    description : str

class TodoPatchSchema(BaseModel):
    title : str | None=None
    description : str | None=None
    completed : bool | None=None

class TodoPutSchema(BaseModel):
    title : str
    description : str
    completed : bool

class TodoResponseSchema(BaseModel):
    id : int
    title : str
    description : str
    completed : bool
