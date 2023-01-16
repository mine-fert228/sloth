def calc():
    print(eval(input("ведите пример: ")))
def echo(text):
    print(text)
def start(path_to_file):
    import os
    uir = path_to_file.replace('\\', '/')
    os.startfile(uir)
def cmd(command):
    import os
    os.system(command)
def browser(url):
    import webbrowser
    webbrowser.open_new_tab(url)
def editfile():
    print("пример prim.txt(если нету этого файла то он создатся)")
    my_cr = input("имя файла: ")
    my_file = open(my_cr, "a+" )
    uyt = input('ведите текст в файле: ')
    my_file.write(uyt +'\n')
    my_file.close()
def file(name,textinfile):
    my_file = open(name, "a+" )
    my_file.write(textinfile +'\n')
    my_file.close()

def help():
    print("calc - калькулятор")
    print("echo - вывод текста в консоль")
    print("start - запуск файла")
    print("cmd - выполнение команды от cmd windows")
    print("browser - браузер")
    print("editfile - редактор файла для юзера")
    print("file - редактор файла для кода")