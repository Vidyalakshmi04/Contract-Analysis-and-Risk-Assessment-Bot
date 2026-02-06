import streamlit as st


from extractor import extract_text
from clause_splitter import split_clauses
from risk_detector import detect_risks
from llm_helper import explain_clause
from analysis_utils import detect_contract_type, classify_clause_type, is_ambiguous
from ner_utils import extract_entities
from pdf_report import generate_pdf

st.set_page_config(page_title="Legal Assistant", layout="wide")
st.title("⚖️ Contract Analysis and Risk Assessment Bot")
st.markdown("""

An AI-powered legal assistant designed to help small businesses and individuals quickly understand contracts, identify risky clauses, and make informed decisions.

---
###  What You Can Do Here

- 📄 Upload contracts (PDF / DOCX / TXT)
- ⚠️ Detect risky and ambiguous clauses
- 🧩 Classify clause types (Termination, Payment, NDA, etc.)
- 🧠 Get simple AI explanations
- 📊 View risk distribution (Bar)
- 📑 Export a professional PDF report

---""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("⚡ Instant Risk Detection")

with col2:
    st.success("🧠 AI-Powered Explanations")

with col3:
    st.warning("📄 Downloadable Legal Report")

uploaded_file = st.file_uploader("Upload Contract (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"])



if uploaded_file:
    text = extract_text(uploaded_file)
    clauses = split_clauses(text)

    contract_type = detect_contract_type(text)
    st.info(f"📑 Detected Contract Type: {contract_type}")

    # ❌ Removed Extracted Key Entities UI (kept backend if needed)
    entities = extract_entities(text)

    total_score = 0
    risky_clauses_for_pdf = []

    # For charts
    risk_counts = {"Low": 0, "Medium": 0, "High": 0}

    clause_results = []

    for i, clause in enumerate(clauses):
        risk = detect_risks(clause)
        total_score += risk["score"]

        risk_level = risk["level"]
        risk_counts[risk_level] += 1

        clause_type = classify_clause_type(clause)
        ambiguous = is_ambiguous(clause)

        explanation = None
        if risk["score"] > 0:
            explanation = explain_clause(clause)
            risky_clauses_for_pdf.append(
                f"Clause {i+1}: {clause}\nExplanation: {explanation}"
            )

        clause_results.append({
            "index": i,
            "clause": clause,
            "risk_level": risk_level,
            "clause_type": clause_type,
            "ambiguous": ambiguous,
            "explanation": explanation
        })

  
# =========================
# 📊 Risk Charts (Streamlit Native - BEFORE explanations)
# =========================
    st.subheader("📊 Risk Analysis Overview")

    risk_df = {
    "Risk Level": ["Low", "Medium", "High"],
    "Count": [risk_counts["Low"], risk_counts["Medium"], risk_counts["High"]]
}

    st.bar_chart(
    data={"Low": [risk_counts["Low"]], "Medium": [risk_counts["Medium"]], "High": [risk_counts["High"]]},
    use_container_width=True
)

    st.caption(
    "🟦 The bar chart shows how contract clauses are distributed across risk levels. "
    "A higher bar indicates more clauses falling under that risk category. "
    "This helps quickly identify whether the contract is dominated by low, medium, or high-risk terms."
)

    
  

    # =========================
    # Clause-by-Clause Explanation (After charts)
    # =========================
    st.subheader("📘 Clause-by-Clause Explanation")

    for item in clause_results:
        header = f"Clause {item['index']+1} | Risk: {item['risk_level']} | Type: {item['clause_type']}"
        if item["ambiguous"]:
            header += " | ⚠️ Ambiguous"

        with st.expander(header):
            st.write(item["clause"])

            if item["ambiguous"]:
                st.info("This clause contains vague words and may be open to interpretation.")

            if item["explanation"]:
                st.warning("⚠️ Risky clause detected")
                st.write("🧠 Simple explanation:")
                st.write(item["explanation"])

    # =========================
    # Overall Risk Meter
    # =========================
    final_risk = "Low" if total_score < 3 else "Medium" if total_score < 6 else "High"
    st.success(f"📊 Overall Contract Risk: {final_risk}")

    st.subheader("📊 Overall Risk Meter")
    risk_value = 30 if final_risk == "Low" else 60 if final_risk == "Medium" else 90
    st.progress(risk_value)

    if final_risk == "Low":
        st.success("🟢 Low Risk Contract")
    elif final_risk == "Medium":
        st.warning("🟠 Medium Risk Contract")
    else:
        st.error("🔴 High Risk Contract")

    # =========================
    # 📄 PDF Export (with Summary + Findings)
    # =========================
    overall_summary = (
        f"This contract is classified as a {contract_type}. "
        f"It contains {risk_counts['High']} high-risk clauses and "
        f"{risk_counts['Medium']} medium-risk clauses. "
        f"Certain terms may expose SMEs to legal and financial risks."
    )

    if st.button("📄 Export PDF Report"):
        pdf_path = generate_pdf(
            contract_type=contract_type,
            final_risk=final_risk,
            summary=overall_summary,
            risky_clauses=risky_clauses_for_pdf
        )
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name="contract_risk_report.pdf")


