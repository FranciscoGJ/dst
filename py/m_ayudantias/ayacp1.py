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



