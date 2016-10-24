from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 400:
        tx_out = tx_in[:409]+"99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 400:
        tx_out = tx_in[:409]+"99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
 	
 	cola = Cola_mensajes()

 	data = {}
 	data_filter = {}
 	data["modo"] = "ayacp1"
 	data_filter["id"] = tx_sa
 	data_filter["motivo"] = tx_in
 	data["filter"] = data_filter

 	respuesta = cola.enviar(data)

 	tx_out = "%s%s%s"%(generator_space(409),respuesta["code"])
 	tx_sa = ""
 	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}