try:
    soA = float(input())
    soB = int(input())
    print('{0:.{1}f}'.format(soA, soB))
except:
    print("Dinh dang dau vao khong hop le!")