#from .common import base
import pandas as pd
import numpy as np
from sqlalchemy import text
import os
import sys

sys.path.append('..')
from common.base import session, engine
base_path = os.path.abspath(__file__ + "/../../../")

soccer_path = f"{base_path}/data/raw/source/euro_soccer.zip"


