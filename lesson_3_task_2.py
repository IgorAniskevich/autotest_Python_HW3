from smartphone import Smartphone
catalog = []
catalog.append (Smartphone("nokia", "3310", "+7989898989"))
catalog.append (Smartphone("iphone", "14", "+756589658333"))
catalog.append (Smartphone("motorola", "v3", "+7999999999"))
catalog.append (Smartphone("asus", "999", "+72121121212"))
catalog.append (Smartphone("sony", "x1", "+7369852147"))

for i in catalog:
    print(i.brand, i.model, i.number)

 