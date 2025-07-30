# PDF to ARXML Converter

## 📄 Overview

The **PDF to ARXML Converter** is a tool that parses structured content from a PDF document (such as CAN signal definitions, ECU configurations, or diagnostics specifications) and converts the extracted data into AUTOSAR-compliant `.arxml` (AUTOSAR XML) files.

This utility is useful for automotive developers, embedded engineers, and AUTOSAR toolchain users who need to convert OEM documentation into machine-readable ARXML format for use in their AUTOSAR stack or MCAL configuration.

---

## 🚀 Features

- Extract structured data (tables, text blocks) from PDF
- Convert signal/message definitions to `Com` or `Pdu` ARXML format
- Generate AUTOSAR XML for:
  - ECU extract
  - PDU and signal definitions
  - Diagnostics (if DIDs/UDS services are provided)
- Validate ARXML syntax (optional)
- Command-line interface (CLI)

---

## 🛠️ Prerequisites

- Python 3.8+
- pip
- Recommended: Use a virtual environment

---

## 📦 Installation

```bash
git clone https://github.com/Auroshaa/pdf_arxml_generator_AUTOSAR.git
cd pdf_arxml_generator_AUTOSAR
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pip install streamlit lxml pdfplumber
streamlit run app.py
```

<img width="1011" height="217" alt="image" src="https://github.com/user-attachments/assets/bed5fe51-04f5-4702-9d89-6c3d1716e3c5" />
<img width="889" height="240" alt="image" src="https://github.com/user-attachments/assets/dc81ec79-998a-4afb-803c-ea81f9606bef" />
<img width="927" height="721" alt="image" src="https://github.com/user-attachments/assets/eab1326c-1fb6-48ae-856a-e120d60f2abd" />

## Let me know:
- What exact data your PDF contains (signals? DIDs? ECU structure?)
- What AUTOSAR version you're targeting (4.2.2, 4.3.0, etc.)
- Whether this is a Python project or another language

So I can tailor it even better.

