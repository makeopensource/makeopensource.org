# run `$ python generate_key.py` from /website
from django.core.management.utils import get_random_secret_key
from pathlib import Path

with open(Path('mos') / '.env', 'w') as f:
	f.write('SECRET_KEY=' + get_random_secret_key())

