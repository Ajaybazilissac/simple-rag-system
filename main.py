from pypdf  import PdfReader
from pathlib import Path
from docs import Document
from io import BytesIO


def load_txt(file_path):
    with open(file_path,"r",encoding="UTF-8") as file:
        text= file.read()
def load_pdf (file_byte, fileName):
   reader= PdfReader(file_path)
   documents=[]
     for page_number,page in enumerate(reader.pages,start=1):
        text=page.extract_text() or ""
        if text.strip():
            documents.append({
                "text":text,
                "metadata":{
                    "source":str(file_path),
                    "page":page_number
                }
            })
            return documents
            
            
        
def load_documents (directory):
    documents=[]
    directory=Path(directory)

    for file_path in directory.iterdir():
            if not file_path.is_file():
                continue
            extension=file_path.suffix.lower()
            
            if extension==".txt":
                documenst.extend(load_txt(file_path))
            if extension==".pdf":
                 documenst.extend(load_pdf(file_path))
        