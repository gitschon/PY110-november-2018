import Tasks.post_adr_generator as pt


# my_str = '{"1": ["\u0420\u0424", "\u0421\u041f\u0411", "\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u0438\u044f"],'\
#          ' "2": ["\u0420\u0424", "\u0421\u041f\u0411",' \
#          ' "\u0416\u0443\u043a\u043e\u0432\u0441\u043a\u043e\u0433\u043e"],'\
#          ' "3": ["\u0420\u0424", "\u0421\u041f\u0411",' \
#          ' "\u041c\u0430\u044f\u043a\u043e\u0432\u0441\u043a\u043e\u0433\u043e"],'\
#          ' "4": ["\u0420\u0424", "\u0421\u041f\u0411", "\u0415\u0441\u0435\u043d\u0438\u043d\u0430"]}'
my_str = '''{
    "1": ["РФ", "СПБ", "Восстания"],
    "2": ["РФ", "СПБ", "Жуковского"],
    "3": ["РФ", "СПБ", "Маяковского"],
    "4": ["РФ", "СПБ", "Есенина"]
}'''

#my_str = ""

m = pt.adr_generator(j_string=my_str)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)

m = pt.adr_generator(j_file="..\\json_file.txt")
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
next(m)
