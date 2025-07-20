import json
import os

class JsonDataManager: #Basisklasse erstellt mit dem Namen JsonDataManager, erster Buchstabe muss immer groß geschrieben sein
                       #-mit der Erstellung einer Basisklasse erstelle ich einen Bauplan

    def __init__(self): # Konstruktor der Klasse, momentan ohne Initialisierung

        pass

    def read_data(self, filepath):
        # Überprüft, ob die Datei existiert. Falls nicht, wird eine leere Liste zurückgegeben.
        if not os.path.exists(filepath):
            return []
        try:
            # Öffnet die Datei im Lesemodus mit UTF-8-Kodierung
            with open(filepath, 'r', encoding='utf-8') as file:
            # Lädt und gibt die JSON-Daten aus der Datei zurück
                return json.load(file)

        except json.JSONDecodeError:
            # Fehlerbehandlung bei ungültiger JSON-Syntax
            print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
            return [] 
        except Exception as e:
            # Allgemeine Fehlerbehandlung beim Lesen der Datei
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
            return []

            #pass

    def write_data(self, filepath, data):
        # Erstellt das Verzeichnis, falls es nicht existiert
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            # Öffnet die Datei im Schreibmodus mit UTF-8-Kodierung
            with open(filepath, 'w', encoding="utf-8") as file:
                # Schreibt die Daten als formatiertes JSON in die Datei
                json.dump(data, file, indent=4)
                return True
        except Exception as e:
            # Allgemeine Fehlerbehandlung beim Schreiben der Datei
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Schreiben von {filepath}: {e}")
            return False


            #pass 