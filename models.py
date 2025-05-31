from database import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS cryptocurrencies (
            id VARCHAR PRIMARY KEY,
            name VARCHAR,
            symbol VARCHAR,
            rank INTEGER,
            supply FLOAT,
            max_supply FLOAT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS market_data (
            id SERIAL PRIMARY KEY,
            crypto_id VARCHAR REFERENCES cryptocurrencies(id),
            price_usd FLOAT,
            market_cap_usd FLOAT,
            volume_usd_24hr FLOAT,
            change_percent_24hr FLOAT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS exchanges (
            id SERIAL PRIMARY KEY,
            exchange_id VARCHAR(50),
            name VARCHAR(100),
            rank INTEGER,
            percent_total_volume NUMERIC
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()