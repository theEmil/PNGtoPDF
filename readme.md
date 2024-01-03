Das ist ein Programm, dass automatisch alle PNG Bilder in einem Ordner in PDF Dateien umwandelt.

Dadurch get die Kompilierung von Latex-Code deutlich schneller.

Zunächst wird der angegebene Dateipfad und alle Unterordner nach .png und .jpg Dateien untersucht.

Das Programm erkennt, welche Bilder seit dem letzten Erstellen der .pdf-Datei verändert wurden.

Es aktualisiert alle, die geändert wurden.

Bilder, zu denen keine entsprechende .pdf-Datei existiert, werden ebenfalls umgewandelt.

Die umgewandelten Dateien liegen am gleichen Ort mit dem gleichen Namen.

Lediglich die Dateiendung wurde zu .pdf geändert.

Dadurch kann man im Latex-Code mit Suchen und Ersetzen die Bilder sehr leicht austauschen.

Neue Funktion:

    Wenn viele Bilder umgewandelt/aktualisiert werden sollen ist das Programm sehr langsam. 
    
    Deswegen gibt es jetzt die Möglichkeit, die Bilder mit Hilfe von Multiprocessing umzuwandeln.
    
    Dadurch geht es bei vielen Bildern sehr viel schneller.