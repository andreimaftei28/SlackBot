import os
import time
from flask import Flask
from bot.jobs.scheduler import scheduler

# initialize a Flask app to host the events adapter
# this part is not needed if one choose to create a chron job
app = Flask(__name__)

if __name__ == "__main__":
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('C' if os.name == 'nt' else 'Break'))
    try:
        time.sleep(120)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
    finally:
        scheduler.shutdown()