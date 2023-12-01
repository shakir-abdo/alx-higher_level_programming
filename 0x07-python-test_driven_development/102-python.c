#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] String Object Info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GetLength(p);

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  Type: Compact ASCII\n");
    else
        printf("  Type: Compact Unicode Object\n");

    printf("  Length: %ld\n", length);


    wchar_t *value = PyUnicode_AsWideCharStringAndSize(p, &length);
    if (value)
    {
        printf("  Value: %ls\n", value);
        PyMem_Free(value);
    }
    else
    {
        printf("  [ERROR] Unable to retrieve string value\n");
    }
}
