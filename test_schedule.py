import schedule as sc
import time
import email_class as e
import datetime as dt
from dotenv import load_dotenv
load_dotenv('.env')




def job():
    try:
        load_dotenv('.env')
        email_obj = e.DynamicEmail()
        email_obj.connect_server()
        email_obj.send_email('9738205999@vtext.com', 'Cool', 'It worked!!')
    except Exception as ex:
        print(f"An error occurred: {ex}")



def check_condition():
    set_time = dt.time(21, 44)
    current_time = dt.datetime.now().time()
    if set_time.minute == current_time.minute:
        job()
    else:
        return False



sc.every(1).seconds.do(check_condition)

while True:
    sc.run_pending()
    time.sleep(1)

