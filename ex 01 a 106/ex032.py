from datetime import date

ano = int(input('Digite um ano para analizar. Caso queira analisar o ano atual digite 0 '))
if ano == 0:
    ano = date.today().year

if ano % 4 != 0:
    print('O ano de {} não é bissexto'.format(ano))
else:
    if ano % 100 != 0:
        print('O ano de {} é bissexto'.format(ano))
    else:
        if ano % 400 != 0:
            print('O ano de {} não é bissexto'.format(ano))
        else:
            print('O ano de {} é bissexto'.format(ano))
