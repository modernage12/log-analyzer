'''
Semplice programma per estrarre IP da file di log e conteggiare codici evento e IP.
Vengono infine filtrati in base a limiti e stampati solo quelli che superano questi limiti.
Viene infine stampata una panoramica sui conteggi dei singoli eventi nel totale.

Usati: open() con readlines(), dictionaries, lists, strings, string function .split()
for loops, if statements annidati, f-strings
'''

ERROR_404_LIMIT = 5  # Threshold per filtro 404
IP_LIMIT = 7  # Threshold per filtro IP

# Funzione per aprire log.txt e filtrare
# Itero per ogni singolo elemento nella lista prendendo quindi le singole stringhe
def log_counter():
    # Apro il file log.txt
    log = open("log.txt", "r", encoding="UTF-8")

    # Inizializzo dictionaries e costanti

    ip_dict = {}  # Dict contenente gli IP e count di essi
    code_dict = {}  # Dict contenente i codici (200, 404) e count di essi
    dict_404 = {}  # Dict contenente solo IP con 404 come errore e il loro count

    for string in log.readlines():
        ip_address = string.split()[0] # divido la stringa, prendo IP che si trova per primo
        code = string.split()[-1] # divido la stringa, prendo il codice che si trova alla fine

        # Controlli per aggiungere in dizionario o aumentare il count se esiste già IP nel dizionario
        if ip_address in ip_dict:
            ip_dict[ip_address] += 1 # Se esiste, aumenta il count di 1
        else:
            ip_dict[ip_address] = 1 # Se non esiste, aggiungilo al dizionario e metti 1 come valore e IP come Key

        # Stessa logica di prima ma per i codici
        if code in code_dict:
            code_dict[code] += 1
        else:
            code_dict[code] = 1

        # check per filtrare IP con codice 404
        if code == "404":
            if ip_address in dict_404: # se è codice 404 allora controlla se l'IP si trova in dict_404
                dict_404[ip_address] += 1 # se esiste, aumenta il count del value di +1
            else:
                dict_404[ip_address] = 1 # se non esiste lo aggiunge con IP come Key e count come Value

    # Chiudo il file aperto
    log.close()

    return ip_dict, code_dict, dict_404

# Stampo i risultati
def ip_result(ip_dict):
    print(f"IP con più di {IP_LIMIT} richieste:\n")
    for ip, count in ip_dict.items(): # con .items() ritorno key-value pair, passo Key a ip e Value a count
        if count > IP_LIMIT: # filtro in base al threshold
            print(f"IP: {ip} | Richieste: {count}")

def code_result(dict_404):
    print(f"\nIP con più di {ERROR_404_LIMIT} 404 Error:\n")
    for ip, count in dict_404.items():
        if count > ERROR_404_LIMIT:
            print(f"IP: {ip} | Count 404: {count}")

# Stampo i conteggi dei codici in totale
def count_result(code_dict):
    print("\nConteggio codici\n")
    for code, count in code_dict.items():
        print(f"Codice: {code} | Count: {count}")

ip_dict, code_dict, dict_404 = log_counter()
ip_result(ip_dict)
code_result(dict_404)
count_result(code_dict)
