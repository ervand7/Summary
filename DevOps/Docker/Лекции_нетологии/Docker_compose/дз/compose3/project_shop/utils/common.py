from enum import Enum


class Status(Enum):
    new = 'NEW'
    in_progress = 'IN_PROGRESS'
    done = 'DONE'

    def __init__(self, status):
        self.status = status
