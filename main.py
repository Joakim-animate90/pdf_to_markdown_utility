import os
from image_splitter import pdf_to_images
from image_to_markdowns import process_images_to_markdown


def main():
    # Convert PDF to images
    pdf_path = "convert-to-markdown.pdf"
    pdf_to_images(pdf_path)
    print("PDF conversion to images completed.")

    # Convert images to markdown
    process_images_to_markdown()
    print("All images converted to markdown.")


if __name__ == "__main__":
    main()
