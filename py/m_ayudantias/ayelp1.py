from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 2:
		tx_out = "99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	elif tx_in.count(' ') == 2:
		tx_out = "99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	if tx_in.lower() != "si" and tx_in.lower() != "no":
		tx_out = "02"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	if tx_in.lower() == "si":
		cola = Cola_mensajes()

		data = {}
		data_filter = {}
		data["modo"] = "ayelp1"
		data_filter["id"] = tx_sa
		data["filter"] = data_filter

		respuesta = cola.enviar(data)

		aci = "ayelp101"
		tx_out = "01"

	elif tx_in.lower() == "no":

		tx_out = "03"
		aci = "ayelp101"

	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}