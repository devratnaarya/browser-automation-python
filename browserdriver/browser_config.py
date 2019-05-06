import os

def get_driver_path():
    return str(os.path.dirname(os.path.abspath('chromedriver'))) + '/browserdriver/chromedriver'