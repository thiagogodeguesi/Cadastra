from database import get_connection

def insert_cryptos(cryptos):
    conn = get_connection()
    cur = conn.cursor()

    for crypto in cryptos:
        cur.execute('''
            INSERT INTO cryptocurrencies (id, name, symbol, rank, supply, max_supply)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE
            SET name = EXCLUDED.name,
                symbol = EXCLUDED.symbol,
                rank = EXCLUDED.rank,
                supply = EXCLUDED.supply,
                max_supply = EXCLUDED.max_supply;
        ''', (crypto['id'], crypto['name'], crypto['symbol'], int(crypto['rank']),
              float(crypto['supply']) if crypto['supply'] else None,
              float(crypto['maxSupply']) if crypto['maxSupply'] else None))

        cur.execute('''
            INSERT INTO market_data (crypto_id, price_usd, market_cap_usd, volume_usd_24hr, change_percent_24hr)
            VALUES (%s, %s, %s, %s, %s)
        ''', (crypto['id'], float(crypto['priceUsd']), float(crypto['marketCapUsd']),
              float(crypto['volumeUsd24Hr']), float(crypto['changePercent24Hr'])))

    conn.commit()
    cur.close()
    conn.close()

def insert_exchanges(exchanges):
    conn = get_connection()
    cur = conn.cursor()

    for exchange in exchanges:
        cur.execute('''
            INSERT INTO exchanges (exchange_id, name, rank, percent_total_volume)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        ''', (
            exchange['exchangeId'],
            exchange['name'],
            int(exchange['rank']) if exchange['rank'] else None,
            float(exchange['percentTotalVolume']) if exchange['percentTotalVolume'] else None
        ))

    conn.commit()
    cur.close()
    conn.close()