from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 2:
		tx_out = tx_sa+"99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	elif tx_in.count(' ') == 2:
		tx_out = tx_sa+"99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	if tx_in.lower() != "si" and tx_in.lower() != "no":
		tx_out = tx_sa+"02"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	if tx_in.lower() == "si":
		cola = Cola_mensajes()

		data = {}
		data_filter = {}
		data["modo"] = "ayels1"
		data_filter["id"] = tx_sa
		data["filter"] = data_filter

		respuesta = cola.enviar(data)

		tx_out = "%s%s"%(generator_space(27),"01")

	elif tx_in.lower() == "no":

		tx_out = "01"
		aci = "ayels101"

	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}