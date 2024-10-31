import openai, time, os
from dotenv import load_dotenv
from prompts import uncensored_assistant, python_coder, rust_coder, summerizer

#caricara le variabili d'ambiente
load_dotenv()

url_mistral = 'https://api.mistral.ai/v1'
url_sambanova = 'https://api.sambanova.ai/v1'


#creazione degli agenti
class agente:
    def __init__(self, modello, prompt, url, nome, temperature):
        self.modello = modello
        self.prompt = prompt
        self.url = url
        self.nome = nome
        self.temperature = temperature
    
    def ottieni_dati(self):
        modello = self.modello
        prompt = self.prompt
        url = self.url
        nome = self.nome
        temperature = self.temperature
        return modello, prompt, url, nome, temperature

uncensored_assistant_1 = agente(modello='Meta-Llama-3.1-405B-Instruct', prompt=uncensored_assistant.system_prompt, url=url_sambanova, nome="Tank", temperature=0.8)
uncensored_assistant_2 = agente(modello='Llama-3.2-90B-Vision-Instruct', prompt=uncensored_assistant.system_prompt, url=url_sambanova, nome="Tank", temperature=0.8)
uncensored_assistant_3 = agente(modello='mistral-large-latest', prompt=uncensored_assistant.system_prompt, url=url_mistral, nome="Tank", temperature=0.8)
rust_coder = agente(modello='codestral-latest', prompt=rust_coder.system_prompt, url=url_mistral, nome="Rusty", temperature=0.1)
python_coder = agente(modello='codestral-latest', prompt=python_coder.system_prompt, url=url_mistral, nome="Pitone", temperature=0.1)
summerizer_1 = agente(modello='Meta-Llama-3.1-405B-Instruct', prompt=summerizer.system_prompt, url=url_mistral, nome="Sam", temperature=0.4)
summerizer_2 = agente(modello='Llama-3.2-90B-Vision-Instruct', prompt=summerizer.system_prompt, url=url_mistral, nome="Sam", temperature=0.4)
summerizer_3 = agente(modello='mistral-large-latest', prompt=summerizer.system_prompt, url=url_mistral, nome="Sam", temperature=0.4)


#funzioni principali
def seleziona_agente():
    while True:
        print("\033[95mSeleziona l'agente che desideri utilizzare:\n\033[0m\n\033[94m-----------------Chat Generica-----------------\033[0m\n1. Tank - Llama 3.1 405B uncensored (sambanova)\n2. Tank - Llama 3.2 90B uncensored (sambanova)\n3. Tank - Mistral large uncensored (mistral)\n\033[94m\n-----------------Programmazione----------------\033[0m\n4. Rusty - Codestral (mistral)\n5. Pitone - Codestral (mistral)\n\033[94m\n-------------------Riassunti-------------------\033[0m\n6. Sam - Llama 3.1 405B (sambanova)\n7. Sam - Llama 3.2 90B (sambanova)\n8. Sam - Mistral large (mistral) \n")
        print("\033[91mAssicurati di avere la chiave api di sambanova e/o di mistral nelle proprie variabile d'ambiente come SAMBANOVA_API_KEY e MISTRAL_API_KEY, rispettivamente.\033[0m")
        print("\033[94m\nDigita 'exit' per uscire.\033[0m")
        scelta = input("\nInput:")
        #confronta la scelta con gli agenti, e quando trova quello corrispondente ne estrae i dati
        match scelta:
            case "1":
                return uncensored_assistant_1.ottieni_dati()
            case "2":
                return uncensored_assistant_2.ottieni_dati()
            case "3":
                return uncensored_assistant_3.ottieni_dati()
            case "4":
                return rust_coder.ottieni_dati()
            case "5":
                return python_coder.ottieni_dati()
            case "6":
                return summerizer_1.ottieni_dati()
            case "7":
                return summerizer_2.ottieni_dati()
            case "8":
                return summerizer_3.ottieni_dati()
            case "exit":
                print("\033[95m\nArrivederci!\n\033[0m")
                exit(0)
            case _:
                print("\033[91mOpzione non valida, riprova.\033[0m")
                pulisci_schermo()

def converazione(client, modello, prompt, nome, temperature):
    pulisci_schermo()
    print(f"\033[95mSono {nome}, il tuo assistente personale, dimmi cosa posso fare per te.\033[0m \n") 

    time.sleep(1)
    while True:
        #chat
        domanda = input("\033[92m>\033[0m ")

        if domanda == "/exit":
            break

        #invia l'input al client e restituisce la risposta
        risposta = client.chat.completions.create(
            model = modello,
            messages=[{"role":"system","content":prompt},{"role":"user","content":domanda}],
            temperature =  temperature,
            top_p = 0.1
        )

        print("\n\033[94m" + risposta.choices[0].message.content + "\033[0m\n")

        #aggiunge la domanda e la risposta al contesto del prompt per la memoria dell'agente
        prompt += domanda + risposta.choices[0].message.content
        time.sleep(0.5)

def pulisci_schermo():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)


def main():
    while True:
        pulisci_schermo()
        modello, prompt, url, nome, temperature = seleziona_agente()
        if url == url_mistral:
            api_key = os.getenv("MISTRAL_API_KEY")
        elif url == url_sambanova:
            api_key = os.getenv("SAMBANOVA_API_KEY")
        
        #crea un client e si connette all'api di sambanova o mistral
        client = openai.OpenAI(
            api_key=api_key,
            base_url=url,
        )

        converazione(client, modello, prompt, nome, temperature)



if __name__ == "__main__":
    main()