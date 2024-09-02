from instrument import EletricGuitar, Instrument, Guitar, Flute, Distortion


gianini = Guitar("Gianini m2")
print(gianini.play())


yamaha = Flute("Yamaha Magic Flute")
print(yamaha.play())

lespaul = EletricGuitar("lespaul m1")
print(lespaul.play(distortion=Distortion.wave))
