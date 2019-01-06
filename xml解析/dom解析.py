from xml.dom.minidom import parse


DOMTree = parse('movies')
root = DOMTree.documentElement
if root.hasAttribute('shelf'):
    print('Root element:{}'.format(root.getAttribute('shelf')))
movies = root.getElementsByTagName('movie')
for movie in movies:
    print("****movies****")
    if movie.hasAttribute('title'):
        print('Title:', movie.getAttribute('title'))
    type = movie.getElementsByTagName('type')[0]
    print('Type:', type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print('Format:', format.firstChild.data)
    years = movie.getElementsByTagName('year')
    if years:
        print('Year:', years[0].firstChild.data)