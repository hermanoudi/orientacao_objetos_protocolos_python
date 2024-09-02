from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List

# Enumeração / Enumerador
class InstrumentKind(Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"

@dataclass
class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...

@dataclass
class DataInstrumentMixin:
    name: str
    sound: str
    kind: InstrumentKind
    colors: List[str] = field(default_factory=list)

@dataclass
class Instrument(ABCInstrument, DataInstrumentMixin):
    ...

@dataclass
class Guitar(Instrument):
    
    sound: str = "Ding Ding Ding"
    kind: InstrumentKind = InstrumentKind.string
    colors: List[str] = field(default_factory=lambda: ["white", "black"])

    def play(self):
        return self.sound

@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind

    def play(self):
        return self.sound
