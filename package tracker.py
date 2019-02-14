import time
import ctypes
import webbrowser

from urllib.request import urlopen


#ctypes.windll.user32.MessageBoxW(0,"Result poker has started (pythonw.exe)", "Result Poker", 0)
poke_count = 1
r_url = "http://www.indiapost.gov.in/SpeedNetTracking.aspx?articlenumber=yourtrackingnumber"

while True:
    try:
        page = urlopen(r_url)
        updated = str(page.read()) #[2996:3007]
        #if len(updated) != 
        print(len(updated))
        if len(updated) != 7964:
            print("No changes")
     #       ctypes.windll.user32.MessageBoxW(0,"Results not yet updated", "Result Poker", 0)
        else:
            webbrowser.open(r_url)
            ctypes.windll.user32.MessageBoxW(0,"Results Updated", "Result Poker", 0)
        poke_count += 1
        print("going to sleep")
        time.sleep(60*60)
        print("back to work")
    except Exception as e:
        print(e)
     #   time.sleep(60*60)
