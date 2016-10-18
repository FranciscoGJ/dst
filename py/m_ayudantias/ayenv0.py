from os import getpid
from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 418:
        tx_out = generator_space(22)+ ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 418:
        tx_out = generator_space(22) + ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    if tx_in[9:].count(' ') == 400:
        tx_out = generator_space(22) + ("04")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    #verif rut
    #if tx_in[9:].count(' ') == 400:
    #    tx_out = generator_space(22) + ("03")
    #    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    pid = getpid()
    cola = Cola_mensajes()

    verif = {}
    verif["modo"] = "ayenv0_verif"
    hoy=datetime.now()
    verif["id"] = tx_in[:9]+"%s%s"%(hoy.year,int(hoy.month/6)+1)

    verif_res = cola.enviar(pid,verif)

    if not verif_res["existe"]:
        tx_out = generator_space(22) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["vacantes"]:
        tx_out = generator_space(22) + ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data["modo"] = "ayenv0"
    data["curso"] = tx_in[:7]
    data["seccion"] = tx_in[7:][:2]
    data["rut"] = tx_in[9:][:9]
    data["id"] = verif["id"] + data["rut"]
    data["motivo"] = tx_in[18:]

    respuesta = cola.enviar(pid,data)

    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}