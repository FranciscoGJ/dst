from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 418:
        tx_out = generator_space(23)+ ("99")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 418:
        tx_out = generator_space(23) + ("99")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    if tx_in[9:].count(' ') == 400:
        tx_out = generator_space(23) + ("04")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    #verif rut
    #if tx_in[9:].count(' ') == 400:
    #    tx_out = generator_space(23) + ("03")
    #    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()

    verif = {}
    verif_filter = {}
    verif["modo"] = "ayenv0_verif"
    hoy=datetime.now()
    verif_filter["curso"] = tx_in[:7]
    verif_filter["sec"] = tx_in[7:][:2]
    verif_filter["ano"] = "%s"%(hoy.year)
    verif_filter["sem"] = "%s"%(int(hoy.month/6)+1)
    verif_filter["id"] = "%s%s%s"%(tx_in[:9],hoy.year,int(hoy.month/6)+1)
    verif["filter"] = verif_filter

    verif_res = cola.enviar(verif)

    if not verif_res["existe"]:
        tx_out = generator_space(23) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["vacantes"]:
        tx_out = generator_space(23) + ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data_item = {}
    data_item["curso"] = tx_in[:7]
    data_item["sec"] = tx_in[7:][:2]
    data_item["rut"] = tx_in[9:][:9]
    data_item["ano"] = "%s"%(hoy.year)
    data_item["sem"] = "%s"%(int(hoy.month/6)+1)
    data_item["solicitud_id"] = verif_filter["id"]
    data_item["id"] = verif_filter["id"] + data_item["rut"]
    data_item["motivo"] = tx_in[18:]
    data_item["status"] = "Pendiente"
    data["filter"] = data_item

    data["modo"] = "ayconp_verif"
    id_res = cola.enviar(data)

    if id_res["postulacion"]:
        tx_out = "%s%s"%(data["filter"]["id"],"06")

    else:
        del data["filter"]
        data["item"] = data_item
        data["modo"] = "ayenv0"
        respuesta = cola.enviar(data)
        tx_out = "%s%s"%(respuesta["id"],respuesta["code"])

    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}