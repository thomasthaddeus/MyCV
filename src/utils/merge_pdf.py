"""
_summary_

_extended_summary_
"""

import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(directory, output_filename):
    """
    merge_pdfs _summary_

    _extended_summary_

    Args:
        directory (_type_): _description_
        output_filename (_type_): _description_
    """
    pdf_writer = PdfWriter()

    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            pdf_reader = PdfReader(filepath)

            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print(f'Merged PDFs into {output_filename}')

# Usage example
DIR = 'E:/Resumes/my-cv/docs/Combo'
FOUT = 'docs/combo/Combo.pdf'
merge_pdfs(DIR, FOUT)
