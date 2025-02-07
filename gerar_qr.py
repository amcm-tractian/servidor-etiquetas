import psycopg2  # Conectar ao PostgreSQL
import qrcode  # Gerar QR Codes
import os  # Criar pastas no sistema

# Configuração da conexão com o banco PostgreSQL
PG_CONN = "postgresql://postgres:Tractian%40437@db.vkrvgjdpamcadthhkdxj.supabase.co:5432/postgres"


# Criar a pasta onde os QR Codes serão salvos
OUTPUT_DIR = "qrcodes"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Cria a pasta se não existir

try:
    # Conectar ao PostgreSQL
    conn = psycopg2.connect(PG_CONN)
    cur = conn.cursor()

    # Buscar os IDs das etiquetas
    cur.execute("SELECT label_id FROM inventory_labels;")
    labels = cur.fetchall()

    # Gerar QR Code para cada etiqueta
    for label in labels:
        label_id = label[0]  # Pegando o ID da etiqueta
        
        # Criar QR Code contendo apenas o label_id
        qr = qrcode.make(label_id)
        
        # Definir o nome do arquivo
        qr_path = os.path.join(OUTPUT_DIR, f"{label_id}.png")
        
        # Salvar o QR Code como imagem PNG
        qr.save(qr_path)
        
        print(f"QR Code gerado: {qr_path}")

    # Fechar conexão com o banco
    cur.close()
    conn.close()

    print("Todos os QR Codes foram gerados com sucesso!")

except Exception as e:
    print("Erro ao gerar os QR Codes:", e)
