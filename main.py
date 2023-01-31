import glob
import pandas as pd
from fpdf import FPDF


invoice_list = glob.glob("invoices/*xlsx*")

for invoice in invoice_list:
    df = pd.read_excel(invoice, sheet_name="Sheet 1")
    print(df)

