from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('testing_translator.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('testing_translator-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError:
    print('check your file path silly!')




