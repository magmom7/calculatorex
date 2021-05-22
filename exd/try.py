try:
    fruit = {'apple': 5, 'grape': 2, 'pi': 3, 'mango': 4}
    sorted1 = sorted(fruit.itmes(), key=lambda x: x[0])
    print(sorted1)
except:
    print(fruit)
