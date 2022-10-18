from dataclasses import dataclass
from datetime import datetime


@dataclass
class SrcObject1:
    name: str


@dataclass
class SrcObject2:
    start: datetime
    end: datetime


@dataclass
class DstObject:

    id: str
    name: str
    start: datetime
    end: datetime


# old code


def old_code(src_obj1: SrcObject1, src_obj2: SrcObject2):
    dst_obj = DstObject(
        id='1221',
        name=src_obj1.name,
        start=src_obj2.start,
        end=src_obj2.end,
        # ...
    )

# new code

class DstObjectBuilder:

    _instance: DstObject

    def __init__(self):
        self._instance = DstObject()
        self._instance.id = '12321'

    def from_obj1(self, obj: SrcObject1) -> 'DstObjectBuilder': 
        self._instance.name = obj.name
        return self

    def with_obj2(self, obj: SrcObject2) -> 'DstObjectBuilder': 
        self._instance.start = obj.start
        self._instance.end = obj.end
        return self

    def build(self) -> DstObject:
        return self._instance


def new_code(src_obj1: SrcObject1, src_obj2: SrcObject2):
    dst_obj = DstObjectBuilder().from_obj1(src_obj1).with_obj2(src_obj2).build()