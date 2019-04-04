# -*- coding: cp1252 -*-
import fresh_tomatoes
import media

# Instanciando os objetos Movie
dr_strangelove = media.Movie("Dr Strangelove",
                             "https://upload.wikimedia.org/wikipedia/pt/thumb/7/73/Dr._Strangelove.jpg/200px-Dr._Strangelove.jpg",
                             "https://youtu.be/IE9CmX15PYA?list=PL4E1017C886D1A1F2")

space_odyssey = media.Movie("2001: A Space Odyssey",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/2001_A_Space_Odyssey_%281968%29.png/220px-2001_A_Space_Odyssey_%281968%29.png",
                        "https://youtu.be/Qv4Jv15OSGI?list=PL4E1017C886D1A1F2")

laranja_mecanica = media.Movie("Clockwork Orange",
                        "https://www.movieposter.com/posters/archive/main/19/A70-9892",
                        "https://youtu.be/eRerbaI9axY")

barry_lyndon = media.Movie("Barry Lyndon",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/e/ee/Barry_Lyndon_A.jpg/220px-Barry_Lyndon_A.jpg",
                     "https://youtu.be/9lzSoKOs1fc?list=PL4E1017C886D1A1F2")

iluminado = media.Movie("O Iluminado",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/ea/The_Shining_%281980%29.png/220px-The_Shining_%281980%29.png",
                        "https://youtu.be/S014oGZiSdI?list=PL4E1017C886D1A1F2")

full_metal_jacket = media.Movie("Full Metal Jacket",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Full_Metal_Jacket_poster.jpg/220px-Full_Metal_Jacket_poster.jpg",
                          "https://youtu.be/3Un-WBlVHPw?list=PL4E1017C886D1A1F2")

# lista dos meus filmes preferidos de Stanley Kubrick
movies = [dr_strangelove, space_odyssey, laranja_mecanica, barry_lyndon, iluminado, full_metal_jacket]

# criação da página web através da fresh_tomatoes 
fresh_tomatoes.open_movies_page(movies)
