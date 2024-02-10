import fitz  # PyMuPDF
from PIL import Image
import io

def optimize_pdf(input_path, output_path, quality=20):
    # Open the existing PDF
    doc = fitz.open(input_path)

    # Iterate through each page
    for page in doc:
        image_list = page.get_images(full=True)
        for _, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Compress the image using Pillow
            img = Image.open(io.BytesIO(image_bytes))
            img_io = io.BytesIO()
            img.save(img_io, format="JPEG", quality=quality)
            img_io.seek(0)

            # Replace the original image
            doc._replace_page_image(page.number, img_io, xref)

    # Save the optimized PDF
    doc.save(output_path, garbage=4, deflate=True)

# Example usage
optimize_pdf("docs/Combo/ThaddeusThomasCV.pdf", "ThomasThaddeusCV.pdf")
