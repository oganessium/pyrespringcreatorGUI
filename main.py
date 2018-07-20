from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk
import os
import requests
import math
import subprocess

# Checks

if os.name != 'nt':
    print("Error: This program is made for windows systems and is not yet compatible/tested with Unix systems. you can still try but at your own risk")
    linuxn=""
else:
    try:
        subprocess.check_output(['ubuntu', 'run', 'mkdir', '~/Theme'])
        linuxn="ubuntu run "
    except subprocess.CalledProcessError:
        linuxn="ubuntu run "
        pass
    except FileNotFoundError:
        print(e)
        try:
            subprocess.check_output(['ubuntu1804', 'run', 'mkdir', '~/Theme'])
            linuxn="ubuntu1804 run "
        except subprocess.CalledProcessError:
            linuxn="ubuntu1804 run "
            pass
        except FileNotFoundError:
            print(e)
            try:
                subprocess.check_output(['debian', 'run', 'mkdir', '~/Theme'])
                linuxn="debian run "
            except subprocess.CalledProcessError:
                linuxn="debian run "
                pass
            except FileNotFoundError:
                print(e)
                print("Error: The windows Linux distribution present is either missing or unknown. Please get Ubuntu or Debian from the Windows 10 Store or use a Linux/Mac machine.")
                os.system("pause")
                exit()

def hello(): print('Hello, world!')
master = Tk()
master.title("Respring Logo Creator by Yak")
print(linuxn)
#master.geometry("300x200")

def loaderS():
    filename=askopenfilename()
    print(filename)
    e1.delete(0,END)
    e1.insert(0,filename)
    return

def actualPacking():

    # Original pack method by Yak#7474
    # any .sh script is likely by my man Evan

    if resize.get() == 1:
       modImage()
    else:
        try:
            from PIL import Image
            imageFile = filename
            im1 = Image.open(imageFile.get())
            im1.save("img.png")
        except ModuleNotFoundError:
            print("Error: PIL not found. Run py -m pip install Pillow")
            exit()
    
    os.system("{} mkdir ~/Theme/src".format(linuxn))
    os.system("{} mkdir ~/Theme/dist".format(linuxn))
    os.system("{} mkdir ~/Theme/src/DEBIAN".format(linuxn))
    if os.name=="nt":
        username = os.path.expanduser("~").rsplit("\\", 1)[1]
    else:
        username = os.path.expanduser("~").rsplit("/", 1)[1]
    control = open("control", 'w+')
    control.write("Package: {}\n".format(pkgvstr.get().replace(" ", "")))
    control.write("Name: {}\n".format(namevstr.get()))
    control.write("Version: {}\n".format(vervstr.get()))
    control.write("Architecture: iphoneos-arm\n")
    control.write("Description: {}\n".format(descvstr.get()))
    control.write("Maintainer: {} <{}>\n".format(authnvstr.get(), emailvstr.get()))
    control.write("Author: {} <{}>\n".format(authnvstr.get(), emailvstr.get()))
    control.write("Section: Themes\n")
    control.write("Depends: com.anemonetheming.anemone\n")
    control.close()
    path = os.path.realpath(__file__).replace("\\", "/")
    path=path.replace("C:","/mnt/c")
    path=path.replace(" ", "\\ ")
    path=path.rsplit("/", 1)[0]
    name=namevstr.get()
    name=name.replace(" ", "\ ")
    os.system("{} mv {}/control ~/Theme/src/DEBIAN/".format(linuxn, path))
    os.system("{} mkdir ~/Theme/src/Library".format(linuxn))
    os.system("{} mkdir ~/Theme/src/Library/Themes".format(linuxn))
    os.system("{} mkdir ~/Theme/src/Library/Themes/{}.theme".format(linuxn, name))
    os.system("{} mkdir ~/Theme/src/Library/Themes/{}.theme/Bundles".format(linuxn, name))
    os.system("{} mkdir ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI".format(linuxn, name))
    fg=name
    os.system("{} cp {}/img.png ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI/apple-logo@2x~ipad.png".format(linuxn, path, name))
    os.system("{} cp {}/img.png ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI/apple-logo@3x~iphone.png".format(linuxn, path, name))
    os.system("{} cp {}/img.png ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI/apple-logo-black@2x~ipad.png".format(linuxn, path, name))
    os.system("{} cp {}/img.png ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI/apple-logo@2x~iphone.png".format(linuxn, path, name))
    os.system("{} cp {}/img.png ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI/apple-logo-black@2x~iphone.png".format(linuxn, path, name))
    os.system("{} cp {}/img.png ~/Theme/src/Library/Themes/{}.theme/Bundles/com.apple.ProgressUI/apple-logo-black@3x~iphone.png".format(linuxn, path, name))

    info = open("Info.plist", "w+")
    info.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    info.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
    info.write('<plist version="1.0">\n')
    info.write('<dict>\n')
    info.write('\t<key>PackageName</key>\n')
    info.write('\t<string>{}</string>\n'.format(name))
    info.write('</dict>\n</plist>')
    info.close()
    os.system("{} mv {}/Info.plist ~/Theme/src/Library/Themes/{}.theme/Bundles/".format(linuxn, path, fg))
    os.system("{} chmod -R 0755 ~/Theme/src/DEBIAN".format(linuxn))
    os.system("{} dpkg-deb -b -Zgzip ~/Theme/src ~/Theme/dist".format(linuxn))
    os.system("{} mv ~/Theme/dist/{}_{}_iphoneos-arm.deb {}/".format(linuxn, pkgvstr.get(), vervstr.get(), path))
    os.system("{} rm -r ~/Theme/src".format(linuxn))


