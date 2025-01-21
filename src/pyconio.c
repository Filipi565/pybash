#include <Python.h>
#include <memory.h>
#include <conio.h>

static PyObject *PyConioGetCH(PyObject *m, PyObject *args)
{
    return PyLong_FromLong(getch());
}

static PyObject *PyConioGetCHE(PyObject *m, PyObject *args)
{
    return PyLong_FromLong(getche());
}

static PyObject *PyConioPutCH(PyObject *m, PyObject *args)
{
    int c;

    if (!PyArg_ParseTuple(args, "i", &c))
    {
        return NULL;
    }

    return PyLong_FromLong(putch(c));
}

static PyObject *PyConioUnGetCH(PyObject *m, PyObject *args)
{
    int c;

    if (!PyArg_ParseTuple(args, "i", &c))
    {
        return NULL;
    }

    return PyLong_FromLong(ungetch(c));
}

static PyMethodDef methods[] = {
    {"ungetch", PyConioUnGetCH, METH_VARARGS},
    {"getche", PyConioGetCHE, METH_NOARGS},
    {"putch", PyConioPutCH, METH_VARARGS},
    {"getch", PyConioGetCH, METH_NOARGS},
    {NULL, NULL, 0, NULL}
};

static PyModuleDef module;

PyMODINIT_FUNC PyInit_conio()
{
    memset(&module, 0, sizeof(PyModuleDef));

    module.m_methods = methods;
    module.m_name = "conio";

    return PyModule_Create(&module);
}