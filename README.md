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
