from dataclasses import dataclass, field
from typing import Optional, Union
from enum import Enum


class StoreType(Enum):
    NUMBER = 1
    STRING = 2  # always bytes

    # TODO: UPPER NEEDS TO BE REMOVED, ONLY TO TEMPORARILY SUPPORT ERROR FIXING
    def upper(self):
        return self.name

@dataclass
class ConfigStore:
    label: str
    init_value: Union[bytes, float]
    type: StoreType
    index: int = field(init=False)
    identifier: Optional[str] = ''
    description: str = ''
    _next_id: int = field(default=1, init=False, repr=False)
    
    def __post_init__(self):
        self.index = ConfigStore._next_id
        ConfigStore._next_id += 1
        self.type = StoreType[self.type.upper()]