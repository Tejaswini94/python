import time
import webbrowser
breakcount=1
timebreak=3
print("the program started on "+time.ctime())
while(breakcount<=timebreak):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=5nyFfZnsyNY")
    print("play video @ "+time.ctime())
    breakcount=breakcount+1
