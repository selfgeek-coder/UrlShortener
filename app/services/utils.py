import string
from secrets import choice

def generate_slug(length: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits
    
    return "".join(choice(alphabet) for _ in range(length))
