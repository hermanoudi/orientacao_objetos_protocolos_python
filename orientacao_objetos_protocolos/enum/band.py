from enum_example import Instrument, Guitar, Flute, InstrumentKind


gianini = Guitar("Gianini m2", kind=InstrumentKind.keys, colors=["green"])
print(gianini.play())
print(gianini.colors)

yamaha = Flute("Yamaha Magic Flute")
print(yamaha.play())
