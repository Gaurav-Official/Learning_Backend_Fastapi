from fastapi import HTTPException
from typing import Optional, List

class ApiError(HTTPException):
    def __init__(
        self,
        status_code: int,
        message: str = "Something went wrong",
        errors: Optional[List] = None,
        stack: Optional[str] = None
    ):
        super().__init__(
            status_code=status_code,
            detail=message
        )

        self.errors = errors
        self.stack = stack
