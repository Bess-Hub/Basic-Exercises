# Will attempt to perform a homework from Ely 

# Reto 11
## Escribe un programa que pida al usuario los siguientes datos por consola:
### Título de la película
### Director
### Año
### País
##E introduzca esos valores en una variable GLOBAL llamada "pelicula"

movie = {}

# Creat the possible inputs
print('Please inform the following information about the movie:')

title = str(input("Movie title: "))
director = str(input("Movie director: "))
year = int(input("Release year: "))
country = str(input("Country: "))
movie = {'Title': title, 'Director': director, 'Year': year, 'Country': country}

# Start by creating a variable called 'pelicula'
print()
print(movie)

# Success
