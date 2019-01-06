from xml.dom import minidom

dom = minidom.Document()
root = dom.createElement('root')
dom.appendChild(root)
book = dom.createElement('book')
book.setAttribute('price', '199')
root.appendChild(book)
name = dom.createElement('name')
name_text = dom.createTextNode("python学习")
name.appendChild(name_text)
book.appendChild(name)

try:
    with open('book.xml', 'w', encoding='utf-8') as f:

        dom.writexml(f, indent='', addindent='\t', newl='\n', encoding='utf-8')
        print('写入xml完成')
except Exception as e:
    print(e)