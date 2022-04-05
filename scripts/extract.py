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


def truncate_drive_table():
    session.execute(
        text("TRUNCATE TABLE drive ;ALTER SEQUENCE drive_id_seq RESTART;"))
    session.commit()
    print("['Load'] Drive table Truncated")

def load_new_vehicle_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    df = pd.read_csv(vehicle_path)
    conn = engine.connect()
    df.to_sql('vehicle', conn, if_exists='replace')

    import zipfile
with zipfile.ZipFile("file.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")

def main():
    print("[Extract] Start")
    print("[Extract] Downloading snapshot")
    download_snapshot()
    print(f"[Extract] Saving data from '{source_path}' to '{raw_path}'")
    save_new_raw_data()
    print(f"[Extract] End")

if __name__ == "__main__":
    print('[Load] Converting Data')
    calc_distance_using_lat_long()
    calc_distance_using_velocity()
    print('[Load] Dataframes to PSQL')
