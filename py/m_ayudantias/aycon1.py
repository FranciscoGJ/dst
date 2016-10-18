from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 418:
        tx_out = generator_space(23)+ ("99")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 418:
        tx_out = generator_space(23) + ("99")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    #verif rut
    #if tx_in[9:].count(' ') == 400:
    #    tx_out = generator_space(23) + ("03")
    #    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()

    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}