# 🖨️ 3D-Druck Kostenrechner

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Ein einfacher und benutzerfreundlicher Kostenrechner für 3D-Drucke. Berechne Material- und Stromkosten basierend auf STL-Dateien mit einer schönen, farbigen Konsolenoberfläche.

## ✨ Features

- **STL-Datei Analyse**: Automatische Berechnung des Volumens und Gewichts aus STL-Dateien
- **Kostenberechnung**: Schätzt Material- und Stromkosten für Ihren 3D-Druck
- **Moderne UI**: Farbige Konsolenausgabe mit Fortschrittsbalken
- **Speicheroption**: Ergebnisse können als Textdatei gespeichert werden
- **Einfach zu bedienen**: Grafische Dateiauswahl über Tkinter

## 🚀 Installation

### Voraussetzungen
- Python 3.8 oder höher
- pip für die Paketinstallation

### Schritte
1. Repository klonen:
   ```bash
   git clone https://github.com/IhrBenutzername/3D-Druck_Kostenrechner.git
   cd 3D-Druck_Kostenrechner
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Nutzung

1. Starten Sie das Programm:
   ```bash
   python main.py
   ```

2. Wählen Sie eine STL-Datei über den Dateidialog aus.

3. Das Programm analysiert die Datei und zeigt die geschätzten Kosten an.

4. Optional: Speichern Sie das Ergebnis als Textdatei.

### Beispiel Ausgabe
```
==================================================
ERGEBNIS FÜR: mein_modell.stl
----------------------------------------
Geschätztes Gewicht: 	 45.67 g
Materialkosten: 	 0.46 €
Stromkosten (5h): 	 0.12 €
----------------------------------------
GESAMTKOSTEN: 		 0.58 €
==================================================
```

## ⚙️ Konfiguration

Die Kostenparameter können in `main.py` angepasst werden:

```python
FILAMENT_PREIS_PRO_KG = 10.0  # € pro kg Filament
STROM_VERBRAUCH_KW = 0.095    # kWh pro Stunde
STROM_PREIS_KWH = 0.25        # € pro kWh
DICHTE_PLA = 1.25             # g/cm³ für PLA
```

## 🤝 Mitwirken

Beiträge sind willkommen! Bitte öffnen Sie ein Issue für Vorschläge oder einen Pull Request für Verbesserungen.

1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz - siehe die [LICENSE](LICENSE) Datei für Details.

## 🙏 Danksagungen

- [numpy-stl](https://github.com/WoLpH/numpy-stl) für STL-Datei Unterstützung
- [colorama](https://github.com/tartley/colorama) für farbige Konsolenausgabe
- [tqdm](https://github.com/tqdm/tqdm) für Fortschrittsbalken

---

**Hinweis**: Dies ist ein Schätztool. Die tatsächlichen Kosten können je nach Drucker, Material und Druckeinstellungen variieren.
