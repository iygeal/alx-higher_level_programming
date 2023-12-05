#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python list
 * @p: A python object
 **/
void print_python_list_info(PyObject *p)
{
	long int list_size;
	int i;
	PyListObject *obj;

	obj = (PyListObject *)p;
	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < list_size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
