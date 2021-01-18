import os
from environment import Environment

active_environment = Environment[os.environ['ENVIRONMENT']]
