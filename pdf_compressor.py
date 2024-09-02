import pypdf as pdf


def pdf_compressor(pdf_file):
    writer = pdf.PdfWriter(clone_from=pdf_file)

    for page in writer.pages:
        page.compress_content_streams()
    
    with open(pdf_file,"wb") as file:
        writer.write(file)
    print("file compressed successfuly")
        
if __name__ == "__main__":
    file = input("enter the path (c:/a/b.pdf) or name (a.pdf)  ")
    pdf_compressor(file)