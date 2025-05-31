
# 📊 Cadastra Crypto Market Data ETL

Projeto Python para consumir dados da API pública da CoinCap (`v3`), armazenar as informações sobre criptomoedas e exchanges em um banco de dados PostgreSQL.

Utilizado o banco de dados da Render: [Render](https://render.com/)
Free: 256 MB RAM, 1 GB Storage, 30 dias de validade

Para visualização dos dados usamos o LookerStudio
[LookerStudio](https://lookerstudio.google.com/reporting/af63fcde-cec5-4a9d-8e8f-1032879b0f85)

---

## 🚀 Funcionalidades

✅ Conectar à API da CoinCap v3

✅ Coletar dados de criptomoedas (`/v3/assets`)  

✅ Coletar dados de exchanges (`/v3/exchanges`)  

✅ Armazenar dados em tabelas PostgreSQL  

✅ Configuração flexível via arquivo `.env` ou `config.env`  

✅ Código modular e limpo, seguindo boas práticas  

✅ Criação de dashboard via Looker

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- PostgreSQL
- `psycopg2-binary` para conexão com PostgreSQL
- `requests` para requisições HTTP
- `python-dotenv` para carregar configurações
- Looker Studio

---

## 📦 Estrutura do Projeto

```plaintext
├── api_client.py      # Comunicação com a API CoinCap
├── config.env         # Configurações sensíveis (não versionar!)
├── config.py          # Load das variaveis
├── database.py        # Conexão com o banco de dados
├── inserts.py         # Inserção de dados no banco
├── main.py            # Arquivo principal de execução
├── models.py          # Criação das tabelas no banco
├── requirements.txt   # Dependências
└── README.md          # Este documento
```

---

## ⚙️ Configuração

1. Clone este repositório:

```bash
git clone https://github.com/thiagogodeguesi/Cadastra.git
cd seu_repositorio
```

.
2. Crie um arquivo `config.env` na raiz com as seguintes variáveis:

```env
DB_NAME=cryptodb
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
COINCAP_API_KEY=sua_api_key
```

⚠️ **Importante:**  

- Não compartilhe sua API Key publicamente!  
- Garanta que o PostgreSQL esteja rodando e o banco `cryptodb` criado.

---

## 🐍 Instalação das dependências

Recomendo usar um ambiente virtual:  

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Instale as dependências:  

```bash
pip install -r requirements.txt
```

---

## ✅ Como executar

```bash
python main.py
```

O programa:  
✅ Cria as tabelas `cryptos` e `exchanges` (caso não existam).  
✅ Faz requisição à CoinCap API (v3).  
✅ Insere os dados no banco.

---

## 🗄️ Banco de Dados

Duas tabelas são criadas:

1. **cryptos** — informações de criptomoedas:  
   - `id`, `crypto_id`, `name`, `symbol`, `price_usd`

2. **exchanges** — informações de exchanges:  
   - `id`, `exchange_id`, `name`, `rank`, `percent_total_volume`

---

## 📄 Exemplo de saída

```plaintext
Dados inseridos com sucesso!
```

---

## ❓ Problemas comuns

- **Erro de conexão ao banco:**  
  - Verifique se o PostgreSQL está rodando.  
  - Confirme que as credenciais no `config.env` estão corretas.

- **Erro HTTP (401/403):**  
  - Verifique se sua API Key CoinCap é válida.

---

## ✅ Melhorias futuras

- Agendar execução automática (cron/scheduler).  
- Testes unitários.  

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir issues ou pull requests.

---

## ✉️ Contato

Desenvolvido por **[Thiago Godeguesi]**  

📧 Email: [thiagogodeguesi@gmail.com](mailto:thiagogodeguesi@gmail.com)  

🔗 LinkedIn: [seulinkedin](https://www.linkedin.com/in/thiagogodeguesi/)
