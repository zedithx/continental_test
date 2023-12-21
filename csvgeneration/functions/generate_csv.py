import json
import pandas as pd


def vehicular_data(filepath):
    """Generate vehicular_data.csv which consists of all fields of json file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    data = data['imu_data']
    df = pd.DataFrame(data)

    df.to_csv('vehicular_data.csv')



def mag_high(filepath):
    """Generate mag_high.csv which only has magy > 0.09."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    data = data['imu_data']
    df = pd.DataFrame(data)
    df = df[df['magy'] > 0.09]
    df.to_csv('mag_high.csv')


def mag_low(filepath):
    """Generate mag_high.csv which only has magy < 0.09."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    data = data['imu_data']
    df = pd.DataFrame(data)
    df = df[df['magy'] < 0.09]
    df.to_csv('mag_low.csv')