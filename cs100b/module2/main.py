from plant import Plant
from fungus import Fungus
from animal import Animal

eukaryotes = [Plant("peat_moss"), Fungus("honey_fungus"), Animal("blue_whale")]
for e in eukaryotes:
    e.directional_movement()

    if type(e) is Plant:
        e.thigmotropism("magic_wand")
    elif type(e) is Fungus:
        e.mycelium("common_juniper")
    elif type(e) is Animal:
        e.active_feeding("krill")