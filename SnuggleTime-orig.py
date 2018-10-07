import time
import unicornhat
import schedule

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.rotation(0)
unicornhat.brightness(0.5)

def yellow ():
  unicornhat.clear()
  unicornhat.show()
  unicornhat.set_all(255, 255, 0)
  unicornhat.show()

def indigo ():
  unicornhat.clear()
  unicornhat.show()
  unicornhat.set_all(51, 0, 51)
  unicornhat.show()

schedule.every().day.at("07:30").do(yellow)
schedule.every().day.at("19:00").do(indigo)

while True:
    schedule.run_pending()
    time.sleep(10)