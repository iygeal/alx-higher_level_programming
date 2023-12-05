#include "/usr/include/python3.4/Python.h"
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python list
 * @p: python object
 **/
void print_python_list_info(PyObject *p)
{
	long int size;
	int i;
	PyListObject *obj;

	if (!PyList_Check(p) || !p)
	{
		fprintf(stderr, "Invalid Python List\n");
		return;
	}

	size = PyList_Size(p);
	obj = (PyListObject *)p;

	if (size < 0)
	{
		fprintf(stderr, "Failed to get size of Python List\n");
		return;
	}

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		if (!obj->ob_item[i])
		{
			fprintf(stderr, "Failed to get Python List item\n");
			return;
		}
	printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
