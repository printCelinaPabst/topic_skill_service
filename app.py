#Import von Standardbibliotheken

import json # Zum Einlesen und Verarbeiten von JSON-Dateien
import os #Für Pfadoperationen, um Dateipfade betriebssystemunabhängig zu behandeln

# Import aus dem Flask-Framework
from flask import Flask, jsonify # Flask: Basisobjekt der Webanwendung / jsonify: wandelt Python-Daten in JSON um,damit der Client sie versteht


app = Flask(__name__) #Flaskanwendung (Flaskapp) erstellt __name__ sorgt dafür,das Flask weiß wo der Einstiegspunkt ist-wichtig für Routing und Debugging

# Pfade zu den Daten werden sicher und dynamisch generiert
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') #__file__ zeigt auf die aktuelle Datei
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json') #baut korrekte Pfade zusammen Voteil:funktioniert auf Windows,Linux gleichermaßen

@app.route('/') # eine einfache Root-Route (Startseite) die zeigt, dass die App läuft.Praktisch für erste Tests und Health-Checks,
def hello_world():
    return "Hello from Topic and Skill Services!"

#Eine Funktion zum sicheren Einlesen ein JSON-Datei
def read_json_file(filepath):
    if not os.path.exists(filepath): # gibt eine leere Liste zurück, wenn die Datei nicht existiert
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file) #nutzt json.load() um den Inhalt zu parsen.
        
    except json.JSONDecodeError: # für kaputte JSON-Syntax
        print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
        return [] 
    except Exception as e: #für allgemeine Probleme beim Lesen
        print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
        return []
    
#API-Endpunkt /topics      
@app.route('/topics', methods=['GET'])
#           Ressource    Methode
def get_topics():
    topics = read_json_file(TOPICS_FILE) # ruft die JSON-Datei ab
    return jsonify(topics) #wandelt sie mit jsonify in eine Web-taugliche Antwort um
                           #Client(Browser oder JavaScript-App) bekommt ein sauberes JSON zurück

if __name__ == '__main__': # Start der Anwendung, wenn die Datei direkt ausgeführt wird
    app.run(debug=True, port=5000) #debug=True --> die Anwendung läuft im Debug-Modus, 
                                   #die App startet automatisch neu, wenn man Änderungen am Code macht
                                   #zeigt Fehler direkt im Browser inkl. Möglichkeit, Code zu inspizieren
                                   #Im Terminal bekommst man mehr Logs und Meldungen als im normalen Modus
                                   #Wenn z. B. JSON falsch ist oder eine Route fehlt, sieht man direkt die Ursache
                                   #wenn was schief gelaufen ist, sieht man wo und warum

                                   #port=5000 -->Lokaler Port, auf dem der Server läuft