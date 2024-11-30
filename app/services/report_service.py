
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def export_csv():
    # Example data
    scan_results = [{"host": "192.168.1.1", "status": "up", "port": 80, "state": "open"}]

    file_path = "reports/scan_results.csv"
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["host", "status", "port", "state"])
        writer.writeheader()
        writer.writerows(scan_results)

    return file_path

def export_pdf():
    results = [{"host": "192.168.1.1", "status": "up"}]
    file_path = "reports/scan_results.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(50, 750, "Penetration Testing Report")
    c.drawString(50, 730, f"Generated: {datetime.now()}")

    y = 700
    for result in results:
        c.drawString(50, y, f"Host: {result['host']}, Status: {result['status']}")
        y -= 20

    c.save()
    return file_path
