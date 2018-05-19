import xlwings as xw


def summarize_sales():
    """
    ecrire Hello world dans une case excel
    """
    wb = xw.Book.caller()
    nom = xw.Range('B14').value
    wb.sheets[0].range('B16').value = 'Salut '+str(nom)

@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)


def somme_e():
    wb = xw.Book.caller() 
    a = xw.Range('B4').value
    b = xw.Range('B5').value
    wb.sheets[0].range('B6').value = a + b