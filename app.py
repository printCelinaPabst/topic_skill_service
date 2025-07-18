#Import von Standardbibliotheken
import os                        #Für Pfadoperationen, um Dateipfade betriebssystemunabhängig zu behandeln
from flask import Flask, jsonify # Flask: Basisobjekt der Webanwendung / jsonify: wandelt Python-Daten in JSON um,damit der Client sie versteht
from data_manager import JsonDataManager


app = Flask(__name__) #Flaskanwendung (Flaskapp) erstellt __name__ sorgt dafür,das Flask weiß wo der Einstiegspunkt ist-wichtig für Routing und Debugging
data_manager = JsonDataManager()

# Pfade zu den Daten werden sicher und dynamisch generiert
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data') #__file__ zeigt auf die aktuelle Datei
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json') #baut korrekte Pfade zusammen Voteil:funktioniert auf Windows,Linux gleichermaßen
SKILLS_FILE = os.path.join(DATA_DIR, 'skills.json')
@app.route('/') # eine einfache Root-Route (Startseite) die zeigt, dass die App läuft.Praktisch für erste Tests und Health-Checks,
def hello_world():
    return "Hello from Topic and Skill Services!"


#API-Endpunkt /topics      
@app.route('/topics', methods=['GET'])
#           Ressource    Methode

@app.route('/skills', methods=['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)


def get_topics():
    topics = data_manager.read_data(TOPICS_FILE) # ruft die JSON-Datei ab
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