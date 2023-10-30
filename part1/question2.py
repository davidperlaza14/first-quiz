################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`

def swapper(t):
  """
  Me parecio mejor  crear una funcion que intercambiara los elemtos de la tupla que, una variable. 
  
  Keyword arguments:
    t (tupla): Esta es la tupla de los dos elementos a intercambiarse.
  Return: return_description
    Tuble: Devuelve  la tupla nueva con los items intercambiados.
  """
  
  return (t[1], t[0])

def run_swapper(list_of_tuples):
  return list(map(swapper, list_of_tuples))


run_swapper()