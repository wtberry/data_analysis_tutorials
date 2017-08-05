import xml.etree.ElementTree as ET

with open('catalog.xml', 'rb') as data:
    xmlParsed = ET.parse(data)

    increase_v = float(input('input a increase value'))
    for elem in xmlParsed.iter('price'):
        price = float(elem.text)
        new_price = round((price*increase_v), 2)
        print(new_price)
        elem.text = str(new_price)

    xmlParsed.write('output3.xml')
