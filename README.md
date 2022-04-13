# Labyrintti

## Checkpoint1

## Tämänhetkiset ominaisuudet

Graafinen ikkuna, johon ilmestyy halutun kokoinen pelattava labyrintti.
Labyrintin keskelle sijoitetaan pelaaja(musta kolmio) ja jonnekin reunalle exit(vihreä neliö.)
Pelaajaa voi liikutella WASD näppäimillä. Ja kun pelaaja saavuttaa exitin peli loppuu(sys.exit).
Tällä hetkellä työstämässä juuri 3D versiota. 
Täten labyrinttejä ilmestyy nyt 2 ja niihin samoissa paikoissa olevia punaisia neliöitä jotka kuvaavat portaita.
Portaat eivät kuitenkaan vielä toimi ja täten ainoastaan aloitustaso on pelattavissa, joskin usein exit on saavuttamattomissa koska toinen taso on pelaajan tavoittamattomissa.
Mutta taustalla on kuitenkin toimiva labyrintti.

 ## Käyttöohje

 - Voiko ohjelmaa jo ajaa? (kyllä/ei)
 Kyllä.

 - Kuinka ohjelma käynnistetään?
 Ajamalla main funktio.
labyrintin kokoa voi muuttaa vaihtamalla main funktion ensimäisellä rivillä lähetettävän numeron suuruutta. Numeron neliöjuuren täytyy kuitenkin olla kokonaisluku.

 ## Aikataulu

 - Kuinka paljon olet jo käyttänyt aikaa projektiin?
 Koodiin noin 20h ja suunnitelmaan noin 6h

 - Onko ilmennyt muutoksia suunnitelman aikatauluun?
 Ei vielä

 ## Muuta

 - Onko ilmaantunut erityisiä ongelmia?
 Tällä hetkellä tosiaan portaat eivät toimi ja kruskalin algoritmissä lista saattaa mennä välillä yli indeksin jolloin ohjelma kaatuu erroriin.
 Johtuu create_graph metodista ja siihen lisäämästä satunnaisuudesta siitä kuinka usein linkkejä kerroksien välille luodaan(muuten mielestäni portaita tuli liika).

 - Oletko joutunut tekemään muutoksia suunnitelmaasi?
 Kyllä.
 yksi kirjasto lisää(math), koska tarvitsimme sqrt funktiota.
 Vaihdoin labyrinttini weave-mallista 3D-malliin. Saattaa olla että tämä vielä muuttuu.
primin algoritmin sijasta käytämme kruskalin algoritmia. Tekemäni primin algoritmin implementaatio matriiseille aivan liian hidas.
Täten myös käytössä oleva matriisi muuttui hiukan verrattuna suunnitelman versioon. Nyt rivin kaksi ensimmäistä numeroa kuvaavat linkitettyjä ruutuja ja kolmas linkin painoarvoa.
Molemmat implementaatiot löytyvät labyrinth luokasta(prim kommentoituna)

## Checkpoint2

## Tämänhetkiset ominaisuudet

Graafisessa ikkunassa pelattava weave labyrintti. Labyrintin kokoa ja tunneleiden määrää voi vaihdella muuttamalla kahta arvoa koodissa. Pelaaja, exit ja liikkuminen toimivat edelleen samalla tavalla kuin aikaisemmin. 

Pelissä on kuitenkin sisäänrakennettuna ansa, monet tunneleiden suuaukoista eivät toimi. Kun kaikki näistä ovat identtisen näköisiä, labyrinteistä tulee yllättävän turhauttavia ja vaikeita ratkaista. Tietenkin kun mahdollisten tunnelien määrää voi säädellä se myös säätelee hiukan vaikeustasoa.

 ## Käyttöohje

 - Voiko ohjelmaa jo ajaa? (kyllä/ei)

 Kyllä.

 - Kuinka ohjelma käynnistetään?

Ajamalla main funktio.

Labyrintin kokoa voi muuttaa vaihtamalla main funktion rivillä 10 lähetettävän numeron suuruutta. Numeron neliöjuuren täytyy kuitenkin olla kokonaisluku.

Tunneleiden määrä voi vaihdella vaihtamalla Labyrinth.py:n rivillä 33 olevan for-loopin iteroinnin määrää. Labyrinteissä on kuitenkin aina raja, kuinka monta tunnelia mahtuu, joten tietyn pisteen jälkeen iteroinnin määrää lisäämällä tunneleita ei tule enään lisää.

 ## Aikataulu

 - Kuinka paljon olet jo käyttänyt aikaa projektiin?

 Koodiin noin 30h ja suunnitelmaan noin 6h

 - Onko ilmennyt muutoksia suunnitelman aikatauluun?
 
 Yhden viikon skippasin muiden kurssien kiireiden takia ja tenttiviikolla olen tehnyt normaalia vähemmän koodia. Loppua kohti voin kuitenkin kiristää tahtia.

 ## Muuta

 - Onko ilmaantunut erityisiä ongelmia?

 Tällä hetkellä kaikki labyrintissä toimii niin kuin pitääkin.

 Weaven toimivuuden kanssa oli aika paljon taisteltavaa. Samalla tuli vahingossa keksittyä labyrintin ansa ominaisuus, kun grafiikka piirsi kaikki tunnelit vaikka algoritmi ei niitä kaikkia toteuttanutkaan.

 - Oletko joutunut tekemään muutoksia suunnitelmaasi?

 Kyllä.

Palasin takaisin weave labyrinttiin, kun tajusin että 3D:tä varten olisi joutunut uudelleenkirjoittamaan paljon koodia joka jo toimi moitteettomasti 2D labyrintissä. Mielestäni valinta oli oikea sillä labyrintti on juuri sellainen kuin halusin.

Seuraavaksi lähden tekemään ratkaisualgoritmiä ja valikkoa. Sekä viimeistelemään työtä.

