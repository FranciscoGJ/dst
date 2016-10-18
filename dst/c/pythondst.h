#include "/usr/include/python2.7_d/Python.h"
#include <stdio.h>
#include <string.h>
struct trans{
        int len;
        char datos [2000];
};

void Python(char *Module,char *aci, struct trans *tx_in, struct trans *tx_out, struct trans *tx_sa){

    Py_Initialize();
    PyRun_SimpleString("from sys import path;path.append(\"/home/alumnos/18020677/dst/py\")");

    PyObject* myModuleString = PyString_FromString(Module);
    PyObject* myModule       = PyImport_Import(myModuleString);
    PyObject* myFunction     = PyObject_GetAttrString(myModule, "proceso");
    PyObject* args = PyTuple_Pack(4,PyString_FromString(aci),PyString_FromString(tx_in->datos),PyString_FromString(tx_out->datos),PyString_FromString(tx_sa->datos));
    PyObject *ret;
    ret=PyObject_CallObject(myFunction,args);
    PyObject* out = PyDict_GetItemString(ret,"tx_out");
    PyObject* sa = PyDict_GetItemString(ret,"tx_sa");
    PyObject* acis = PyDict_GetItemString(ret,"aci");

    strcpy(aci,PyString_AsString(acis));
    strcpy(tx_out->datos,PyString_AsString(out));
    tx_out->len= strlen(tx_out->datos);
    strcpy(tx_sa->datos,PyString_AsString(sa));
    tx_sa->len= strlen(tx_sa->datos);
    Py_Finalize();


}