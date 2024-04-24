import time
import sys
from colorama import Fore, Style
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


def intro():
    print_slow(Fore.LIGHTYELLOW_EX +"""
    Sinä ja toinen pelaaja olette arvostettuja jäseniä luksus golfklubilla. 
    Olette päättäneet järjestää pikku kisan. Lyötte julkisesti vetoa muiden jäsenten edessä siitä, 
    kumpi teistä ehtisi ensin matkata koko maapallon halki.
    
    Kisa etenee seuraavasti; Lähtö on Svalbardin lentokentältä ja maali on Etelänapa. 
    Vierailette jokaisessa maanosassa, joista keräätte leimat passiin. Golfklubin muut 
    jäsenet ovat pistäneet kokoon listan lentokentistä (pelilauta), joiden kautta edetään. 
    Voittaja on perillä ensin.
    
    Matkailunne aiheuttaa suuria määriä päästöjä, jotka vaikuttavat maapallon säätilaan. 
    Jokaisella kentällä vedetään Co2- kortti, joista kerätään “Ökyrikas”- pisteitä. Joillekin kentille 
    on myös piilotettu “Yllätys”- kortteja. Ne voivat olla hyödyksi tai haitaksi.
    
    Lopussa jaetaan tittelit. Ensimmäinen maalissa on voittaja, eli “Rutikuiva”. 
    Pelissä lasketaan myös “Ökyrikas”- pisteet yhteen ja niitä eniten kerännyt saa tittelin “Upporikas”, 
    mikäli hän ei ollut maalissa ensimmäisenä. Jos pelaaja on sekä ensimmäisenä maalissa että haalinut eniten 
    “Ökyrikas”- pisteitä, kruunataan hänet pelin ylivoimaiseksi mestariksi. Hän ansaitsee tittelin “Ökyrikas ja 
    Rutikuiva”.
    
    """ + Style.RESET_ALL)
