from fpdf import FPDF
def sanitize_text(text):
    if not text:
        return ""
    return text.encode("latin-1", "ignore").decode("latin-1")


def generate_pdf(contract_type, final_risk, summary, risky_clauses):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, sanitize_text("Contract Risk Report"), ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, sanitize_text(f"Contract Type: {contract_type}"), ln=True)
    pdf.cell(0, 10, sanitize_text(f"Overall Risk Level: {final_risk}"), ln=True)

    pdf.ln(6)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, sanitize_text("Overall Summary:"), ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 8, sanitize_text(summary))

    pdf.ln(4)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, sanitize_text("Risk-Based Findings (High Risk Clauses):"), ln=True)
    pdf.set_font("Arial", size=10)

    if not risky_clauses:
        pdf.multi_cell(0, 8, sanitize_text("No high-risk clauses were detected."))
    else:
        for idx, clause_info in enumerate(risky_clauses, 1):
            pdf.multi_cell(0, 8, sanitize_text(f"{idx}. {clause_info}"))
            pdf.ln(1)

    file_path = "contract_risk_report.pdf"
    pdf.output(file_path)
    return file_path


