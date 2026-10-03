# Log Analyzer

Piccolo programma in Python che analizza un file di log di un server web e segnala gli indirizzi IP sospetti.

## Cosa fa

- Legge un file di log (`log.txt`), una richiesta per riga
- Conta quante richieste ha fatto ogni IP
- Conta quante volte compare ogni codice di risposta (per esempio 200 e 404)
- Conta quanti errori 404 ha generato ogni IP
- Stampa solo gli IP che superano le soglie impostate: troppe richieste in totale, oppure troppi errori 404 (un comportamento tipico di chi cerca pagine nascoste come `/admin` o `/backup`)

## Come si usa

Serve Python 3 installato. Metti `log.txt` nella stessa cartella di `main.py`, poi da terminale:

```
python main.py
```

## Formato del log

Ogni riga ha quattro campi separati da spazi: IP, metodo, pagina richiesta e codice di risposta.

```
198.51.100.4 GET /admin 404
203.0.113.7 GET /home 200
```

## Esempio di output

```
IP con più di 7 richieste:

IP: 198.51.100.4 | Richieste: 8
IP: 192.0.2.15 | Richieste: 8
IP: 203.0.113.101 | Richieste: 10
...

IP con più di 5 404 Error:

IP: 198.51.100.4 | Count 404: 7
IP: 192.0.2.15 | Count 404: 6
...

Conteggio codici

Codice: 200 | Count: 31
Codice: 404 | Count: 62
```

## Impostazioni

Le soglie si cambiano in cima a `main.py`:

- `IP_LIMIT`: numero di richieste oltre cui un IP viene segnalato
- `ERROR_404_LIMIT`: numero di errori 404 oltre cui un IP viene segnalato

## Cosa ho usato

Lettura di file, dizionari, stringhe e `.split()`, cicli `for`, `if` annidati, f-string.

## Note

Primo progetto della mia pratica con Python. Il file `log.txt` contiene dati di esempio inventati.
