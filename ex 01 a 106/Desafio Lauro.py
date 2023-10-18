s = str(input('palavra 1: ')).strip().lower()
t = str(input('palavra 2: ')).strip().lower()

if len(s) != len(t):
    print('não é')
else:
    list_s= []
    list_t=[]
    for letter in s:
        list_s += letter
        sorted_s = sorted(list_s)
    for letter in t:
        list_t += letter
        sorted_t = sorted(list_t)
    if sorted_s == sorted_t:
        print('é anagrama')
    else:
        print('não é anagrama')
    