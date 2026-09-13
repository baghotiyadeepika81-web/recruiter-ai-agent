from pypdf import PdfReader
import tempfile


def extract_text_from_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

    reader = PdfReader(temp_file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text