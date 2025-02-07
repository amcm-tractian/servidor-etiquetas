import psycopg2

# Connection String ajustada com sua senha correta
PG_CONN = "postgresql://postgres:Tractian%40437@db.vkrvgjdpamcadthhkdxj.supabase.co:5432/postgres"

try:
    # Tentar conectar ao banco
    conn = psycopg2.connect(PG_CONN)
    print("✅ Conexão bem-sucedida ao Supabase!")

    # Fechar conexão
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
