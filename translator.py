from translate import Translator
try:
    f = open("RDMTextFile.txt", "r")
    translator = Translator(to_lang="ja")
    print(translator.translate(f.read()))
except FileNotFoundError as e:
    print("File Not Found")
