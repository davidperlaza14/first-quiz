################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class HornoMagico:
    def __init__(self):
        # Inicializa una nueva instancia del HornoMagico.
        # El horno se inicia sin ingredientes, a una temperatura "none" y sin un resultado definido.

        self.ingredients = []
        self.temperature = "None"
        self.output = None

    def add(self, item):
        # Añade un ingrediente al horno.
        self.ingredients.append(item)

    def freeze(self):
        # Congela los ingredientes en el horno.
        if self.temperature != "boiled":
            self.temperature = "frozen"

    def boil(self):
        # Hierve los ingredientes en el horno.
        self.temperature = "boiled"

    def wait(self):
        # Combina los ingredientes sin cambiar la temperatura.
        pass
    
    def get_output(self):
        """
        Obtiene el resultado de la combinación de ingredientes.
        
        Return:
            str: El resultado de la combinación de ingredientes.
        """
        
        if self.temperature == "frozen":
            self.output = "Ice " + " ".join(self.ingredients)
        elif self.temperature == "boiled":
            self.output = "Soup " + " ".join(self.ingredients)
        else:
            self.output = "Nixed " + " ".join(self.ingredients)
        return self.output


def make_oven():
    """
    Crea una nueva instancia de HornoMagico y la devuelve.

    Returns:
        HornoMagico: Una nueva instancia de la clase HornoMagico.
    """
    return HornoMagico()



def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)
    
    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()
    
    result = oven.get_output()  # Obtener el resultado después de cada operación.
    return result  # Devolver el resultado final después de todas las operaciones.