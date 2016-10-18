from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 9:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 9:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    #verif rut
    #if tx_in[9:].count(' ') == 400:
    #    tx_out = generator_space(23) + ("03")
    #    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()

    hoy = datetime.now()
    verif = {}
    verif["modo"] = "ayenv0_verif"
    verif["id"] = tx_in + "%s%s"%(hoy.year,int(hoy.month/6)+1)


    verif_res = cola.enviar(verif)

    if not verif_res["existe"]:
        tx_out = "01"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["vacantes"]:
        tx_out = "02"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    aci = "1"

    data = {}
    data["modo"] = "aycon0"
    data["solicitud_id"] = verif["id"]

    respuesta = cola.enviar(data)

    print respuesta

    from time import sleep
    sleep(25)



    tx_out = ""
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}