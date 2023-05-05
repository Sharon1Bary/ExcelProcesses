from dataclasses import dataclass
from pydantic import BaseModel, validator
from uuid import UUID
from typing import List

import uuid


@dataclass
class Category(BaseModel):

    name: str
    region: str
    type_: str
    files: List[str]
    uuid: UUID

    def __init__(self, name: str, region: str, type_: str) -> None:
        super().__init__(name=name, region=region, type_=type_, files=[], uuid=uuid.uuid4())

    @validator('*', pre=True)
    def name_len(cls, value):
        if isinstance(value, str):
            if len(value) <= 0:
                raise ValueError('category_name len should be bigger than 1')
        return value

    def is_duplicate(self, file):
        if file:
            self.files.append(file)
