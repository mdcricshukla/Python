import base64
str='this is string example...wow!'
str=base64.b64encode(str.encode('utf-8'))
print(str)
str=base64.b64decode(str).decode('utf-8')
print(str)
                                
