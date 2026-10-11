import os

def clean_screen():
    try:
        from IPython.display import clear_output
        clear_output(wait=True)
    except (ImportError, ModuleNotFoundError):
        pass

    os.system('cls' if os.name == 'nt' else 'clear')