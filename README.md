# Orchestrator AI
## Progetto
Semplice gestore di agenti ai/assistenti scritto in python per uso personale. Permette di usare numerosi modelli tramite le api gratuite di sambanova.ai, mistral.ai, openrouter.ai e github.com specializzati in determinati compiti tramite appositi prompt.
## Agenti
Le tipologie di agenti disponibili sono:
- Chat generica
- Programmazione (rust e python)
- Riassunti
- Matematica
- Trascrizione di appunti (risultati buoni ma non perfetti)
![Screenshot 2024-11-06 alle 21 02 55](https://github.com/user-attachments/assets/e342115d-24ab-461a-8a2f-e35f946cf782)
## To-do
Al momento non ho in mente altre idee per il progetto, per ora funziona bene senza bug e lo trovo completo per le mie esigenze, se avete richieste particolari sono pronto a prenderle in considerazione. Al massimo aggiungerò nuovi modelli con eventuali altre API gratuite se ne scopro di nuovi.
## Installazione
### Installare il pacchetto
Il programma è caricato sul repository PYPI: https://pypi.org/project/orchestrator.ai/, basterà quindi avere installato python ed eseguire il comando:
```bash
pip install orchestrator.ai
```
Per eseguirlo sarà sufficiente invece lanciare dal terminale il comando:
```bash
orchestrator-ai
```
### Installazione manuale
Se si preferisce installare il programma manualmente bisogna clonare questo repository:
```bash
git clone https://github.com/CiroBurro/orchestrator-ai.git
```
Entrare nella cartella del progetto e installare le dipendenze:
```bash
cd orchestrator-ai
pip install -r requirements.txt![Screenshot 2024-11-06 alle 20 59 42](https://github.com/user-attachments/assets/981e1ffa-fd1e-4005-9a18-56fe7525c85c)

```
Infine lanciare il programma con python:
```bash
python orchestrator-ai.py
```
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
