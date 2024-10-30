# Orchestrator AI
![Screenshot 2024-10-30 alle 17 35 13](https://github.com/user-attachments/assets/286e2111-e382-439e-ace1-bb3d06cf4d44)
## Progetto
Semplice gestore di agenti ai/assistenti scritto in python per uso personale. Permette di usare i modelli Meta Llama 3.1 405B, Meta Llama 3.2 90B, Mistral Large e Codestral tramite le api gratuite di sambanova.ai e mistral.ai specializzati in determinati compiti tramite appositi prompt.
## Agenti
Al momento ho inserito tre tipologie di agenti: chabot generici, assistenti per la programmazione in rust e in python, e agenti per fare il riassunto di testi (non ancora testati)
- Per i chatbot generici e i "summerizers" è possibile scegliere tra i modelli più grandi Meta Llama 3.1 405B, Meta Llama 3.2 90B e Mistral Large
- Per gli assistenti per la programmazione è impostato solo il modello "codestral" dal momento che è meno pesante e ottimizzato per questa task
## To-do
- [ ] Aggiunta di altri agenti per altre task
- [ ] Implementare funzioni personalizzate (tools) che gli agenti possono utilizzare per restituire un'output più accurato o svolgere azioni più complesse
- [ ] Creazione di uno script per automatizzare l'installazione
## Installazione
Al momento l'unico modo per usare orchestrator ai è clonare la repo e installare le dipendenze manualmente, consiglio di farlo in un ambiente virtuale python apposito per il progetto.
## IMPORTANTE
Questo programma è solo un gestore di ai agents, non un modello ai vero e proprio, pertanto utilizza modelli preaddestrati tramite le api di sambanova.ai e mistral.ai. Per poterlo utilizza quindi è necessario procurarsele, almeno una delle due, creando un account al loro sito web, sottolineo che è gratuito.
