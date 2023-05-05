from src.lib.domains.Category import Category

from dataclasses import dataclass
from typing import List
from uuid import UUID
from pydantic import BaseModel
import uuid


@dataclass
class APIMock(BaseModel):
    name: str
    region: str
    type_: str
    files: List[str]
    uuid: UUID

    def __init__(self, name: str, region: str, type_: str) -> None:
        super().__init__(name=name, region=region, type_=type_, files=[], uuid=uuid.uuid4())

