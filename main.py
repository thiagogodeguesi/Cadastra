from models import create_tables
from api_client import fetch_cryptos, fetch_exchanges
from inserts import insert_cryptos, insert_exchanges


def main():
    create_tables()

    cryptos = fetch_cryptos()
    insert_cryptos(cryptos)
    
    exchanges = fetch_exchanges()
    insert_exchanges(exchanges)
    
    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    main()