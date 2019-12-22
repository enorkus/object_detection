import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(xml_file)
        for member in root.findall('object'):
            boundBox = member.findall('bndbox')
            xmin = boundBox[0][0].text
            ymin = boundBox[0][1].text
            xmax = boundBox[0][2].text
            ymax = boundBox[0][3].text
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     float(xmin),
                     float(ymin),
                     float(xmax),
                     float(ymax)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for folder in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), folder)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv((folder+'_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()
