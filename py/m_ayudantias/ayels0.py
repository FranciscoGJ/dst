from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 14:
		tx_out = "99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	elif tx_in.count(' ') == 14:
		tx_out = "99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	cola = Cola_mensajes()

	hoy = datetime.now()
	verif = {}
	verif_filter = {}
	verif["modo"] = "aycon0_verif"
	verif_filter["curso"] = tx_in[:7]
	verif_filter["sec"] = tx_in[7:][:2]
	verif_filter["id"] = tx_in
	verif["filter"] = verif_filter

	verif_res = cola.enviar(verif)

	if not verif_res["existe"]:
		tx_out = "02"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	elif not verif_res["vacantes"]:
		tx_out = "03"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	data = {}
	data_filter = {}
	data["modo"] = "ayels0"
	data_filter["id"] = verif_filter["id"]
	data["filter"] = data_filter

	respuesta = cola.enviar(data)

	aci = "ayels001"

	count=str(respuesta["count"])

	tx_out = "%s%s%s%s"%(verif_filter["id"],respuesta["status"],generator_space(4-len(count))+count,"01")

	return {'tx_out':tx_out,'tx_sa':tx_out[:27],'aci':aci}



