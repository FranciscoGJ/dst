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
    data['modo']="ayslev"
    data['item']={}


    data['item']["curso"]=tx_in[0:][:7]

    if data['item']["curso"][3:].isdigit() == False:
        tx_out = generator_space(14) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data['item']["sec"]=tx_in[7:][:2]

    if data['item']["sec"].isdigit() == False:
        tx_out = generator_space(14)+ ("03")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data['item']["ano"]=tx_in[9:][:4]

    hoy = datetime.now()
    if data['item']["ano"].isdigit():
        if int(data['item']["ano"]) > hoy.year or int(data['item']["ano"]) < 2010:
            tx_out = generator_space(14)+ ("04")
            return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data['item']["sem"]=tx_in[13]

    if data['item']["sem"] != "1" and data['item']["sem"] != "2":
        tx_out = generator_space(14)+ ("05")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    cola = Cola_mensajes()
    data['item']["status"] = "Pendiente"
    data['item']['id'] = "%s%s%s%s" % (data['item']['curso'], data['item']['sec'], data['item']['ano'], data['item']['sem'])


    respuesta = cola.enviar(data)

    tx_out = "%s%s"%(respuesta["id"],respuesta["code"])
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




