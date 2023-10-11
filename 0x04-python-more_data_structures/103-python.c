#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: Python object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	long int size, i, limit;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	string = PyBytes_AS_STRING(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	limit = (size >= 10) ? 10 : size;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_list - prints information about a Python list
 * @p: Python object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		const char *type_name = Py_TYPE(obj)->tp_name;

		printf("Element %ld: %s\n", i, type_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
