Thrift type system
=======================================

The thrift type system includes base types like bool, byte, double, string and integer but also special types like binary and it also supports structs (equivalent to classes but without inheritance) and also containers (list, set, map) that correspond to commonly available interfaces in most programming languages. The type system focuses on key types available in all programming languages and omits types that are specific to only some programming languages.

* A detailed reference to Thrift type system follows next and more details can be found here: http://thrift.apache.org/docs/types
* If you want to check the Thrift interface description language that allows for the definition of Thrift types you can read here: http://thrift.apache.org/docs/idl

Base types
-----------

    * **bool**: A boolean value (true or false)

    * **byte**: An 8-bit signed integer

    * **i16**: A 16-bit signed integer

    * **i32**: A 32-bit signed integer

    * **i64**: A 64-bit signed integer

    * **double**: A 64-bit floating point number

    * **string**: A text string encoded using UTF-8 encoding

*Note: There is no support for unsigned integer types, due to the fact that there are no native unsigned integer types in many programming languages. Signed integers can be safely cast to their unsigned counterparts when necessary.*

Special Types
--------------

**binary**: a sequence of unencoded bytes

Structs
--------

A struct has a set of strongly typed fields, each with a unique name identifier. The look very similar to C-like structs. ::

	struct Example {
	  1:i32 number=10,
	  2:i64 bigNumber,
	  3:double decimals,
	  4:string name="thrifty"
	}

Containers
-----------
   * **list** (Maps to c++ STL vector, Java ArrayList etc)

   * **set** (Maps to an STL set, Java HashSet etc)

        * PHP doesn’t support sets - so it is treated similar to a List map

   * **map** (Maps to an STL map, Java HashMap etc)

All the above are the defaults but can be customized to correspond to different types of any language. For this reason custom code generation directives have been added.

Exceptions
-----------

They inherit from the native exception base class as appropriate in each target programming language. ::

	exception InvalidOperation {
 	1: i32 what,
  	2: string why
	}


Services
--------
A service consists of a set of named functions, each with a list of parameters and a return type. It is semantically equivalent to defining an interface or a pure virtual abstract class. ::

	service <name> {
	<returntype> <name>(<arguments>)
	[throws (<exceptions>)]
	...
	}

	An example:
	service StringCache {
	void set(1:i32 key, 2:string value),
	string get(1:i32 key) throws (1:KeyNotFound knf),
	void delete(1:i32 key)
	}



.. toctree::
   :maxdepth: 2
   

