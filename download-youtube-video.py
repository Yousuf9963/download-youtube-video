print("Thank you")

print("[+] Tool Namee:Download-Youtube-Videos")

print("[+] Author:Yousuf Shafi'i Muhammad.(Junior Programmer")

print("[+] Version:1.3")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/download-youtube-video")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] I hope for you good future and i am willing that you will come high effort.")

print("")

import pytube

except ModuleNotFoundError:
    print("\033[1;31;40m Some requirements are missing!\n\nRun \"pip install -r requirements.txt\" then run \"python3 download-youtube-video.py \"\033[1;37;40m" )
    t.sleep(2)
    exit()
    
    from pytube import YouTube
    
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter Youtube video URL to download:")

print("")

print("downloading please wait ........")
print("downloading please wait Thank you  0%")
print("downloading please wait Thank you  10%")
print("downloading please wait Thank you  20%")
print("downloading please wait Thank you  40%")
print("downloading please wait Thank you  60%")
print("downloading please wait Thank you  70%")
print("downloading please wait Thank you  80%")
print("downloading please wait Thank you  90%")
print("downloading please wait Thank you  100%")
print("Successfully downloaded  Thank you.")

Download(link)
