# ==============================================================================
# KM-MODULE-05: src/manifest_builder.py
# Universal Project Manifest File Assembly Exporter System
# ==============================================================================

class KamelionManifestExporter:
    def __init__(self, output_directory="dist"):
        self.output_dir = output_directory
        if not os.path.exists(self.output_dir) and 'os' in globals():
            os.makedirs(self.output_dir)

    def assemble_universal_project_profile(self, custom_spools_dict, slicing_matrix_grid):
        """
        Compiles the full slice computation grid and active filament materials 
        into an uncorrupted, standardized local configuration dictionary schema.
        """
        project_manifest_schema = {
            "application": "Kamelion Slicing Studio",
            "version": "1.0.0",
            "active_materials": custom_spools_dict,
            "calculated_matrix_checksum": hash(str(slicing_matrix_grid[:10])),
            "total_computed_rows": len(slicing_matrix_grid)
        }
        return project_manifest_schema

    def export_text_instruction_manifest_sheet(self, project_schema, file_destination_path="dist/instructions.txt"):
        """
        Generates a clean, human-readable text receipt index detailing exactly 
        how the user must arrange their filament rolls inside their physical AMS setup.
        """
        print(f"[Exporter] Writing standalone text recipe manifest sheet: {file_destination_path}")
        try:
            with open(file_destination_path, "w", encoding="utf-8") as f:
                f.write("=====================================================================\n")
                f.write("      KAMELION AUTOMATED HARDWARE SLICING RUN - PRINT RECEIPT        \n")
                f.write("=====================================================================\n\n")
                f.write(f"Application Source Track: {project_schema['application']} v{project_schema['version']}\n")
                f.write(f"Total Grid Vectors Processed: {project_schema['total_computed_rows']} depth tracks\n\n")
                f.write("--- HARDWARE SLOT LOAD METRIC INSTRUCTIONS ---\n")
                f.write("Arrange your multi-material feeder bays matching this mapping exactly:\n\n")
                
                # Enumerate active spools down into the text receipt columns
                for i, (spool_id, data) in enumerate(project_schema["active_materials"].items(), 1):
                    f.write(f" -> AMS Feeder Slot [{i}]: Brand: {data.get('brand')} | Name: {data.get('name')} | Hex Color: {data.get('hex')} | Target TD Value: {data.get('td')}\n")
                    
                f.write("\n=====================================================================\n")
                f.write("      EXECUTE MATERIAL CALIBRATION IN ORCASLICER/BAMBU STUDIO       \n")
                f.write("=====================================================================\n")
            return True
        except IOError as e:
            print(f"[Exporter Fault] Failed writing manifest file: {str(e)}")
            return False

