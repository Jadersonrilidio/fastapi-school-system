from pydantic import BaseModel


class DeleteResponse(BaseModel):
    """
    Basic delete entity from database response.

    Params:
        - success : bool
        - message : str

    """
    success: bool
    message: str
