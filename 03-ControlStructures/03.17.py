x = float(input("Podaj koordynaty liczby x: "))
y = float(input("Podaj koordynaty liczby y: "))

if x>0 and y>0:
    print("Punkt x,y=[{},{}] leży w pierwszej części układu współrzędny".format(x,y))
elif x<0 and y>0:
    print("Punkt x,y=[{},{}] leży w drugiej części układu współrzędny".format(x,y))
elif x<0 and y<0:
    print("Punkt x,y=[{},{}] leży w trzeciej części układu współrzędny".format(x,y))
elif x>0 and y<0:
    print("Punkt x,y=[{},{}] leży w czwartej części układu współrzędny".format(x,y))
else:
    print("Współrzędne leżą w punkcie (0,0)")