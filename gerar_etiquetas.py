import pg8000
import qrcode
from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

# 🔹 Configuração da conexão com Supabase
PG_CONN = {
    "host": "db.vkrvgjdpamcadthhkdxj.supabase.co",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "Tractian@437"
}

# Criar pasta para salvar etiquetas
OUTPUT_DIR = "etiquetas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    # Conectar ao banco de dados
    conn = pg8000.connect(**PG_CONN)
    cur = conn.cursor()

    # Buscar os dados para etiquetas
    cur.execute("""
        SELECT item_code, batch_id, label_id, status, creation_date, batch_qty, expiry_date, iwo, qdr
        FROM inventory_labels;
    """)
    labels = cur.fetchall()

    for label in labels:
        item_code, batch_id, label_id, status, creation_date, batch_qty, expiry_date, iwo, qdr = label

        # Gerar QR Code
        qr = qrcode.make(label_id)
        qr_path = os.path.join(OUTPUT_DIR, f"{label_id}.png")
        qr.save(qr_path)

        # Criar PDF para etiqueta
        pdf_path = os.path.join(OUTPUT_DIR, f"{label_id}.pdf")
        c = canvas.Canvas(pdf_path, pagesize=(80*mm, 50*mm))

        # Adicionar texto no formato correto
        c.setFont("Helvetica-Bold", 12)
        c.drawString(10, 120, f"{item_code}")
        c.drawString(10, 105, f"{batch_id}")

        c.setFont("Helvetica", 10)
        c.drawString(10, 90, f"Label ID: {label_id}")
        c.drawString(10, 75, f"Status: {status}")
        c.drawString(10, 60, f"Creation Date: {creation_date}")
        c.drawString(10, 45, f"Batch Qty: {batch_qty}")
        c.drawString(10, 30, f"Expiry Date: {expiry_date if expiry_date else 'N/A'}")
        c.drawString(10, 15, f"IWO: {iwo}  QDR: {qdr}")

        # Adicionar QR Code na etiqueta
        c.drawImage(ImageReader(qr_path), 150, 30, width=50, height=50)

        c.save()
        print(f"Etiqueta gerada: {pdf_path}")

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Erro ao gerar etiquetas:", e)
