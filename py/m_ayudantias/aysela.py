from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 23:
		tx_out = "99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	elif tx_in.count(' ') == 23:
		tx_out = "99"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    if not verificador_rut(tx_in[14:][:9]):
        tx_out = generator_space(23) + ("10")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}


	cola = Cola_mensajes()

	hoy = datetime.now()
	verif = {}
	verif_filter = {}

	verif_filter["curso"] = tx_in[:7]
	verif_filter["sec"] = tx_in[7:][:2]
	verif_filter["ano"] = tx_in[9:][:4]
	verif_filter["sem"] = tx_in[13]
	verif_filter["rut"] = tx_in[14:]
	verif_filter["solicitud_id"] = tx_in[:14]
	verif_filter["postulacion_id"] = tx_in
	verif["filter"] = verif_filter
	verif["modo"] = "aysela_verif"

	verif_res = cola.enviar(verif)

	if not verif_res["existe"]:
		tx_out = "02"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
	if not verif_res["vacantes"]:
		tx_out = "03"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
	if not verif_res["postulacion"]:
		tx_out = "04"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
	if verif_res["status"] == "Resuelto":
		tx_out = "05"
		return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

	data = {}
	data_filter = {}
	data_filter["solicitud_id"] = verif["filter"]["solicitud_id"]
	data_filter["postulacion_id"] = verif["filter"]["postulacion_id"]
	data["filter"] = data_filter
	data["modo"] = "aysela"

	respuesta = cola.enviar(data)

	tx_out = respuesta["code"]

	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}