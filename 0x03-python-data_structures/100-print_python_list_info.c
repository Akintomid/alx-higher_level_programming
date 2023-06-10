#include "/usr/include/python3.8/Python.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t a;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (a = 0; a < size; a++)
	{
		item = PyList_GetItem(p, a);

		printf("Element %zd: %s\n", a, Py_TYPE(item)->tp_name);
	}
}
