from os import getpid
from datetime import datetime

from dst import *



def proceso(aci,tx_in,tx_out,tx_sa):
    print tx_in
    if len(tx_in) < 14:
        tx_out = generator_space(14)+ ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 14:
        tx_out = generator_space(14) + ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}


    data = {}
    data["modo"] = "ayslev"


    data["cod_curso"]=tx_in[0:][:7]

    if data["cod_curso"][3:].isdigit() == False:
        tx_out = generator_space(14) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data["cod_seccion"]=tx_in[7:][:2]

    if data["cod_seccion"].isdigit() == False:
        tx_out = generator_space(14)+ ("03")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data["cod_ano"]=tx_in[9:][:4]

    hoy = datetime.now()
    if data["cod_ano"].isdigit():
        if int(data["cod_ano"]) > hoy.year or int(data["cod_ano"]) < 2010:
            tx_out = generator_space(14)+ ("04")
            return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data["cod_sem"]=tx_in[13]

    if data["cod_sem"] != "1" and data["cod_sem"] != "2":
        tx_out = generator_space(14)+ ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    pid = getpid()
    cola = Cola_mensajes()

    respuesta = cola.enviar(pid,data)

    #print "ACA",respuesta
    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




