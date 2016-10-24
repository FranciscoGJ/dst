from datetime import datetime

from dst import *

limit = 4

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 9:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 9:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}


    cola = Cola_mensajes()

    hoy = datetime.now()
    verif = {}
    verif_filter = {}
    verif["modo"] = "aycon0_verif"
    verif_filter["curso"] = tx_in[:7]
    verif_filter["sec"] = tx_in[7:][:2]
    verif_filter["id"] = tx_in + "%s%s"%(hoy.year,int(hoy.month/6)+1)
    verif["filter"] = verif_filter

    verif_res = cola.enviar(verif)

    if not verif_res["existe"]:
        tx_out = "01"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["vacantes"]:
        tx_out = "02"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data_filter = {}
    data["modo"] = "aycon0"
    data_filter["solicitud_id"] = verif_filter["id"]
    data["filter"] = data_filter
    data["offset"] = 0
    data["limit"] = limit

    respuesta = cola.enviar(data)

    aci = "aycon001"

    tx_sa = "%s|%s|%s|%s"%(data_filter["solicitud_id"],respuesta["total"],respuesta["start"],respuesta["end"])

    tx_out = "%s%s"%(respuesta["code"],tx_sa[:9])

    for result in respuesta["result"]:
        tx_out = tx_out + result["rut"] + result["motivo"]

    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}