import os
from spire.pdf import *
from spire.pdf.common import *

def extract_xml_attachment_from_folder(folder_path, output_path):
    # Iterate through files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                try:
                    extract_xml_attachment(pdf_path, output_path)
                except Exception as e:
                    print(file, f":\t{e}")

def extract_xml_attachment(pdf_path, output_path):
    doc = PdfDocument()
    doc.LoadFromFile(pdf_path)
    collection = doc.Attachments

    if not collection.Count:
        print(f"No XML file found as an attachment in the PDF: {pdf_path}")
        return

    for i in range(collection.Count):
        attachment = collection.get_Item(i)
        fileName = attachment.FileName

        if not fileName.endswith('.xml'):
            continue

        data = attachment.Data

        data.Save(output_path + fileName)

        print(f"XML file '{fileName}' extracted successfully to '{output_path}'.")


# Specify the folder path
folder_path = '/home/prajwal/Downloads/'

# Specify the output path
output_path = '/home/prajwal/Downloads/output/'

# Call the function to extract XML attachment from the folder
extract_xml_attachment_from_folder(folder_path, output_path)
