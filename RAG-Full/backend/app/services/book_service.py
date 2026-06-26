from pathlib import Path
from pypdf import PdfReader as pdfr


def extract_text(path:Path)-> str:
    if (path.exists()):
        if(path.is_file()):
                match path.suffix:
                    case ".pdf":
                        whole_text = extract_pdf(path)
                        return whole_text
                    case ".epub":
                          pass
        else:
            print("NOT A FILE")
                    
    else:
        print(f"FILE NOT FOUND")
        return "FILE NOT FOUND"
    
def extract_pdf(path:Path):
    reader = pdfr(str(path))

    extracted_pages = []
    for page in reader.pages:
         text = page.extract_text()
         if text is not None: 
            stripped_text = text.strip()
            if stripped_text:
                extracted_pages.append(stripped_text)
    return "\n\n".join(extracted_pages)