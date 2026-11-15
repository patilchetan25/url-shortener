# The core logic of the URL shortener: making codes, saving links and finding them.
import secrets
import string

# The 62 characters a code can use: a–z, A–Z and 0–9.
ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 7

# In-memory storage: code → long URL. Phase 2 replaces this with Postgres,
# and only this file will need to change.
urls: dict[str, str] = {}

def generate_code() -> str:
    # Pick CODE_LENGTH random characters and join them into one string.
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


def shorten_url(long_url: str) -> str:
    # Save a long URL under a new, unused code, and return that code.
    code = generate_code()
    # Step 1.6: keep trying until the code isn't already taken.
    while code in urls:
        code = generate_code()
    urls[code] = long_url
    return code

# "str | None" means it returns either a string or None.
def get_long_url(code: str) -> str | None:
    # Return the long URL for a code, or None if the code doesn't exist.
    # Deciding that None means "404" is the route's job, not the service's.
    return urls.get(code)
