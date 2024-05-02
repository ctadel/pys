import os
import pandas as pd
import xml.etree.ElementTree as Xet

SOURCE_DIR = '/home/prajwal/Downloads/output'
SHEET_NAME = 'Company listing'
OUTPUT_FILE = '/home/prajwal/Downloads/altryx.xlsx'

def extract_data_from_xml(xml_file):
    name = pan = None
    xmlparse = Xet.parse(xml_file)
    root = xmlparse.getroot()
    for elem in root.iter():
        if name and pan:
            break

        if elem.tag.endswith('NameOfCompany'):
            name = elem.text

        if elem.tag.endswith('PermanentAccountNumberOfEntity'):
            pan = elem.text

    return {
            'Name of Company' : name,
            'PAN' : pan
        }



dataframe = pd.DataFrame(columns=['Name of Company', 'PAN'])
for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                data = extract_data_from_xml(xml_file)
                dataframe.loc[len(dataframe)] = data

with open(OUTPUT_FILE, 'wb') as file:
    dataframe.to_excel(file, sheet_name=SHEET_NAME, index=False)

