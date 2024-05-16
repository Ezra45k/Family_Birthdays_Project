import sys

import schedule as sc
import time
import send_email as e
import datetime as dt

job_done = False


def job():
    global job_done
    try:
        email_obj = e.DynamicEmail()
        email_obj.connect_server()
        email_obj.send_email('9738205999@vtext.com', 'Only Once')
        job_done = True
    except Exception as ex:
        print(f"An error occurred: {ex}")


def check_condition():
    set_time = dt.time(7, 3)
    current_time = dt.datetime.now().time()
    if set_time.minute == current_time.minute and not job_done:
        job()
    else:
        return False


task = sc.every(1).seconds.do(check_condition)

while True:
    if not job_done:
        try:
            sc.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print('👷🏻 User Terminated The Program')
    elif job_done:
        print('📦 Job Done.')
        sys.exit()
