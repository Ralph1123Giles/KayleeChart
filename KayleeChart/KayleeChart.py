import webbrowser
import os
from pathlib import Path
print(os.getcwd())
#f=open("C:/Users/giles.157/source/repos/KayleeChart/KayleeChart/P.html", "w")
##f.write("Hello")
#f.close()

filepath = Path(r"C:/Users/giles.157/source/repos/KayleeChart/KayleeChart/P.html")
print ("Exists: ", filepath.exists())
print ("URI: ", filepath.as_uri())
result = webbrowser.open(filepath.as_uri())
print("OPENED: ", result)
