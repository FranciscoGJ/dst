from os import getpid
from enviar_demonio import Cola_mensajes

def proceso(aci,tx_in,tx_out,tx_sa):
    print tx_in
    data = {}
    data["modo"] = "ay_levantas_solicitud"
    data["cod_curso"]=tx_in[0:][:7]
    data["cod_seccion"]=tx_in[7:][:2]
    data["cod_ano"]=tx_in[9:][:4]
    data["cod_sem"]=tx_in[13]
    pid = getpid()

    cola = Cola_mensajes()
    respuesta = cola.enviar(pid,data)
    print "aca",respuesta

    from time import sleep
    sleep(6)

    tx_out = "0201"

    return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}




