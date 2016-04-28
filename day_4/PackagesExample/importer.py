from A.classes import Animal, Poacher, Tourist
from A.functions import word_count, sum_of_digits

print Animal, word_count
#another way
import A.functions as func
import A.classes as classes

print Animal, word_count
print classes.Animal, func.word_count