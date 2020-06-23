# create the planets.txt
planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n',
           'Saturn\n', 'Uranus\n', 'Neptune\n']
fout = open('planets.txt', 'w', encoding='utf-8')
fout.writelines(planets)
fout.close()
