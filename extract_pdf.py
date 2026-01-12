import sys

try:
    import pypdf
except ImportError:
    try:
        import PyPDF2 as pypdf
    except ImportError:
        print("No PDF library found (pypdf or PyPDF2).")
        sys.exit(1)

pdf_path = "Horizontal Tabs V1.0.0 Docs.pdf"
output_path = "pdf_content_utf8.txt"

try:
    reader = pypdf.PdfReader(pdf_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Number of pages: {len(reader.pages)}\n")
        for i, page in enumerate(reader.pages):
            f.write(f"--- Page {i + 1} ---\n")
            f.write(page.extract_text())
            f.write("\n")
    print(f"Written to {output_path}")
except Exception as e:
    print(f"Error reading PDF: {e}")
