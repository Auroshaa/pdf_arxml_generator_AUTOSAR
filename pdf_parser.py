import pdfplumber

def extract_tables_from_pdf(pdf_file):
    results = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and len(row) >= 2 and row[0] and row[1]:
                        results.append({
                            "name": row[0].strip(),
                            "address": row[1].strip(),
                            "description": row[2].strip() if len(row) > 2 and row[2] else ""
                        })
    return results
