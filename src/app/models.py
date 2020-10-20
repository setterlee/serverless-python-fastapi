from typing import Dict

# pylint: disable=no-name-in-module
from pydantic import BaseModel, Field
from typing import Optional

class InputExample(BaseModel):
    a: int = Field(..., title="Input value a")
    b: int = Field(..., title="Input value b")

class OutputExample(BaseModel):
    a: int = Field(..., title="Input value a")
    b: int = Field(..., title="Input value b")
    result: int = Field(..., title="Result of a * b")
