import colorama
import basic

colorama.init()
while (1):
    print(colorama.Fore.YELLOW, "", end='')
    text = input("basic > ")
    result, error = basic.run('<stdin>', text)
    if error is not None:
        print(colorama.Fore.RED, error.as_string())
    else:
        print(colorama.Fore.YELLOW, result)
