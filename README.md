# **Kako se servis pokreće?**

1. U terminalu je potrebno instalirati korištene librarye koristeći sljedeću komandu:
   pip install fastapi uvicorn google-genai
2. Postaviti Gemini API u Windows system variables koristeći grafičko sučelje OS Windowsa
3. Pozicionirati se u direktorij u kojemu se nalaze datoteke, te pokrenuti backend sljedećom naredbom:
   uvicorn main:app --reload
4. Za provjeru kako program radi imate dvije opcije:
   4.1 Koristiti službenu dokumentaciju koju automatski generira FastAPI odlaskom na rutu koja je dana nakon naredbe > uvicorn main:app --reload uz dodatak "/docs"
   4.2. Korisititi frontend koji je kreiran u datoteci frontend.html tako što dvaput kliknete na njega
5. Odgovor Geminija se nalazi pod ključem "candidates" pa "parts" pa "text" unutar liste.

# **Što bi se dalo poboljšati?**

Ono što bi se dalo poboljšati, svakako ljepši frontend, prompt bi svakako trebao biti puno detaljniji, u smislu da treba sadržavati i informacije o tome što činiti kada se dogodi nekakav nepredviđeni scenarij.

# **Kako bi se sustav mogao provjeravati?**

Sustav bi se mogao provjeravati koristeći pytest library za one narudžbe za koje znamo egzaktni .json fajl koji program treba vratiti. Što se tiče drugih slučajeva u kojima program treba predložiti nešto recimo bez mesa, tu ne možemo egzaktno znati koji će oblik rješenja biti, tako da bi to bilo dobro provjeriti ručno.
Također, nakon istraživanja došao sam do saznanja da je unutar FastAPI TestClient postoji ugrađen pytest pa je i to jedna od solucija
