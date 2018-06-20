import requests
import logging
from mysql import DB
from decimal import Decimal

db = DB(host="192.168.0.149", port=8005, user="tom", password="tom123", database="coin")

url = 'http://api.f2pool.com/eth/0x7999895ddc1b69750739f61e96983c36f2e4966b'

def parse_one(data=None):
    if not data:
        return

    d = data[0][:10]
    txid = data[1]
    amount = Decimal(data[2])
    if db.select(r'''SELECT COUNT(-1) FROM eth_profit WHERE `date`="{}"'''.format(d))[0][0]:
        print(d)
        return

    return db.execute(r'''INSERT INTO eth_profit (`date`, txid, amount) VALUES ("{}", "{}", {})'''.format(d, txid, amount))

def get_all():
    r = requests.get(url)
    result = r.json()
    return result["payout_history"]

def main():
    db.connect()
    data = get_all()[-1]
    parse_one(data)
    db.close()

if __name__ == '__main__':
    main()

