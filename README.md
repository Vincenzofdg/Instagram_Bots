1. `pip install selenium python-dotenv`
2. Install ChromeDriver [Link](https://chromedriver.chromium.org/downloads)

# Main.py
from dotenv import dotenv_values

config = dotenv_values(".env")
print(config['SECRET_TOKEN'])


# .env
ACCESS_TOKEN=ABC123
SECRET_TOKEN=SUPERSECRET123
