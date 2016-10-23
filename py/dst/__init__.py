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
    rut=rut_digito[:8]
    digito=rut[8]
