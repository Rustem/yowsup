from .env_android import AndroidYowsupEnv
from .env_s40 import S40YowsupEnv
import random

def CURRENT_ENV():
    return random.choice((S40YowsupEnv(), AndroidYowsupEnv()))

