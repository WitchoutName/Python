from string import ascii_lowercase as az
import physics
areas = {
    "a": ("earth", "Země"),
    "b": ("moon", "Měsíc"),
    "c": ("mars", "Mars"),
    "d": ("merkur", "Merkur"),
    "e": ("uran", "Uran"),
    "f": ("venus", "Venuše"),
    "g": ("saturn", "Saturn"),
    "h": ("neptun", "Neptun"),
    "i": ("jupiter", "Jupiter"),
    "j": ("sun", "Slunce")
}

def print_golf():
    print("SIMULÁTOR GOLFU")
    print("Kde odpalujete míček?")
    count = 0
    for x, area in enumerate(areas):
        print(f"  {area}) {areas[area][1]}")
        count = x
    area = input()
    if area in az[:count + 1]:
        angle = input("V jakém úhlu odpalujete míček? ")
        force = input("Jakou silou odpalujete míček? (v Newtonech) ")
        print("Pobrá práce! Míček dopadl {}m daleko.".format(physics.golf(float(force), float(angle), area=areas[area][0])))

def print_light():
    print("SIMULÁTOR BLESKŮ")
    inp = input("Někde uhodil blesk: zadejte dobu v sekundách, za jakou bylo slyšet hřmění.\n")
    print(f"Blesk jste viděli {physics.time_from_lihgtning(float(inp))} mikrosekund op jeho vzniknutí.")

def menu():
    print("Funkce:")
    print("  a) Golf")
    print("  b) Blesky")
    inp =input()
    if inp == "a":
        print_golf()
    if inp == "b":
        print_light()

menu()