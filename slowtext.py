# Dead function, idea for later

'''
try:
    from time import sleep
except ModuleNotFoundError:
    print("Error, import failed")
    print("Game ended")
    sys.exit()


def intro_text(text):
    """Prints title of game in a typewriter style"""
    words = text

    for char in words:
        sleep(0.25)
        print(char, end="", flush=True) '''