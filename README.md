# BashBoot

Hier liegen ausgewählte Quellen zum Bash BootCamp der PC-und Internet Teams BB. 

## wheatherin
Der Ansatz ist prinzipiell interessant, statt bash habe ich das Ganze aber in python implementiert.

## substdigits.sh
Nachdem die 1. Version mit hart kodierten sed Ersetzungen für eine 24MB ziffernlastige Textdatei unter
20 Sekunden benötigte, die Musterlösungen dagegen 30 Minuten, musste eine andere schnelle, aber gleichzeitig
flexible Lösung her: Das Skript generiert aus einer Konvertierungstabelle ein dediziertes Skript
mit hart kodierten sed Befehlen, das dann nach Rückfrage automatisch gestartet wird.
