classes_with_module_attribute = []

for subclass in (1).__class__.__base__.__subclasses__():
    print(subclass)
    try:
        print(subclass.__init__)
        if hasattr(subclass.__init__, '__globals__'):
            classes_with_module_attribute.append(subclass)
    except:
        pass

if classes_with_module_attribute:
    print("Classes with __globals__ attribute:")
    print(classes_with_module_attribute)
    #for subclass in classes_with_module_attribute:
        #print(subclass)
else:
    print("No subclasses with _module attribute found.")
