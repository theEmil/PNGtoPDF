import os
import time
from PIL import Image
import multiprocessing
from multiprocessing import Pool


def convert(image_path, pdf_path):

    ########### Bild zu PDF konvertieren
    with Image.open(image_path) as rgba:
        if len(rgba.split()) == 4:
            rgb = Image.new("RGB", rgba.size, (255, 255, 255))
            rgb.paste(rgba, mask=rgba.split()[3])
            rgb.save(pdf_path, "PDF", resolution=50.0)
        else:
            rgba.save(pdf_path, "PDF", resolution=50.0)

def convertImagesMultiThread(folder_path: str, loud = False) -> None:

    print("Converting all .png Images in Path "  + folder_path + " to .pdf-Files...")
    
    ########### Variablen initialisieren
    num_files = 0
    num_updated= 0
    num_converted = 0
    numthreads = multiprocessing.cpu_count()
    pool = Pool(numthreads)
    queue = []


    ########### alle Unterordner durchsuchen
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
                
                num_files += 1
                image_path = os.path.join(root, file)
                pdf_path = os.path.splitext(image_path)[0] + ".pdf"
                
                if os.path.exists(pdf_path) and os.path.getmtime(image_path) <= os.path.getmtime(pdf_path):
                    if loud:
                        print("File " + file + " has not been changed since last conversion")
                    continue
                
                ########### Prüfen ob ein Thread frei ist
                while True:
                    num_unfinished_threads = sum([t.ready() == False for t in queue])
                    if num_unfinished_threads < numthreads:
                        break
                    else:
                        time.sleep(0.1)

                ########### Nächstes Bild in die "Warteschlange" hinzufügen
                        
                if  os.path.exists(pdf_path) and os.path.getmtime(image_path) > os.path.getmtime(pdf_path):
                    num_updated += 1
                    print("Updating File " + file)
                    t = pool.apply_async(convert, args=(image_path, pdf_path))
                    queue.append(t)
                    
                else:
                    num_converted += 1
                    print("Converting File " + file + " to .pdf")
                    t = pool.apply_async(convert, args=(image_path, pdf_path))
                    queue.append(t)

    ########### Warten bis Warteschlange leer ist               
    for t in queue:
        t.get()                       
    print("Found " + str(num_files) + ", updated " + str(num_updated) + " and converted " + str(num_converted) + " to .pdf-Files")

def convertImagesToPDF(folder_path: str, loud = False) -> None:

    print("Converting all .png Images in Path "  + folder_path + " to .pdf-Files...")
    
    ########### Variablen initialisieren
    num_files = 0
    num_updated= 0
    num_converted = 0

    ########### alle Unterordner durchsuchen
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
                
                num_files += 1
                image_path = os.path.join(root, file)
                pdf_path = os.path.splitext(image_path)[0] + ".pdf"
                
                if os.path.exists(pdf_path) and os.path.getmtime(image_path) <= os.path.getmtime(pdf_path):
                    if loud:
                        print("File " + file + " has not been changed since last conversion")
                    continue
                
                ########### Bilder aktualisieren / konververtieren
                if  os.path.exists(pdf_path) and os.path.getmtime(image_path) > os.path.getmtime(pdf_path):
                    num_updated += 1
                    print("Updating File " + file)
                    convert(image_path, pdf_path)
                    
                else:
                    num_converted += 1
                    print("Converting File " + file + " to .pdf")
                    convert(image_path, pdf_path)
                            
                            
    print("Found " + str(num_files) + ", updated " + str(num_updated) + " and converted " + str(num_converted) + " to .pdf-Files")


#Examples: 
#convertImagesToPDF("PATH") # <- singlethreaded
    
#if __name__ == '__main__':
#    convertImagesMultiThread("PATH") # <- multithreaded (very much faster)