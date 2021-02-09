from api_client import get_daily_summary
from s3_uploader import upload_to_s3
import yaml
import sys
from datetime import datetime

def extract_and_upload(date):
    year = date.strftime('%Y')
    month = date.strftime('%m')
    day = date.strftime('%d')
    for coin in config['coins']:
        json_data = get_daily_summary(coin, int(year), int(month), int(day))
        upload_to_s3(
            bucket=config['bucket'],
            schema='cryptocurrency',
            table=coin,
            partition=date.strftime('%Y-%m-%d'),
            json_data=json_data
        )


if __name__ == '__main__':
    date = datetime.strptime(sys.argv[1], '%Y-%m-%d')

    with open('config.yml') as f:
        config = yaml.safe_load(f)

    extract_and_upload(date)
