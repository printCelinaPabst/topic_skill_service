import json
import os

class JsonDataManager:

    def __init__(self):
        pass

    def read_data(self, filepath):
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

            pass

        def write_data(self, filepath, data):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            try:
                with open(filepath, encoding="utf-8")as file:
                    json.dump(data, file, indent=4)
                    return True
            except Exception as e:
                print(f"Ein unerwarteter Fehler ist aufgetreten beim Schreiben von {filepath}: {e}")
                return False


            pass