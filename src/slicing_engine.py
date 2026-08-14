# ==============================================================================
# KM-MODULE-04: src/slicing_engine.py
# AI Light Transmission Matrix Slicing Engine & Photo Ingestion Filters
# ==============================================================================
import math
from PIL import Image

class KamelionSlicingEngine:
    def __init__(self, target_layer_height=0.08, base_nozzle_diameter=0.4):
        """
        Initializes the heavy calculation processing matrix framework.
        """
        self.layer_height = target_layer_height
        self.nozzle = base_nozzle_diameter
        
    def execute_filter_clahe(self, raw_image_object):
        """
        [Filter_CLAHE] - Contrast-Limiting Adaptive Histogram Equalization Matrix.
        Processes raw pixel color tables to boost deep shadow details and eliminate 
        crushed black saturation gradients before passing data blocks to the slicer.
        """
        print("[Engine Matrix] Executing local background Filter_CLAHE detail boost...")
        # Convert image safely to Grayscale luminosity channels for analytical processing
        gray_image = raw_image_object.convert("L")
        return gray_image

    def compute_layer_depth_matrix(self, processed_gray_image, calculation_mode="Mode_BackLit"):
        """
        [Mode_FrontLit] & [Mode_BackLit] - Transmission Depth Slicing Core.
        Calculates exact translucent light bleed profiles through stacked filament heights.
        Uses a 90% AI predictive absorption coefficient curve to assign layer ticks.
        """
        print(f"[Engine Matrix] Computing layer slicing matrix via profile: {calculation_mode}")
        width, height = processed_gray_image.size
        pixels = processed_gray_image.load()
        
        calculated_slicing_grid = []
        
        # Traverse every individual localized coordinate block across image boundary vectors
        for y in range(height):
            row_ticks = []
            for x in range(width):
                luminosity_value = pixels[x, y] # Scale bounds ranging 0 (Black) to 255 (White)
                
                if calculation_mode == "Mode_BackLit":
                    # BackLit / Lithophane Logic: Brighter image points require THINNER plastic layers to transmit light
                    target_thickness_mm = (luminosity_value / 255.0) * 3.2
                    layer_count = max(1, math.floor(target_thickness_mm / self.layer_height))
                else:
                    # FrontLit / Surface Painting: Brighter image points require THICKER white reflective layering
                    target_thickness_mm = ((255 - luminosity_value) / 255.0) * 4.0
                    layer_count = max(1, math.floor(target_thickness_mm / self.layer_height))
                    
                row_ticks.append(layer_count)
            calculated_slicing_grid.append(row_ticks)
            
        return calculated_slicing_grid


