from translate import Translator

def perevod(my_str):
    my_str = str(my_str)
    rus_alf = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    def match_rus(text, alphabet=rus_alf):
        return not alphabet.isdisjoint(text.lower())

    if any(c.isalpha() for c in my_str) == False:
        return(eval(my_str))

    else:
        rus = 0
        for elem in my_str:
            if match_rus(elem) == True:
                rus += 1
        eng = len(my_str) - rus

        if rus >= eng:
            translator = Translator(to_lang='ru', from_lang= 'en')
            new_str = my_str.split()
            result = ''
            for el in new_str:
                translation = translator.translate(el)
                result = result + ' ' + translation
            return result[1:]

        elif rus < eng:
            translator = Translator(to_lang='en', from_lang= 'ru')
            new_str = my_str.split()
            result = ''
            for el in new_str:
                translation = translator.translate(el)
                result = result + ' ' + translation
                return result[1:]

print(perevod("hello friend"))