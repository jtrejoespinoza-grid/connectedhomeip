

from chip.ChipDeviceCtrl import ChipDeviceControllerBase
from chip.ChipDeviceCtrl import ChipDeviceController
import inspect

class_arr = [ChipDeviceController, ChipDeviceControllerBase]
table = []


x = range(1, 2)

for n in x:
    print(n)

exit()

for tmp_class in class_arr:
    print(f"Running for class : {tmp_class}")
    class_name_methods = [method for method in tmp_class.__dict__.values() if callable(
        method) and method.__qualname__.startswith(tmp_class.__name__ + '.')]

    for method in class_name_methods:
        method_name = method.__name__
        is_raises = False
        is_return = False
        try:

            print(f"Trying the method : {method_name}")
            source_code = inspect.getsource(method)
            docstring = inspect.getdoc(method)
            has_docstring = 0 if source_code is None else 1
            print(f"Source code for {method_name}:")
            # print(source_code)
            if 'raises' in source_code or 'raise' in source_code:
                is_raises = True
                print(f"This code raises and exception")

            if 'return' in source_code:
                is_return = True
                print("This code returs something")

            if docstring is None:
                print(f"No source code for {method_name}")
            else:
                print(f"Contains docstring for method {method_name}")
                # print(docstring)
                # row index

            if docstring is not None:
                doc_has_raises = 1 if 'Raises:' in docstring else 0
                doc_has_returns = 1 if 'Returns:' in docstring else 0
            else:
                doc_has_returns = 0
                doc_has_raises = 0
            # 0 name
            # 1 code has raise
            # 2 code has return
            # 3 has docstring
            # 4 has Raises
            # 5 has Returns
            row = [method_name, is_raises, is_return, has_docstring, doc_has_raises, doc_has_returns]
            table.append(row)

        except OSError:
            print(f"Could not retrieve source code for {method_name} (likely a built-in method)")

for r in table:
    print(r)
