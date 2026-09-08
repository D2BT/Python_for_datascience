from typing import Any

def NULL_not_found(obj: Any) -> int:

    # 1. On récupère le type pour l'affichage final
    obj_type = type(obj)

    # 2. On commence les vérifications spécifiques
    # Cas du None (Nothing)
    if obj is None:
        print(f"Nothing: None {obj_type}")
    
    # Cas du NaN (Garlic) : C'est un float qui n'est pas égal à lui-même
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: nan {obj_type}")

    # Cas du Zero (Zero) : On vérifie que c'est un int ET que c'est 0
    # On utilise 'is not bool' car False == 0 en Python !
    elif isinstance(obj, int) and obj == 0 and obj_type is not bool:
        print(f"Zero: 0 {obj_type}")

    # - La chaîne vide (Empty)
    elif isinstance(obj, str) and obj == "":
        print(f"Empty:  {obj_type}")

    # ... tes tests if/elif ...
    elif obj is False:
        print(f"Fake: False {obj_type}")
    
    else:
        print("Type not Found")

    return 1