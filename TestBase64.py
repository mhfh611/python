import base64
def safe_base64_decodes(s):
    testMul = len(s)%4
    while(testMul != 0):
        s = s + b'='
        testMul = len(s)%4

    return base64.b64decode(s)

#test
assert b'abcd' == safe_base64_decodes(b'YWJjZA=='), safe_base64_decodes('YWJjZA==')
assert b'abcd' == safe_base64_decodes(b'YWJjZA'), safe_base64_decodes('YWJjZA')

print('Pass')
