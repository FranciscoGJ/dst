def proceso(aci,tx_in,tx_out,tx_sa):
	simbolo=tx_in[0]
	numero_1=tx_in[1:][:5]
	numero_2=tx_in[6:][:10]

	return {'tx_out':tx_out,'tx_sa':tx_sa,'aci':aci}