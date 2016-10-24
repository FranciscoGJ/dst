from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 1:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 1:
        tx_out = "99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    if tx_in != "y" and tx_in != "n":
    	tx_out = "02"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	if tx_in == "y":
	    cola = Cola_mensajes()

	   	data = {}
	   	data_filter = {}
	   	data["modo"] = "ayelp1"
	   	data_filter["id"] = tx_sa
	   	data["filter"] = data_filter

	   	respuesta = cola.enviar(data)

	   	tx_out = "%s%s"(generator_space(418),"01")

	elif tx_in == "n":
		tx_out = "03"
		aci = "ayelp101"

	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}