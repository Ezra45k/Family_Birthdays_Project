import sys
import schedule as sc
import time
import send_email as e
import datetime as dt
import get_people

job_done = False  # keep track of job state
last_run_date = None  # initialize to none, but will be overwritten by cd when job done.


def check_condition():
    """Checking:
    1) cd != last_run_date (its a new day)
    2) it's the correct time to send a message, and
    3) if there are any messages to send.

    Only if these three conditions are met will the message be sent
    """
    global job_done, last_run_date
    target_time = dt.time(hour=20, minute=34)  # Time of day to send message.
    current_time = dt.datetime.now().time()  # Get ct
    current_date = dt.datetime.now().date()  # Get cd.

    # Reset job_done if it's a new day.
    if last_run_date != current_date:
        job_done = False
        # Make today the last run date.
        last_run_date = current_date

    # Check that the ct is == to tt.
    if current_time.hour == target_time.hour and current_time.minute == target_time.minute:
        # Only run if the job has not been executed today.
        if not job_done:
            messages = get_people.collect_birthdays_this_month()  # get and store messages.
            # Only execute if messages is NOT empty.
            if messages:
                for message in messages:
                    print(f'Message: {message}')
                    job(message)  # Send each message.
            job_done = True  # This prevents message being sent multiple times in one day.
            print('📦 Job done')


def job(message):
    """Send message only when conditions are satisfied."""
    try:
        email_obj = e.DynamicEmail()  # Create email object.
        email_obj.connect_server()  # Initialize server.
        email_obj.send_email('ezra45k@gmail.com', message, '🥳 BIRTHDAY ALERT 🥳')  # Send email.
    # If anything goes wrong exit program gracefully.
    except Exception as ex:
        print(f"An error occurred: {ex}")


# Schedule the job
sc.every(1).seconds.do(check_condition)

try:
    # Outer loop will run infinitely.
    while True:
        # Inner loop only runs when the job has not been completed for the day.
        while not job_done:
            try:
                sc.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                print('👷🏻 User Terminated The Program')
                sys.exit()
        time.sleep(60)
except KeyboardInterrupt:
    print('👷🏻 User Terminated The Program')
    sys.exit()

