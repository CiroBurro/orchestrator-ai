# Orchestrator AI
## Progetto
Semplice gestore di agenti ai/assistenti scritto in python per uso personale. Permette di usare numerosi modelli tramite le api gratuite di sambanova.ai, mistral.ai, openrouter.ai e github.com specializzati in determinati compiti tramite appositi prompt.
## Agenti
Le tipologie di agenti disponibili sono:
- Chat generica
- Programmazione (rust e python)
- Riassunti (da testare)
- Matematica
- Trascrizione di appunti (risultati buoni ma non perfetti)

![Screenshot 2024-11-01 alle 12 14 54](https://github.com/user-attachments/assets/3694ec69-ac1f-4183-85a7-034f9f652f2f)
## To-do
- [X] Aggiunta di altri agenti per altre task
- [ ] Implementare funzioni personalizzate (tools) che gli agenti possono utilizzare per restituire un'output più accurato o svolgere azioni più complesse
- [ ] Creazione di uno script per automatizzare l'installazione
## Installazione
Per ora l'unico modo per usare orchestrator ai è clonare la repo e installare le dipendenze manualmente, consiglio di farlo in un ambiente virtuale python apposito per il progetto.
## IMPORTANTE
Questo programma è solo un gestore di ai agents, non un modello ai vero e proprio, pertanto utilizza modelli preaddestrati tramite le api di sambanova.ai, mistral.ai, openrouter.ai e github.com. Per poterlo utilizza quindi è necessario procurarsele, almeno una delle tre, creando un account al loro sito web, e sottolineo che è gratuito. Successivamente devono essere aggiunte come variabili d'ambiente sul proprio computer col nome "SAMBANOVA_API_KEY", "MISTRAL_API_KEY", "OPENROUTER_API_KEY" e "GITHUB_API_KEY".
## Comandi e tool
Gli unici due comandi utilizzabili sono:
- /exit : per uscire sia dalla conversazione sia dal programma quando si è nella fase di selezione dell'agente
- /file : per usare i tool implementati

I tool invece sono:
- Possibilità di leggere informazioni da un file di testo, vale per tutti gli agenti eccetto quelli appartenenti alla categoria "appunti"
- Possibilità di visualizzare immagini e trascrivere il testo contenuto al loro interno, vale solo per gli agenti della categoria "appunti"

Utilizzo dei tool:
Sia quando si carica un file sia quando si carica un'immagine bisogna usare il comando /file seguito dal percorso del file/immagine. Successivamente è possibile inserire ulteriori comandi.

Esempi:
">/file /path/to/file/txt"
">/file /path/to/img trascrivi il testo contenuto in questa immagine"


Attenzione!
L'unica dicitura corretta è quella degli esempi: è necessario scrivere /file subito dopo il simbolo ">" senza spazi prima e affianco il percorso del file lasciando uno spazio, eventuali istruzioni vanno inseriti alla fine
