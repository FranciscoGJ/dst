from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 18:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 18:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()

    hoy = datetime.now()
    verif = {}
    verif_filter = {}

    verif["modo"] = "ayconp_verif"

    verif_filter["curso"] = tx_in[:7]
    verif_filter["sec"] = tx_in[7:][:2]
    verif_filter["id"] = tx_in[:9] + "%s%s"%(hoy.year,int(hoy.month/6)+1) + tx_in[9:]
    verif["filter"] = verif_filter

    verif_res = cola.enviar(verif)

    if not verif_res["existe"]:
        tx_out = "02"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["postulacion"]:
        tx_out = "03"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif verif_res["status"] != "Pendiente":
        tx_out = "04"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data_filter = {}
    data["modo"] = "ayacp0"
    data_filter["curso"] = tx_in[:7]
    data_filter["sec"] = tx_in[7:][:2]
    data_filter["ano"] = "%s"%(hoy.year)
    data_filter["sem"] = "%s"%(int(hoy.month/6)+1)
    data_filter["rut"] = tx_in[:9]
    data_filter["id"] = "%s%s%s%s%s"%(tx_in[:7],tx_in[7:][:2],hoy.year,int(hoy.month/6)+1,tx_in[9:])
    data["filter"] = data_filter

    respuesta = cola.enviar(data)

    aci = "ayacp001"

    tx_sa = data_filter["id"]

    tx_out = "%s%s%s"%(tx_in[:9],respuesta["motivo"],"01")

    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