def modImage():
    try:
        from PIL import Image
        imageFile = filename
        im1 = Image.open(imageFile.get())
        owidth, oheight = im1.size
        width=300
        height=math.floor((width*oheight)/owidth)
        im = im1.resize((width, height), Image.BICUBIC)
        ext = ".png"
        im.save("img" + ext)
    except ModuleNotFoundError:
        print("Error: PIL not found. Run: py -m pip install Pillow")
        exit()

Label(master, text="Image Path").grid(row=0, sticky=W)
Label(master, text="Name").grid(row=1, sticky=W)
Label(master, text="Bundle ID").grid(row=2, sticky=W)
Label(master, text="Version").grid(row=3, sticky=W)
Label(master, text="Description").grid(row=4, sticky=W)
Label(master, text="Author").grid(row=5, sticky=W)
Label(master, text="E-Mail").grid(row=6, sticky=W)
resize = IntVar()
Checkbutton(master, text="Auto-Resize?", variable=resize).grid(row=8, sticky=W)


filename=StringVar()
namevstr=StringVar()
pkgvstr=StringVar()
vervstr=StringVar()
descvstr=StringVar()
authnvstr=StringVar()
emailvstr=StringVar()

e1 = Entry(master, textvariable=filename)
name = Entry(master, textvariable=namevstr)
pkg = Entry(master, textvariable=pkgvstr)
ver = Entry(master, textvariable=vervstr)
desc = Entry(master, textvariable=descvstr)
authn = Entry(master, textvariable=authnvstr)
email = Entry(master, textvariable=emailvstr)

browsee1 = Button(master, text="...", command=loaderS).grid(padx=2, pady=2, row=0, column=2, sticky=[W,E])

e1.grid(padx=2, pady=2, row=0, column=1)
name.grid(padx=2, pady=2, row=1, column=1)
pkg.grid(padx=2, pady=2, row=2, column=1)
ver.grid(padx=2, pady=2, row=3, column=1)
desc.grid(padx=2, pady=2, row=4, column=1)
authn.grid(padx=2, pady=2, row=5, column=1)
email.grid(padx=2, pady=2, row=6, column=1)


from io import BytesIO

response = requests.get("https://cdn.discordapp.com/attachments/468442362058768405/469650715682275328/Stacks.png")
img = Image.open(BytesIO(response.content))
img = img.resize((100, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

panel = Label(master, image = img)

panel.grid(rowspan=9, columnspan=3, row=0, column=3, padx=20, pady=20, sticky=N)

eee = Button(master, text="Create!", command=actualPacking).grid(padx=5, pady=5, row=10, sticky=[W,E])

master.mainloop()