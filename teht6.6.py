def laskuri(h1, h1hal, h2, h2hal):
    import math
    h1arvo = h1hal/2 ** 2 * math.pi / 10000 / h1 # neliömetri on 10,000 kertaa neliösentti
    h2arvo = h2hal/2 ** 2 * math.pi / 10000 / h2 # neliömetri on 10,000 kertaa neliösentti
    if h1arvo > h2arvo:
        print(f"Pizza #1 on parempi vaihtoehto, siitä saa {h1arvo} neliömetriä per euro")
        print(f"Pizza #2 on huonompi vaihtoehto, siitä sai vain {h2arvo} neliömetriä per euro")
    else:
        print(f"Pizza #2 on parempi vaihtoehto, siitä saa {h2arvo} neliömetriä per euro")
        print(f"Pizza #1 on huonompi vaihtoehto, siitä sai vain {h1arvo} neliömetriä per euro")
    return

pizza1hinta = float(input("Kuinka paljon 1. pizza maksaa? "))
pizza1hal = float(input("Kuinka paljon on 1. pizzan halkaisija (cm)? "))
pizza2hinta = float(input("Kuinka paljon 2. pizza maksaa? "))
pizza2hal = float(input("Kuinka paljon on 2. pizzan halkaisija (cm)? "))
laskuri(pizza1hinta, pizza1hal, pizza2hinta, pizza2hal)