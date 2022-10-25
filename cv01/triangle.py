
def triangle(a, b, c):
    """
    Funkce vrací True nebo False, podle toho zda strany a, b, c mohou tvořit
    pravoúhlý trojúhelník

    Pro jednoduchost můžete předpokládat, že strany a, b jsou odvěsny, c je přepona.
    Tak jako je to ve známé matematické poučce.
    """

    if c ** 2 == a ** 2 + b ** 2:
        return True;

    return False


