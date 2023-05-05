from src.lib.domains.Category import Category
from dataclasses import dataclass

import uuid


@dataclass
class Core:
    def __init__(self):
        self.uuid: uuid = uuid.uuid4()
        self.categories: {Category} = {}
