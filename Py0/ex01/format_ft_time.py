import time
from datetime import datetime

# 1. Obtenir le timestamp actuel
now = time.time()

# 2. Afficher la première ligne
# On utilise les f-strings pour formater le nombre 'now'
print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")

# 3. Afficher la deuxième ligne
# On convertit le timestamp en objet date, puis on le formate
date_obj = datetime.fromtimestamp(now)
print(date_obj.strftime("%b %d %Y"))