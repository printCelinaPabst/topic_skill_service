#Import von Standardbibliotheken

import uuid # Importiere das UUID-Modul, um eindeutige IDs zu generieren
import os                        #Für Pfadoperationen, um Dateipfade betriebssystemunabhängig zu behandeln
from flask import Flask, jsonify, request # Flask: Basisobjekt der Webanwendung / jsonify: wandelt Python-Daten in JSON um,damit der Client sie versteht / request ist notwendig um auf den Request-Body zuzugreifen
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

#Endpunkt: Alle Topics abrufen (GET-Anfrage an die Ressource)     
@app.route('/topics', methods=['GET'])
#           Ressource    Methode

#Endpunkt: Einzelnes Topic nach ID abrufen (GET mit Pfadparameter)
@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    topics = data_manager.read_data(TOPICS_FILE)
    topic = [t for t in topics if t['id'] == id]
    if topic:
        return jsonify(topic)
    else:
        return jsonify({"error":"Topic not found."})

#Hilfsfunktion: Gibt alle Topics als JSON zurück
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE) # ruft die JSON-Datei ab
    return jsonify(topics) #wandelt sie mit jsonify in eine Web-taugliche Antwort um
                           #Client(Browser oder JavaScript-App) bekommt ein sauberes JSON zurück

#----------------------------------------
#API-Endpunkt /skills
@app.route('/skills', methods=['GET'])

#Endpunkt: Alle Skills abrufen (GET-Anfrage an die Ressource) 
@app.route('/skills/<id>', methods=['GET'])
def get_skill_by_id(id):
    skills = data_manager.read_data(SKILLS_FILE)
    skill = next((skill for skill in skills if skill.get('id').lower() == id.lower()),None)
    if skill:
        return jsonify(skill)
    else:
        return jsonify({"error":"Skill not found."}), 404


#Hilfsfunktion: Gibt alle Skills als JSON zurück
def get_skills():
    skills = data_manager.read_data(SKILLS_FILE)
    return jsonify(skills)

@app.route('/topics', methods=['POST'])
def create_topic():
    new_topic_data = request.json

    if not new_topic_data or 'name' not in new_topic_data or 'description' not in new_topic_data:
        return jsonify({"error": "'name' and 'description' for the topic are required in the request body."}), 400

    new_topic_id = str(uuid.uuid4())

    topic = {
        "id": new_topic_id,
        "name": new_topic_data['name'],
        "description": new_topic_data['description']
        }
    
    topics = data_manager.read_data(TOPICS_FILE)
    topics.append(topic)

    data_manager.write_data(TOPICS_FILE, topics)

    return jsonify(topic), 201


if __name__ == '__main__': # Start der Anwendung, wenn die Datei direkt ausgeführt wird
    app.run(debug=True, port=5000) #debug=True --> die Anwendung läuft im Debug-Modus, 
                                   #die App startet automatisch neu, wenn man Änderungen am Code macht
                                   #zeigt Fehler direkt im Browser inkl. Möglichkeit, Code zu inspizieren
                                   #Im Terminal bekommst man mehr Logs und Meldungen als im normalen Modus
                                   #Wenn z. B. JSON falsch ist oder eine Route fehlt, sieht man direkt die Ursache
                                   #wenn was schief gelaufen ist, sieht man wo und warum

                                   #port=5000 -->Lokaler Port, auf dem der Server läuft