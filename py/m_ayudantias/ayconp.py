from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 18:
        tx_out = generator_space(418)+"99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 18:
        tx_out = tx_out = generator_space(418)+"99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    if not verificador_rut(tx_in[9:][:9]):
        tx_out = generator_space(23) + ("10")
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
        tx_out = generator_space(418) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["postulacion"]:
        tx_out = generator_space(418) + ("03")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data_filter = {}
    data["modo"] = "ayconp"
    data_filter["id"] = verif_filter["id"]
    data["filter"] = data_filter

    respuesta = cola.enviar(data)

    tx_out = "%s%s%s%s01"%(verif_filter["curso"],verif_filter["sec"],respuesta["motivo"],respuesta["status"])
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
