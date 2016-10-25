from datetime import datetime

from dst import *

limit = 4

def proceso(aci,tx_in,tx_out,tx_sa):

    if len(tx_in) != 1:
        tx_out = "99"+generator_space(1645)
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 1:
        tx_out = "99"+generator_space(1645)
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
    
    if tx_in != "s" and tx_in != "a":
        tx_out = "02"+generator_space(1645)
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
    #print "0!"
    tx_sa_arr = tx_sa.split("|")

    solicitud_id = tx_sa_arr[0]
    total = int(tx_sa_arr[1])
    start = int(tx_sa_arr[2])
    offset = int(tx_sa_arr[3])
    
    code = ""
    
    cola = Cola_mensajes()
    
    data = {}
    data_filter = {}
    data["modo"] = "aycon0"
    data_filter["solicitud_id"] = solicitud_id
    data["filter"] = data_filter
    data["limit"] = limit
 
    #print "1!"
    if tx_in == "a":
        if start == 0:
            code = "03"
            data["offset"] = start
            tx_sa = "%s|%s|%s|%s"%(solicitud_id,total,start,offset)
            respuesta = cola.enviar(data)
            tx_out = "%s%s"%(code,tx_sa[:9])
            for result in respuesta["result"]:
                tx_out = tx_out + result["rut"] + result["motivo"]
            
        else:
            code = "01"
            offset = start-limit
            data["offset"] = offset
            respuesta = cola.enviar(data)
            tx_out = "%s%s"%(code,tx_sa[:9])
            for result in respuesta["result"]:
                tx_out = tx_out + result["rut"] + result["motivo"]
            tx_sa = "%s|%s|%s|%s"%(data_filter["solicitud_id"],respuesta["total"],respuesta["start"],respuesta["end"])
            
    elif tx_in == "s":
        if total == offset:
            code = "04"
            data["offset"] = start
            tx_sa = "%s|%s|%s|%s"%(solicitud_id,total,start,offset)
            respuesta = cola.enviar(data)
            tx_out = "%s%s"%(code,tx_sa[:9])
            for result in respuesta["result"]:
                tx_out = tx_out + result["rut"] + result["motivo"]
        
        else:
            code = "01"
            data["offset"] = offset
            respuesta = cola.enviar(data)
            tx_out = "%s%s"%(code,tx_sa[:9])
            for result in respuesta["result"]:
                tx_out = tx_out + result["rut"] + result["motivo"]
            tx_sa = "%s|%s|%s|%s"%(data_filter["solicitud_id"],respuesta["total"],respuesta["start"],respuesta["end"])

    #print "2!"
    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}