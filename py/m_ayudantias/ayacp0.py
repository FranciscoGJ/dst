from datetime import datetime

from dst import *

def proceso(aci,tx_in,tx_out,tx_sa):

	if len(tx_in) != 18:
        tx_out = generator_space(418)+"99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 18:
        tx_out = tx_out = generator_space(418)+"99"
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}
 	
 	cola = Cola_mensajes()

 	hoy = datetime.now()
    verif = {} 
    verif["modo"] = "ayconp_verif"
    verif["id"] = tx_in[:9] + "%s%s"%(hoy.year,int(hoy.month/6)+1) + tx_in[:9]

    verif_res = cola.enviar(verif)

    if not verif_res["existe"]:
        tx_out = generator_space(418) + ("02")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif not verif_res["postulacion"]:
        tx_out = generator_space(418) + ("03")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    data = {}
    data["modo"] = "ayacp0"