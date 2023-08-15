#include <Python.h>
/**
 * print_python_list_info - info of a python list
 * @p: python list
 * Return: bit index else -1
 */
void print_python_list_info(PyObject *p)
{
	PyObject *lst_object;
	int size, lst_size, x;

	size = Py_SIZE(p);

	lst_size= ((PyListObject *)p)->allocated;
	printf("[*] Size of python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lst_size);
	for (x = 0; x < lst_size; x++)
	{
		printf("Element %d: ", x);

		lst_object = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(lst_object)->tp_name;
	}
}
