import pg8000

# 🔹 Substitua "SUA_SENHA" pela senha correta do Supabase
PG_CONN = {
    "host": "db.vkrvgjdpamcadthhkdxj.supabase.co",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "Tractian@437"
}

try:
    # Conectar ao Supabase usando pg8000
    conn = pg8000.connect(**PG_CONN)
    print("✅ Conexão bem-sucedida ao Supabase!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
