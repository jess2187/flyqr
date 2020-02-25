from config.celery import app
from pdfqr import PDF_QR

@app.task
def add_new_job(blank_pdf_url, out_url, list_of_urls, px, py, pwidth, pheight):
    qr = PDF_QR(blank_pdf_url, px, py, pwidth, pheight)
    qr.generatePDF(list_of_urls, out_url)