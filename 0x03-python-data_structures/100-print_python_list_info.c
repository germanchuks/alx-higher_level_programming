#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int index, list_size, list_allocated;
	PyObject *element;

	list_allocated = ((PyListObject *)p)->allocated;
	list_size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", list_allocated);

	for (index = 0; index < list_size; index++)
	{
		printf("Element %d: ", index);

		element = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(element)->tp_name);
	}
}
