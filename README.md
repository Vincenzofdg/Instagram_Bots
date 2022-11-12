## Need to be Installed
1. python3+
2. pip
3. venv

## Starting project
1. Download and place [ChromeDriver](https://chromedriver.chromium.org/downloads) inside the project
2. python3.10 -m venv .venv
3. source .venv/bin/activate
4. python3.10 -m pip install -r requirements.txt



deactivate


# Main.py
from dotenv import dotenv_values

config = dotenv_values(".env")
print(config['SECRET_TOKEN'])


# .env
ACCESS_TOKEN=ABC123
SECRET_TOKEN=SUPERSECRET123
