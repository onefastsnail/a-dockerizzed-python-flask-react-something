#this is the application's entry point

import os

#from our app module lets bring in the create_app method
#this create a new flash instance and sets our routes etc and returns it
from app import create_app

# lets get our FLASK_CONFIG env var on the host, this is set from our docker compose file
config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')