from pdf2docx import Converter
from docx2pdf import convert


def pdf_converter(file):
    try:
        pdf_file = file
        docx_file = "sample.docx"

        cv = Converter(pdf_file)
        cv.convert(docx_file)

        cv.close()
        print(f"{file} has been converted to the word file successfully")
    except :
        print("something went wrong, please try again")
        
        
def docx_converter(pdf_file):
    try:
        convert(pdf_file,"converted.pdf")
        print(f"{pdf_file} has been converter to the converted.pdf")
    except:
        print("something went wrong, please try again")
        
        
if __name__ == "__main__":
    file = input("enter the name of the file")
    if ".docx" in file:
        docx_converter(file)
        
    elif ".pdf" in file:
        pdf_converter(file)
    else:
        print("please enter valid file format")