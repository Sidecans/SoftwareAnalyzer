import os
var = str(os.getcwd())
var = var.split("\\")
drive = var[0]
if os.path.exists(drive + "\\Program Files\\7-Zip"):
    print("Software Found: 7-Zip | Igor Pavlov")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Audition 2022"):
    print("Software Found: Adobe Audition 2022 | Adobe Inc.")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Bridge 2022"):
    print("Software Found: Adobe Bridge 2022 | Adobe Inc.")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Creative Cloud"):
    print("Software Found: Adobe Creative Cloud | Adobe Inc.")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Creative Cloud Experience"):
    print("Software Found: Adobe Creative Cloud | Adobe Inc.")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Illustrator 2022"):
    print("Software Found: Adobe Illustrator 2022 | Adobe Inc.")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Media Encoder 2022"):
    print("Software Found: Adobe Media Encoder 2022 | Adobe Inc.")   
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Photoshop 2022"):
    print("Software Found: Adobe Photoshop 2022 | Adobe Inc.")
if os.path.exists(drive + "\\Program Files\\Adobe\\Adobe Premiere Pro 2022"):
    print("Software Found: Adobe Premiere Pro 2022 | Adobe Inc.")

