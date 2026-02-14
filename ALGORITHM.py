import re
import json

class VoraIXHarmonicEngine:
    """
    VORA IX: Vortex Operations & Resonance Architecture
    Unified Engine: Centripetal Recursion + A1-G7-Z1 Vedic Mapping.
    """
    
    def __init__(self):
        # The Tesla Constants
        self.FLUX_NODES = {3, 6, 9}
        self.MATERIAL_CIRCUIT = {1, 2, 4, 8, 7, 5}
        
        # A1-G7-Z1 Cyclical Mapping Standard
        self.VEDIC_MAP = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
            'h': 6, 'i': 5, 'j': 4, 'k': 3, 'l': 2, 'm': 1,
            'n': 1, 'o': 2, 'p': 3, 'q': 4, 'r': 5, 's': 6, 't': 7,
            'u': 6, 'v': 5, 'w': 4, 'x': 3, 'y': 2, 'z': 1
        }

        # The 180-State Convergence Proof Constants
        self.custom_values = {
            "zero": 1552, "one": 215, "two": 742, "three": 76555, 
            "four": 6265, "five": 6555, "six": 653, "seven": 65551, 
            "eight": 55767, "nine": 1515
        }
        
        # Frequency Anchors for Surgical Nudging (Value-Bearing)
        self.ANCHORS = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i"}

    def get_digital_root(self, text):
        """Calculates the Digital Root using the A1-G7-Z1 mapping."""
        # Now includes all characters to ensure nudges are counted
        words = re.findall(r'\b\w+\b', text.lower())
        total_sum = 0
        
        for word in words:
            if word in self.custom_values:
                # Sum the digits of the custom value
                word_val = sum(int(d) for d in str(self.custom_values[word]))
            else:
                word_val = sum(self.VEDIC_MAP.get(char, 0) for char in word)
            total_sum += word_val

        # dr(n) = 1 + ((n - 1) mod 9)
        return (total_sum - 1) % 9 + 1 if total_sum > 0 else 0, total_sum

    def centrifuge(self, intent, current_iteration="", depth=0):
        """Centripetal Recursion: Pulls data toward the 9-State Seal."""
        if not current_iteration:
            current_iteration = intent

        root, raw_sum = self.get_digital_root(current_iteration)
        
        if root == 9:
            return {
                "status": "VORA-VERIFIED",
                "resonance": 9,
                "sum": raw_sum,
                "depth": depth,
                "output": current_iteration
            }

        if depth > 9:
            return {
                "status": "HIGH_ENTROPY", 
                "resonance": root, 
                "sum": raw_sum,
                "depth": depth, 
                "output": current_iteration
            }

        # CALCULATE FREQUENCY GAP: How far are we from a 9?
        gap = (9 - (raw_sum % 9)) % 9
        if gap == 0: gap = 9 # If it's 0 mod 9, we are at a 9.
        
        # Nudge frequency using a Value-Bearing Anchor
        refined_intent = current_iteration + f" {self.ANCHORS[gap]}" 
        return self.centrifuge(intent, refined_intent, depth + 1)

if __name__ == "__main__":
    engine = VoraIXHarmonicEngine()
    
    # 1. Audit the Primary Sequence (The 180-State Proof)
    proof_intent = "zero one two three four five six seven eight nine"
    proof_res = engine.centrifuge(proof_intent)
    
    # 2. Audit the Manifesto (The Real-World Test)
    manifesto = "The stationary center must be reached"
    manifesto_res = engine.centrifuge(manifesto)
    
    print(f"--- VORA IX HARMONIC AUDIT ---")
    print(f"PROOF: {proof_res['status']} | Seal: {proof_res['resonance']} | Sum: {proof_res['sum']}")
    print(f"MANIFESTO INPUT: {manifesto}")
    print(f"MANIFESTO OUTPUT: {manifesto_res['output']}")
    print(f"MANIFESTO SEAL: {manifesto_res['resonance']} | DEPTH: {manifesto_res['depth']}")
    print(f"STATUS: {manifesto_res['status']}")
