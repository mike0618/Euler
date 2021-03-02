# import requests
#
# x = requests.get('http://localhost:3000')
#
# print(x.text)
elements = 'abcd'
def combs(els):
    if len(els) == 0:
        print('OK')
        return 'stop'
    print(els)
    combs(els[1:])

combs(elements)