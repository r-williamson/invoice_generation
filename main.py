import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

invoice_list = glob.glob("invoices/*xlsx*")


for invoice in invoice_list:
    df = pd.read_excel(invoice, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    invoice_name = Path(invoice).stem
    invoice_num, invoice_date = invoice_name.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_num}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}")

    pdf.output(f"PDFs/{invoice_name}.pdf")


