import eel

# Set web files folder
eel.init('web')

@eel.expose
def start_algorithm(n,lista):
    print(n,lista)
    return ("working")

eel.start('index.html', size=(1000, 600))
