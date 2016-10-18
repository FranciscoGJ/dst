from os import getpid
from enviar_demonio import Cola_mensajes

def proceso(aci,tx_in,tx_out,tx_sa):
    print tx_in
    if len(tx_in) < 14:
        tx_out = "".join([" " for i in range(14)]) + ("00")
        return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}

    elif tx_in.count(' ') == 14:
    	tx_out = "".join([" " for i in range(14)]) + ("00")
    	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}


    data = {}
    data["modo"] = "ay_levantar_solicitud"
    data["cod_curso"]=tx_in[0:][:7]
    data["cod_seccion"]=tx_in[7:][:2]
    data["cod_ano"]=tx_in[9:][:4]
    data["cod_sem"]=tx_in[13]
    pid = getpid()

    cola = Cola_mensajes()
    respuesta = cola.enviar(pid,data)
    
    #print "aca",respuesta

    #from time import sleep


    #tx_out = "123456789"

    #print tx_out

    #sleep(3)

    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




