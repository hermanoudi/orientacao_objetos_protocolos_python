# Abstração e Herança com dataclasse?
# Tem enum no Python?
# dataclasses com valor default dão erro.
# para que server o super()?

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"


@dataclass
class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...

@dataclass
class DataInstrumentMixin:
    name: str
    sound: str
    kind: str

@dataclass
class Instrument(ABCInstrument, DataInstrumentMixin):
    ...

@dataclass
class Guitar(Instrument):
    n_string: int = 6
    sound: str = "Ding Ding Ding"
    kind: str = "string"

    def play(self):
        return self.sound

@dataclass
class EletricGuitar(Guitar):
    sound: str = "Wah Wah Wah"

    def play(self, distortion=Distortion.wave):
        return_from_base_class = super().play()   # mro
        if distortion is Distortion.wave:
            return "~~~~".join(return_from_base_class.split())
        elif distortion is Distortion.whisper:
            return "...".join(return_from_base_class.split())            
        return return_from_base_class
@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: str = "Wind"

    def play(self):
        return self.sound
