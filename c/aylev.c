#include "pythondst.h"

void proceso (char *aci, struct trans *tx_in, struct trans *tx_out, struct trans *tx_sa){

        char module[] ="m_ayudantias.aylev";
        Python(module,aci,tx_in,tx_out,tx_sa);
}