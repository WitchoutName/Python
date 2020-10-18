from math import *
'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807
MOON_GRAVITY = 1.62
SUN_GRAVITY = 274
MARS_GRAVITY = 3.711
MERKUR_GRAVITY = 3.7
URAN_GRAVITY = 8.87
VENUS_GRAVITY = 8.87
SATURN_GRAVITY = 10.44
NEPTUN_GRAVITY = 11.15
JUPITER_GRAVITY = 24.79

SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def time_from_lihgtning(time):
    '''
    někde uhodil blesk: zadejte dobu v sekundách, za jakou bylo slyšet hřmění a dostanete čas,
    za který jste byli schopní blesk vidět v mikrosekundách (za předpokladu, že žijeme ve vákuu (ve kterém by blesky nebyli možné :D))
    '''
    return (SPEED_OF_SOUND * time) / SPEED_OF_LIGHT * 1e6


def golf(force, angle, area="earth"):
    '''
    zadejte sílu, úhel a lokaci ve sluneční soustavě a dostanete vzdálenost, jak daleko by doletěl golfový míček
    '''
    if area == "earth":
        g = EARTH_GRAVITY
    if area == "moon":
        g = MOON_GRAVITY
    if area == "mars":
        g = MARS_GRAVITY
    if area == "merkur":
        g = MERKUR_GRAVITY
    if area == "uran":
        g = URAN_GRAVITY
    if area == "venus":
        g = VENUS_GRAVITY
    if area == "saturn":
        g = SATURN_GRAVITY
    if area == "neptun":
        g = NEPTUN_GRAVITY
    if area == "jupiter":
        g = JUPITER_GRAVITY
    if area == "sun":
        g = SUN_GRAVITY

    mass = 0.04593
    velocity = force / mass
    sinofan = sin((angle*2)*pi/180)
    x = (pow(velocity, 2)/g)*sinofan
    return x

