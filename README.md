# Lentopeli 
## Ohjelmisto 2, Projekti

Peliä varten tarvitsen lentopeli-tietokannan Relaatiotietokanta-kurssilta. 
Jotta peli toimii on luotava kaksi uutta taulua (cards ja gameboard).
Cards taulu sisältää pelin yllätyskortit. Tarvittavat tietokanta-muutokset löydät 
seuraavasta tiedostosta: LentopeliTietokantaMuutokset.txt. 

Syötä käyttäjätunnus ja salasana sekä tietokannan nimi tietokanta-ajurin connect-metodiin, joka löytyy:
Backend/database.py

Ennen kun aloitat pelin käynnistä Backend taustapalvelin Backend/routes.py
Pelin etusivulla (home.html) on kentät, joihin ensiksi syötetään pelaajien nimet. Kun pelikenttä on
muodostunut kartalle voit avata nopan OPEN-täpästä. Noppaa heitetään klikkaamalla ROLL. Pelaajat 
heittävät noppaa vuorollansa.

Virhetilanteissa tarkasta konsoli, sieltä löytyy tarkentavat virheilmoitukset, joiden avulla saat
ratkottua tilanteen (ehkä).

