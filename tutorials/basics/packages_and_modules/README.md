## Introduction

3 objects: | caller | <-> | package(\_\_init\_\_.py) > module |

Common Attributes:
- `dir()`
- `__name__`

Attributes of caller:
- `sys.path`

Attributes of package:
- `__all__`

Attributes of module:
- `__file__`
- `__all__`

Keywords for importing:
- `from`
- `import`
- `as`
- `*`
- `.`
- `,`

Useful method:
- `importlib.reload()`

Important thinking:
- What happens when wildcard are used when importing packages.
- The special importing mechanism in \_\_init\_\_.py.
- The differences in the wildcard import mechanism between packages and modules.
- The absolute import and relative import.
- un-public object with underscore.

[Online Tutorial](https://realpython.com/python-modules-packages/)

## Conclusion

In this tutorial, you covered the following topics:

How to create a Python module
Locations where the Python interpreter searches for a module
How to obtain access to the objects defined in a module with the import statement
How to create a module that is executable as a standalone script
How to organize modules into packages and subpackages
How to control package initialization

If you want to learn more, check out the following documentation at Python.org:
- [The import system](https://docs.python.org/3/reference/import.html)
- [The Python tutorial: Modules](https://docs.python.org/3/tutorial/modules.html)
