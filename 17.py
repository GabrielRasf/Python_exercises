catA = float(input('Cateto adj: '))
catO = float(input('Cateto opo: '))
hip = float(catA ** 2 + catO ** 2) ** 0.5

seno = (catO / hip)
cos = (catA / hip)
tan = (catO / catA)

print('Seno: {:.2f}'.format(seno))
print('Coseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))