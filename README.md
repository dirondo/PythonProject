#  Valūtas un kriptovalūtas konvertētājs

##  Projekta uzdevums

Šī Python programma ir izstrādāta kā interaktīvs valūtas un kriptovalūtas konvertētājs, kuru var darbināt caur konsoli. Mūsu izstrādāta programma var:

- konvertēt valūtas pēc aktuālajiem kursiem;
- aprēķināt, cik daudz sākotnējās valūtas nepieciešams, lai iegūtu noteiktu summu citā valūtā;
- aprēķināt, cik daudz kriptovalūtas (Bitcoin, Ethereum, BinanceCoin) var iegādāties par izvēlēto valūtu;
- saglabāt aktuālos valūtas kursus teksta failā. (Exchange.txt)

Programma izmanto ārējos API pakalpojumus, lai iegūtu jaunākos datus par valūtu un kriptovalūtu kursiem.

---

##  Izmantotās Python bibliotēkas

Programmas izstrādes laikā izmantotas šādas bibliotēkas:

- **requests** — izmanto, lai nosūtītu HTTP pieprasījumus uz valūtu kursu API (Exchange Rate API, CoinGecko). Tā ir nepieciešama, lai iegūtu aktuālos kursus no ārējiem avotiem.
- **datetime** — tiek izmantota datuma un laika attēlošanai un failā pierakstīšanai, kad tika iegūti kursi.
- **colorama** — atbild par krāsainu teksta attēlošanu konsolē, padarot programmu vizuāli saprotamāku un lietotājam draudzīgāku.

---

##  Datu struktūras

- **json** – iebūvēts Python modulis, kas tiek izmantots, lai apstrādātu datus, kurus API atgriež JSON formātā. Tas ļauj pārveidot JSON atbildes par Python vārdnīcām, ar kurām tālāk var strādāt programmā.
- **Vārdnīca** (dict) – galvenā struktūra valūtu kursu glabāšanai. Atslēgas ir valūtas kodi ("USD" un "EUR"), bet vērtības – valūtas kurss.

---
## Izmantotas metodes


- (get_rates) - Šī funkcija iegūst valūtas kursus no exchangerate-api.com un atgriež vārdnīcu ar citu valūtu kursiem attiecībā pret bāzes valūtu
- (convert) - Šī funkcija veic valūtas konvertēšanu no vienas valūtas uz citu un izvade rezultātu.
- (reverse_convert) - Aprēķina, cik daudz sākotnējās valūtas nepieciešams, lai iegūtu noteiktu mērķa summu.
- (save_file) - Saglabā valūtas kursus tekstu failā .txt formātā
- (get_crypto) - Iegūst un parāda kriptovalūtu cenas salīdzinājumā ar norādīto valūtu, izmantojot coingecko.com

---

## Koda izvade

```
Select an option:
1. Currency conversion
2. Reverse currency conversion
3. Conversion to crypto
4. Exit
Enter option number: 1
From currency: usd
In currency: eur
Enter the amount: 5463
5463.0 USD = 4916.15 EUR
Data saved: Exchange_USD.txt
```