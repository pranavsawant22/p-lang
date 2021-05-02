import colorama
import basic

colorama.init()
text = ''
while text != 'exit':
    print(colorama.Fore.YELLOW, "", end='')
    text = input("basic > ")
    if text != 'exit':
        result, error = basic.run('<stdin>', text)
        if error is not None:
            print(colorama.Fore.RED, error.as_string())
        else:
            print(colorama.Fore.YELLOW, result)
    else:
        break
