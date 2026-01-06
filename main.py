import tkinter as tk
from tkinter import filedialog, messagebox
from stl import mesh
import os
import time
from colorama import init, Fore, Style
from tqdm import tqdm

# Initialisiere Colorama für bunte Konsolenausgabe
init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}#################################################
#                                               #
#   {Fore.YELLOW}3D PRINT COST CALCULATOR - PRO EDITION{Fore.CYAN}      #
#                                               #
#################################################{Fore.MAGENTA}
      _____      _____      _____
     |     |    |     |    |     |
     | [ ] |    | [ ] |    | [ ] |
  ___|_____|____|_____|____|_____|___
{Style.RESET_ALL}"""
    print(banner)

def calculate_costs():
    print_banner()
    
    # --- Konfiguration ---
    FILAMENT_PREIS_PRO_KG = 10.0  # €
    STROM_VERBRAUCH_KW = 0.095     # kWh pro Stunde
    STROM_PREIS_KWH = 0.25         # €
    DICHTE_PLA = 1.25              # g/cm³
    
    # 1. Datei auswählen
    root = tk.Tk()
    root.withdraw() 
    
    print(f"{Fore.BLUE}Warte auf Dateiauswahl...\n")
    file_path = filedialog.askopenfilename(
        title="STL-Datei auswählen",
        filetypes=[("STL Files", "*.stl")]
    )
    
    if not file_path:
        print(f"{Fore.RED}Abgebrochen: Keine Datei ausgewählt.")
        input(f"\n{Fore.WHITE}Drücke Enter zum Beenden...{Fore.BLACK}")
        return

    try:
        # 2. Simulation eines Ladevorgangs mit Statusbar
        print(f"{Fore.YELLOW}Analysiere STL-Geometrie:\n")
        for _ in tqdm(range(100), desc="Berechnung läuft", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            time.sleep(0.01) # Simuliert Rechenzeit für das Mesh
        
        # STL laden und Volumen berechnen
        your_mesh = mesh.Mesh.from_file(file_path)
        volume_cm3, cog, inertia = your_mesh.get_mass_properties()
        volume_cm3 = volume_cm3 / 1000 
        
        # 3. Gewicht & Kosten berechnen
        gewicht_gramm = volume_cm3 * DICHTE_PLA
        filament_kosten = (gewicht_gramm / 1000) * FILAMENT_PREIS_PRO_KG
        druckzeit_stunden = 5 
        strom_kosten = druckzeit_stunden * STROM_VERBRAUCH_KW * STROM_PREIS_KWH
        gesamt_kosten = filament_kosten + strom_kosten

        # 4. Ergebnis-String für Konsole und Datei
        dateiname = os.path.basename(file_path)
        ergebnis_text = (
            f"ERGEBNIS FÜR: {dateiname}\n"
            f"{'-'*40}\n"
            f"Geschätztes Gewicht: \t {gewicht_gramm:.2f} g\n"
            f"Materialkosten: \t {filament_kosten:.2f} €\n"
            f"Stromkosten ({druckzeit_stunden}h): \t {strom_kosten:.2f} €\n"
            f"{'-'*40}\n"
            f"GESAMTKOSTEN: \t\t {gesamt_kosten:.2f} €"
        )

        # 5. Konsolenausgabe (Schön bunt)
        print(f"\n{Fore.GREEN}{'='*40}")
        print(f"{Fore.GREEN}{ergebnis_text}")
        print(f"{Fore.GREEN}{'='*40}\n")

        # 6. Abfrage: Speichern?
        antwort = messagebox.askyesno("Speichern?", f"Möchten Sie das Ergebnis für '{dateiname}' speichern?")
        
        if antwort:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=f"Kalkulation_{dateiname.replace('.stl', '')}.txt",
                title="Ergebnis speichern unter..."
            )
            if save_path:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write("=== 3D DRUCK KOSTEN KALKULATION ===\n\n")
                    f.write(ergebnis_text)
                print(f"{Fore.CYAN}✔ Datei erfolgreich gespeichert unter:\n{Style.BRIGHT}{save_path}")
                messagebox.showinfo("Erfolg", f"Datei wurde gespeichert unter:\n{save_path}\n")
            else:
                print(f"{Fore.YELLOW}Speichervorgang abgebrochen.")

    except Exception as e:
        error_msg = f"Fehler beim Berechnen: {e}"
        print(f"{Fore.RED}{error_msg}")
        messagebox.showerror("Fehler", error_msg)

    # 7. Programm offen halten
    print(f"{Fore.WHITE}-----------------------------------------")
    input(f"{Fore.YELLOW}Berechnung abgeschlossen. Drücke ENTER zum Beenden...{Fore.BLACK}")

if __name__ == "__main__":
    calculate_costs()