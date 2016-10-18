from os import getpid
from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) < 515:
        tx_out = generator_space(22)+ ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 515:
        tx_out = generator_space(22) + ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}



    data = {}
    data["modo"] = "ayenv0"



    pid = getpid()
    cola = Cola_mensajes()

    respuesta = cola.enviar(pid,data)


    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




