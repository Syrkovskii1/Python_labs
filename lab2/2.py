import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r', encoding='windows-1251')
xml_data = xml_file.read()


dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currency_names = []

for node in elements:
    nominal = 0
    name = ''
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3:
                    nominal = int(child.firstChild.data)

            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data

   
    if nominal == 1:
        currency_names.append(name)

xml_file.close()


print("Список валют с Nominal = 1:")
print(currency_names)