#include <Python.h>
/**
 * print_python_list_info - info of a python list
 * @p: python list
 * Return: bit index else -1
 */
void print_python_list_info(PyObject *p)
{
	PyObject *lst_object;
	Py_ssize_t lst_size, x;

	lst_size= Pylist_Size(p);
	if (lst_size < 0)
	{
		printf("Failed to get the size of the list\n");
		return;
	}
	printf("[*] Size of python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (x = 0; x < lst_size; x++)
	{
		printf("Element %ld", x);

		lst_object = PyList_GetItem(p, x);
		if (lst_object == Null)
		{
			printf("Failed to get an item at index %ld\n", x);
			continue;
		}
		printf("%s\n", lst_object->ob_type->tp_name);
	}
}
