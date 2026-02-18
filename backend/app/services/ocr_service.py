import pytesseract
from PIL import Image
from pdf2image import convert_from_path

from app.db.session import SessionLocal
from app.models.document import Document


def process_document(document_id: int):
    print("PROCESSING STARTED", document_id)

    db = SessionLocal()

    try:
        document = db.query(Document).filter(Document.id == document_id).first()

        if not document:
            print("DOCUMENT NOT FOUND")
            return

        document.status = "processing"
        db.commit()

        extracted_text = extract_text_from_file(document.file_path)

        document.raw_text = extracted_text
        document.status = "processed"
        db.commit()

        print("STATUS SET TO PROCESSED")

    except Exception as e:
        print("ERROR:", e)
        if document:
            document.status = "failed"
            db.commit()

    finally:
        db.close()


def extract_text_from_file(file_path: str) -> str:

    text_output = ""


    # If PDF → convert pages to images
    if file_path.lower().endswith(".pdf"):
        images = convert_from_path(file_path)
        for image in images:
            text_output += pytesseract.image_to_string(image)

    # If image → directly OCR
    else:
        image = Image.open(file_path)
        text_output = pytesseract.image_to_string(image)

    return text_output
