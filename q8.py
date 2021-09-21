import codecs

try:
    fl1 = codecs.open('test_f.txt','r','utf-8')
    fl2 = codecs.open('test_rev.txt','w')
    text = fl1.read()
    fl2.write(text[::-1])
finally:
    fl1.close()
    fl2.close()

try:
    fl1 = codecs.open('test_f.txt', 'r','utf-8')
    fl2 = codecs.open('test_rev.txt', 'r')
    print(fl1.read())
    print(fl2.read())
finally:
    fl1.close()
    fl2.close()


