"""
@dataclass
"mutable namedtu0ples with default"
https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes

Custom __post_init__ method allows to use default field value, even the None is explicitly used for the field to init the dataclass 
https://stackoverflow.com/questions/56665298/how-to-apply-default-value-to-python-dataclass-field-when-none-was-passed
"""

from dataclasses import dataclass, fields
import dataclasses

@dataclass(unsafe_hash=True)
class LibVersion:
    '''Class of keeping track of lib version used to setup a container'''
    tensorflow: str|None # Union types with x|y for type hints
    numpy: str|None
    pandas: str|None = "1.5.0" # field with default value, must declared after fields without default value
    
    # Uncomment with "shift + cmd + 7" (cmd + /) inside vs code macosx
    def __post_init__(self):
        """
        this method allows to use default value in the dataclass if a None Type is given explicitly.
        """
        # Loop through the fields
        for field in fields(self):
            # If there is a default and the value of the field is none we can assign a value
            if not isinstance(field.default, dataclasses._MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)

def main():
    # use the default field value for field pandas
    local_version = LibVersion(tensorflow="2.10.0", numpy="1.23.3") 
    # use the default field value even a param value "None" is explicitly assigned, the __post_init__ method enables this behaviour
    dev_version = LibVersion(tensorflow="2.10.0", numpy="1.23.3", pandas=None)
    # override the default field value for field pandas
    prod_version = LibVersion(tensorflow="2.10.0", numpy="1.23.3", pandas="1.4.1")
    
    # call the __repr__ method of object
    print(f"local_version {local_version}")
    print(f"dev_version {dev_version}")
    print(f"prod_version {prod_version}")

    # __hash__, __eq___ function test
    print(f"does local_version equal dev_version? {local_version == dev_version}") # uncomment the __post_init__ to see the difference
    print(f"does local_version equal prod_version? {local_version == prod_version}")


if __name__ == "__main__":
    main()    
