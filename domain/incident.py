from dataclasses import dataclass
@dataclass
class Incident:
    id: int
    title: str
    description: str
    level: str
    status: str = "abierta"
