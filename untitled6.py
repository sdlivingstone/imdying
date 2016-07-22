'''
import qrcode
img = qrcode.make("MARICARMEN IS A STAR")
img.show()
img.save('whatintheworld.png')
'''


import base64

encoded = base64.b64encode(b'print(encoded)49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

print(encoded)