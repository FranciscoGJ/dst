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
    verif_filt = {}
    verif["modo"] = "ayenv0_verif"
    hoy=datetime.now()
    verif_filt["cod_curso"] = tx_in[:7]
    verif_filt["cod_sec"] = tx_in[7:][:2]
    verif_filt["cod_ano"] = "%s"%(hoy.year)
    verif_filt["cod_sem"] = "%s"%(int(hoy.month/6)+1)
    verif["filt"] = verif_filt

    verif_res = cola.enviar(verif)

    if not verif_res["existe"]:
        tx_out = generator_space(23) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["vacantes"]:
        tx_out = generator_space(23) + ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data["modo"] = "ayenv0"
    data["curso"] = tx_in[:7]
    data["seccion"] = tx_in[7:][:2]
    data["rut"] = tx_in[9:][:9]
    data["id"] = verif["id"] + data["rut"]
    data["motivo"] = tx_in[18:]
    data["status"] = "Pendiente"

    respuesta = cola.enviar(data)

    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}