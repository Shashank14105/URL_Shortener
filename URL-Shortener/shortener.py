

import random
import string
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    
    if not url or not url.strip():
        return False

    url = url.strip()
    try:
        result = urlparse(url)
    except ValueError:
        return False

    # Must have a scheme (http/https) and a domain (netloc)
    if result.scheme not in ("http", "https"):
        return False
    if not result.netloc:
        return False

    return True


def generate_short_code(existing_codes, length: int = 6) -> str:
    
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choice(characters) for _ in range(length))
        if code not in existing_codes:
            return code


def normalize_url(url: str) -> str:
    
    return url.strip()
