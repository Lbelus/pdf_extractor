from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Delivery Order", ln=True)
pdf.cell(200, 10, txt="Item A: 10.00 EUR", ln=True)
pdf.cell(200, 10, txt="Item B: 25.00 EUR", ln=True)
pdf.cell(200, 10, txt="Total: 35.00 EUR", ln=True)
pdf.output("docs/dummy_delivery.pdf")
