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
    filt = {}
    data["modo"] = "ayslev"


    filt["cod_curso"]=tx_in[0:][:7]

    if filt["cod_curso"][3:].isdigit() == False:
        tx_out = generator_space(14) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    filt["cod_seccion"]=tx_in[7:][:2]

    if filt["cod_seccion"].isdigit() == False:
        tx_out = generator_space(14)+ ("03")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    filt["cod_ano"]=tx_in[9:][:4]

    hoy = datetime.now()
    if filt["cod_ano"].isdigit():
        if int(filt["cod_ano"]) > hoy.year or int(filt["cod_ano"]) < 2010:
            tx_out = generator_space(14)+ ("04")
            return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    filt["cod_sem"]=tx_in[13]

    if filt["cod_sem"] != "1" and filt["cod_sem"] != "2":
        tx_out = generator_space(14)+ ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()
    data["filter"] = filt

    respuesta = cola.enviar(data)

    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    print tx_out
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




