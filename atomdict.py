def atomicDict():
    ele={"Na":'Sodium', "Al":'Aluminium'}
    print(ele)
    key=input("Enter the symbol for the element\n")
    value=input("Enter the name of the symbol {}: \n".format(key))
    ele.update({key:value})
    key=input("Enter symbol for duplicate element\n")
    value=input("Enter the name of the duplicate symbol {}\n".format(key))
    ele.update({key:value})
    print("The number of elements in the dicitonary are {}".format(len(ele)))
    search=input("Enter the value to be searched: ")
    if search in ele.values():
        print("found")
    else:
        print("not found")

atomicDict()