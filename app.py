import streamlit as st
from pdf_parser import extract_tables_from_pdf
from arxml_builder import generate_arxml

st.title("📄 PDF to ARXML Generator")

pdf_file = st.file_uploader("Upload Peripheral PDF", type=["pdf"])

if pdf_file:
    try:
        st.info("Extracting registers...")
        extracted_data = extract_tables_from_pdf(pdf_file)

        if not extracted_data:
            st.warning("No valid register tables found.")
        else:
            names = [item["name"] for item in extracted_data]
            selected = st.multiselect("Select Registers to include in ARXML:", names, default=names)

            if st.button("Generate ARXML"):
                arxml_bytes = generate_arxml(extracted_data, selected)
                st.success("ARXML generated!")

                st.download_button(
                    label="📥 Download ARXML",
                    data=arxml_bytes,
                    file_name="generated.arxml",
                    mime="application/xml"
                )
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
