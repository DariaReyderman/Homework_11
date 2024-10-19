name: str = "Daria Reyderman. Holon"
print('a', "length:", len(name))
print('b', "upper:", name.upper())
print('c', "lower:", name.lower())
print('d', "startswith:", name.startswith("Daria"))
print('e', "endswith:", name.endswith("Holon"))
print('f', "split:", name.split())
print('g', "replace:", name.replace(" ", "*"), name.split())
print('h', "center:", name.center(50, "="))
print('i:', "Daria Reyderman. Holon"[4:])
print('j', "Daria Reyderman. Holon"[:5])
print('k', "Daria Reyderman. Holon"[2::2])
name: str = "daria reyderman. holon"
print('l', name.title())
