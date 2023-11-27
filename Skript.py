import os
from PIL import Image

def convert_images_to_pdf(folder_path: str, ) -> None:
    print("Converting all .png Images in Path "  + folder_path + " to .pdf-Files...")
    num_files = 0
    num_updated= 0
    num_converted = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".png") or file.lower().endswith(".jpg"):
                num_files += 1
                image_path = os.path.join(root, file)
                pdf_path = os.path.splitext(image_path)[0] + ".pdf"
                if os.path.exists(pdf_path) and os.path.getmtime(image_path) <= os.path.getmtime(pdf_path):
                    #print("File " + file + " has not been changed since last conversion")
                    continue
                if  os.path.exists(pdf_path) and os.path.getmtime(image_path) > os.path.getmtime(pdf_path):
                    with Image.open(image_path) as rgba:
                        if len(rgba.split()) is 4:
                            rgb = Image.new("RGB", rgba.size, (255, 255, 255))
                            rgb.paste(rgba, mask=rgba.split()[3])
                            rgb.save(pdf_path, "PDF", resolution=50.0)
                            print("File " + file + " was updated")
                            num_updated += 1
                        else:
                            rgba.save(pdf_path, "PDF", resolution=50.0)
                            print("File " + file + " was updated")
                            num_updated += 1
                else:
                    with Image.open(image_path) as rgba:
                        if len(rgba.split()) is 4:
                            rgb = Image.new("RGB", rgba.size, (255, 255, 255))
                            rgb.paste(rgba, mask=rgba.split()[3])
                            rgb.save(pdf_path, "PDF", resolution=50.0)
                            print("File " + file + " was converted to .pdf")
                            num_converted += 1
                        else:
                            rgba.save(pdf_path, "PDF", resolution=50.0)
                            print("File " + file + " was converted to .pdf")
                            num_converted += 1
    print("Found " + str(num_files) + ", updated " + str(num_updated) + " and converted " + str(num_converted) + " to .pdf-Files")
                    
convert_images_to_pdf("PATH")
