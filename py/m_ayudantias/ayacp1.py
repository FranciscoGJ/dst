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
	data_item = {}
	data["modo"] = "ayacp1"
	data_filter["id"] = tx_sa
	data_item["motivo"] = tx_in
	data["item"] = data_item
	data["filter"] = data_filter

	respuesta = cola.enviar(data)

	tx_out = "%s%s"%(generator_space(409),"01")
	tx_sa = ""
	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}