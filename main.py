import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

invoice_list = glob.glob("invoices/*xlsx*")


for invoice in invoice_list:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    invoice_name = Path(invoice).stem
    invoice_num, invoice_date = invoice_name.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_num}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)

    df = pd.read_excel(invoice, sheet_name="Sheet 1")

    # Add col headers
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", style="B", size=10)
    # pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(columns[0]), border=1)
    pdf.cell(w=70, h=8, txt=str(columns[1]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[4]), border=1, ln=1)

    # Add rows to table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Add total sum to bottom of table
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum as a sentence to bottom of PDF
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is: {total_sum}", ln=1)

    # Add company name and logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=25, h=8, txt=f"RyanCorp")
    pdf.image("logo.jpg", w=10)

    pdf.output(f"PDFs/{invoice_name}.pdf")


