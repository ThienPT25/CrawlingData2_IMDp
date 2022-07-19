#Nhap so A tu ban phim va chuyen sang kieu so thuc
soA = float(input())

#Nhap so B tu ban phim va chuyen sang kieu so nguyen
soB = int(input())

#Dung ham format de dinh dang chuoi dau ra
print('{0:.{1}f}'.format(soA, soB))