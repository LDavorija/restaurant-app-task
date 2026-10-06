from fastapi import FastAPI, Body   # for using FastAPI framework, Body is for parsing request body text as an argument
from fastapi.middleware.cors import CORSMiddleware
from google import genai    # for using Gemini API
from google.genai import types  # for guarantee that Gemini will return .json file
import os   # for using environment variables

app = FastAPI()

# purpose of this is to allow frontend and backend to be connected
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dozvoljava pristup s bilo kojeg izvora (idealno za razvoj/testiranje)
    allow_credentials=True,
    allow_methods=["*"],  # Dozvoljava sve metode (uključujući GET, POST, OPTIONS)
    allow_headers=["*"],  # Dozvoljava sva zaglavlja
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
uploaded_file = client.files.upload(file = "jelovnik.json")


# Home route
@app.get("/")
def index():
    return {"Message": "Dobrodošao u inteligentni sustav za preuzimanje narudžbi u restoranu"}

# Route for taking an order
@app.post("/order")
def take_order(order_text: str = Body(..., embed=True)):

    # building a prompt for Gemini
    prompt = f"""
        Ti si inteligentni sustav za preuzimanje narudžbi u restoranu koji analizira tekst gosta[cite: 2].

        PRAVILA OBRADE:
        1. Prepoznaj stavke i količine te ih mapiraj na odgovarajući ID s jelovnika (npr. margarita, coca_cola, capricciosa, pivo)[cite: 2].
        2. Ono čega nema na jelovniku vraća se zasebno u polje "unavailable". Ne smije se izgubiti ni zamijeniti nečim sličnim[cite: 2].
        3. Uzmi u obzir ispravke u hodu ako gost promijeni mišljenje tijekom rečenice (npr. "ma ne, ipak..."). Pazi je li u nekom dijelu poruke izuzeo određenu stavku ili je samo dodao nove ili promijenio postojeće.[cite: 1].
        4. Ako gost postavlja samo općenito pitanje (npr. o jelima bez mesa), vrati praznu listu stavki i daj prijedloge u poruci[cite: 1].

        FORMAT ODGOVORA:
        Vrati isključivo važeći JSON objekt u sljedećem formatu, bez dodatnog teksta ili markdown oznaka (osim ako je obavezno, ali uz response_mime_type najbolje je čist JSON):
        {{
        "items": [
            {{"id": "id_stavke", "quantity": broj}}
        ],
        "unavailable": [
            {{"text": "naziv stavke", "quantity": broj}}
        ],
        "message": "Ovdje stavi prijedlog ili odgovor ako gost postavlja pitanje"
        }}

        Tekst narudžbe gosta: {order_text}
        """

    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite", 
        contents = prompt,
        # guarantee that Gemini will return correct JSON
        config=types.GenerateContentConfig(response_mime_type="application/json")
    )

    return response