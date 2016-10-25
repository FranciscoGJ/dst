from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):
    #print tx_in
    if len(tx_in) < 14:
        tx_out = generator_space(14)+ ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 14:
        tx_out = generator_space(14) + ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()

    data = {}
    data_filter = {}
    data['modo']="ayslev_verif"

    data_filter["curso"]=tx_in[0:][:7]

    if data_filter["curso"][3:].isdigit() == False:
        tx_out = generator_space(14) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data_filter["sec"]=tx_in[7:][:2]

    if data_filter["sec"].isdigit() == False:
        tx_out = generator_space(14)+ ("03")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data_filter["ano"]=tx_in[9:][:4]

    hoy = datetime.now()
    if data_filter["ano"].isdigit():
        if int(data_filter["ano"]) > hoy.year or int(data_filter["ano"]) < 2010:
            tx_out = generator_space(14)+ ("04")
            return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data_filter["sem"]=tx_in[13]

    if data_filter["sem"] != "1" and data_filter["sem"] != "2":
        tx_out = generator_space(14)+ ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data_filter["status"] = "Pendiente"
    data_filter['id'] = "%s%s%s%s" % (data_filter['curso'], data_filter['sec'], data_filter['ano'], data_filter['sem'])

    data["filter"] = data_filter

    res_verif = cola.enviar(data)

    if res_verif["existe"]:
        tx_out = generator_space(14)+ ("06")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data["modo"] = "ayslev"
    del data["filter"]
    data["item"] = data_filter
    respuesta = cola.enviar(data)

    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




