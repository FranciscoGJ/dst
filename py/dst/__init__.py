from enviar_demonio import Cola_mensajes
def generator_space(x):
    return "".join([" " for i in range(x)])


from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def verificador_rut(rut_digito):
    rut=str(int(rut_digito[:8]))
    digito=rut_digito[8].upper()
    print digito,rut
    digito_correcto= digito_verificador(rut)
    print digito_correcto
    if digito_correcto==10:
        digito_correcto="K"
    if str(digito_correcto)==str(digito):
        return True
    return False

