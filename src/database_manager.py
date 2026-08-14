import os
import json
import threading

class KamelionLibraryManager:
    def __init__(self, storage_directory="data", filename="kamelion_filaments.json"):
        self.storage_directory = storage_directory
        self.storage_path = os.path.join(self.storage_directory, filename)
        self.lock = threading.Lock()
        self.inventory = {}
        if not os.path.exists(self.storage_directory):
            os.makedirs(self.storage_directory)
        self.load_database_from_disk()

    def load_database_from_disk(self):
        with self.lock:
            if not os.path.exists(self.storage_path):
                self.inventory = self._seed_default_database()
                self._write_to_disk_unlocked()
            else:
                try:
                    with open(self.storage_path, "r", encoding="utf-8") as f:
                        self.inventory = json.load(f)
                except (json.JSONDecodeError, IOError):
                    self.inventory = self._seed_default_database()
                    self._write_to_disk_unlocked()

    def _seed_default_database(self):
        return {
            "presets": {
                "generic_white": {"brand": "Generic", "name": "Generic PLA White", "td": 6.5, "hex": "#ffffff", "type": "PLA"},
                "generic_black": {"brand": "Generic", "name": "Generic PLA Black", "td": 0.4, "hex": "#000000", "type": "PLA"},
                "generic_gray": {"brand": "Generic", "name": "Generic PLA Gray", "td": 2.5, "hex": "#808080", "type": "PLA"}
            },
            "custom_spools": {
                "spool_001": {"brand": "Bambu Lab", "name": "Bambu PLA Basic Black", "td": 0.4, "hex": "#111111", "type": "PLA"},
                "spool_002": {"brand": "Polymaker", "name": "PolyLite White", "td": 7.0, "hex": "#fafafa", "type": "PLA"}
            }
        }

    def _write_to_disk_unlocked(self):
        try:
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(self.inventory, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Failed writing data: {str(e)}")

    def add_custom_spool(self, brand, name, td_value, hex_code, material_type="PLA"):
        with self.lock:
            spool_id = f"spool_{len(self.inventory['custom_spools']) + 1:03d}"
            self.inventory["custom_spools"][spool_id] = {"brand": brand, "name": name, "td": float(td_value), "hex": hex_code.lower(), "type": material_type}
            self._write_to_disk_unlocked()
            return spool_id

    def resolve_unknown_filament_fallback(self, color_family_query):
        query = color_family_query.lower()
        if "white" in query: return self.inventory["presets"]["generic_white"]
        elif "black" in query or "dark" in query: return self.inventory["presets"]["generic_black"]
        else: return self.inventory["presets"]["generic_gray"]
