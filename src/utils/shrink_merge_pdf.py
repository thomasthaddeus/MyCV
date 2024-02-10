"""shrink_merge_pdf.py

This script provides functionalities to merge multiple PDF files into a single
file and optionally shrink the merged file so that each page of the new PDF
contains 2 pages of the original side by side.

The script first merges all PDFs in a specified directory using the `merge_pdfs`
function and then, if required, shrinks the merged PDF using the `shrink_pdf`
function.

Returns:
    None: This script does not return a value but saves the merged and/or
    shrunk PDF files to specified locations.
"""

import os
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def merge_pdfs(directory, output_filename):
    """
    Merges all PDF files found in the specified directory into a single PDF
    file.

    Args:
        directory (str): Directory containing PDF files to be merged.
        output_filename (str): The filename for the merged output PDF.
    """
    pdf_writer = PdfWriter()

    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            pdf_reader = PdfReader(filepath)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    print(f'Merged PDFs into {output_filename}')
    return output_filename

def shrink_pdf(input_file, output_file):
    """
    Shrinks the provided PDF file so that each page of the new PDF contains 2
    pages of the original side by side.

    Args:
        input_file (str): The path to the input PDF file.
        output_file (str): The path to the output PDF file.
    """
    reader = PdfReader(input_file)
    output = PdfWriter()

    for i in range(0, len(reader.pages), 2):
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        page = reader.pages[i]
        page.scale_to(letter[0] / 2, letter[1])
        can.drawInlineImage(page, 0, 0, width=letter[0] / 2, height=letter[1])

        if i + 1 < len(reader.pages):
            page = reader.pages[i + 1]
            page.scale_to(letter[0] / 2, letter[1])
            can.drawInlineImage(page, letter[0] / 2, 0, width=letter[0] / 2, height=letter[1])

        can.save()

        packet.seek(0)
        new_pdf = PdfReader(packet)
        for page in new_pdf.pages:
            output.add_page(page)

    with open(output_file, 'wb') as out:
        output.write(out)

    print(f'Shrunk PDF saved as {output_file}')

def main():
    """
    The main function that executes the merging and optional shrinking of PDF
    files.

    It first calls `merge_pdfs` to merge all PDFs in a specified directory into
    a single file. Then it calls `shrink_pdf` to shrink the merged file so that
    each page of the new PDF contains 2 pages of the original side by side. The
    paths for input PDFs and output files are currently hard-coded and can be
    adjusted as needed.
    """
    # Usage example
    merged_file = merge_pdfs('E:/Resumes/my-cv/docs/Combo', 'merged.pdf')
    shrink_pdf(merged_file, 'shrunk_merged.pdf')

if __name__ == '__main__':
    main()
