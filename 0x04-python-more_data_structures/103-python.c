#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints information about a Python list
 * @p: Python object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			PyObject *item = PyList_GetItem(p, i);
			const char *type_str = Py_TYPE(item)->tp_name;

			printf("Element %ld: %s\n", i, type_str);
		}
	}
}

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: Python object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_GET_SIZE(p);
		char *string = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", string);
		printf("  first 10 bytes: ");
		for (Py_ssize_t i = 0; i < size && i < 10; i++)
			printf("%02x ", (unsigned char)string[i]);
		printf("\n");
	}
	else
		printf("[ERROR] Invalid Bytes Object\n");
}
