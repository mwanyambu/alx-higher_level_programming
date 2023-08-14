#include <python.h>
/**
 * print_python_list_info - info of a python list
 * @p: python list
 */
void print_python_list_info(Py0bject *p)
{
	Py0bject *lst_object;
	Py_ssize_t lst_size, x;

	lst_size= Pylist_size(p);
	if (lst_size < 0)
	{
		printf("Failed to get the size of the list\n");
		return;
	}
	printf("[*] Size of python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyList0bject *)p)->allocated);
	for (x = 0; x < lst_size; x++)
	{
		printf("Element %ld", x);

		lst_object = PyList_GetItem(p, x);
		if (lst_object == Null)
		{
			printf("Failed to get an item at index %ld\n", x);
			continue;
		}
		printf("Type: %s\n", lst_object->obj_type->tp_name);
	}
}
