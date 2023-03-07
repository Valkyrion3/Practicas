import xml.etree.ElementTree as TE

def main():
    print("---XML---")
    data = '''
    <person>
        <name>Valkyrion</name>
        <phone type="intl">
            333999
        </phone>
        <email hide="yes"/>
    </person>
    '''
    tree = TE.fromstring(data)
    print("Name:",tree.find("name").text)
    print("Attr:",tree.find("email").get("hide"))
    print("---XML List---")
    input = '''
    <stuff>
        <users>
            <user x="3">
                <id>001</id>
                <name>Valkyrion</name>
            </user>
            <user x="7">
                <id>005</id>
                <name>Monse</name>
            </user>
        </users>
    </stuff>'''

    stuff = TE.fromstring(input)
    lst = stuff.findall('users/user')
    print('User count:', len(lst))

    for item in lst:
        print('Name', item.find('name').text)
        print('Id', item.find('id').text)
        print('Attribute', item.get('x'))

if __name__ == "__main__":
    main()