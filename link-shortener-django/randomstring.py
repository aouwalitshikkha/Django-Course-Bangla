import random
import string


def sample_generator():
    letters = string.ascii_letters
    digits = string.digits
    character = letters+digits
    sample_character = ''.join(random.sample(character, 4))
    return sample_character

