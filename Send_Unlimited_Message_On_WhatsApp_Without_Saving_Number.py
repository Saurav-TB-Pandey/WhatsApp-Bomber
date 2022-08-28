import webbrowser               # It Is Used To Open Or Close Any URl
import pyautogui as pandeyji    # It Is A Module Used For Automation
import time                     # It Is Used For Time
import urllib.request           # It Is A Module Used To Check URL

print("""|--------------------------------------|""")
print("| This Program Is Written By Pandey JI |")
print("""|--------------------------------------|\n""")

# Defining Function
def internet_on():      # Checking Internet Is On Or Not
    try:
        urllib.request.urlopen("https://www.google.com/",timeout=2)
        return True
    except:
        return False

if internet_on()==True:
    i=0
    num=input("Enter Victim's Number With Country Code : ")           # Reading Mobile Number
    message=input("Write Your Message : ")          # Reading Message
    limit=input("Enter Total Number Of Messages You Want To Send : ")   # Reading Number Of Messages
    print("\nPlease Wait For 30 Seconds")
    time.sleep(0.3)

    num="https://web.whatsapp.com/send?phone="+num+"&text&type=phone_number&app_absent=0"

    webbrowser.open(num)        # Opening URL

    time.sleep(30)              # Program Will Stop For 30 Seconds SO That URL Will Open

    while i<int(limit):
        pandeyji.write(message)     # Writing Message On WhatsApp
        pandeyji.press("enter")     # Pressing Enter Button
        time.sleep(0.4)
        i=i+1

else:
    print("""You Are Not Connected With Internet,
    Please Connect And Try Again""")
    time.sleep(3)
    exit()      # Closing Program