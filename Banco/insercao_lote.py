import banco

lista = [
  ["ET", "Steven Spielberg", "01-05-1986", 9, 120, 'Extraterrestre chega á Terra', "livre", "drama"],
  ["O Senhor dos Anéis", "Peter Jackson", "19-12-2001", 10, 178, 'A jornada para destruir o Um Anel', "12+", "fantasia"],
  ["Matrix", "Lana Wachowski", "31-03-1999", 10, 136, 'A luta contra a realidade simulada', "16+", "ficção científica"],
  ["A Origem", "Christopher Nolan", "16-07-2010", 9, 148, 'Exploração dos sonhos e da mente humana', "12+", "ficção científica"],
  ["Avatar", "James Cameron", "18-12-2009", 8, 162, 'Uma nova aventura no planeta Pandora', "12+", "ficção científica"]
]



for registro in lista:
    movie = {}
    movie['titulo'] = registro[0]
    movie['diretor'] = registro[1]
    movie['data_lancamento'] = registro[2]
    movie['avaliacao'] = registro[3]
    movie['duracao'] = registro[4]
    movie['sinopse'] = registro[5]
    movie['classificacao'] = registro[6]
    movie['genero'] = registro[6]
    
    banco.insere_filme(movie)
