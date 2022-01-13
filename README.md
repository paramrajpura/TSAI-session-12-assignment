# Session 12 assignment of EPAi4.0

##Iterables and Iterators - II 
The topic covers following sections:

            Lazy Iterables
            In-Built Iterables
            Sorting Iterables
            The iter() function
            Iterating Callables
            Delegating Iterators
            Reversed Iteration
            Using Iterators as function arguments



#### Problem definition

This assignment's problem statement is formulated as follows:



The starting point for this assignment is the `Polygon` class and the `Polygons` sequence type you created in the previous assignment.

The code for these classes along with the unit tests for the `Polygon` class are below if you want to use those as your starting point. But use whatever you came up with in the last project.
You have two goals:

#### Goal 1:

Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").

 

#### Goal 2:

Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable and an iterator.

 

Once done, submit the publicly accessible GitHub link to this assignment page.

Your GitHub repo must have:

    Proper readme to understand what you have done 
    GitHub actions cleared for the test cases shared (optional with bonus scores)
    Your readme file MUST have the link to Google Colab or Deepnote, where we can read your notebook (most of the time when we check assignments, GitHub fails to render your notebooks, and if you have shared the Colab/Deepnote links, then we can see your word). 





**In Polygon.py:**

This _Polygon.py_. contains the class Polygon to fulfill the following requirements mentioned in problem definition.

The init function takes in:

      number of edges/vertices
      circumradius

The class Polygon has following properties and corresponding setter functions for properties marked with * mark:

      edges*
      circumradius*
      vertices
      interior angle
      edge length
      apothem
      area
      perimeter
        
Polygon class also has these functions:
      
      __repr__ : function representing the polygon with description of its properties
      __eq__ : function implements equality (==) based on # vertices and circumradius
      (__gt__) : function implements > based on number of vertices only 



**In Polygons.py:**

This _Polygons.py_. contains the class Polygons to fulfill the following requirements mentioned in problem definition.

The init function takes in:

      number of vertices for largest polygon in the sequence
      common circumradius for all polygons
        

The class Polygon has following properties and corresponding setter functions for properties marked with * mark:

      number of edges for largest polygon in the sequence*
      common circumradius for all polygons*
      max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
        
Polygons class also has these functions:
      
      __repr__ : function representing the polygon with description of its properties
      __len__ : supports the len() function and returns the total length of sequence
      __iter__ : function returns an iterator and enables the class to be iterable
      __getitem__ : this function allows to access elements using index and slicing 

Polygons class also has PolygonIter Iterator class implementing __next__, __iter__.


### **Unit tests**
**test_polygon.py:**


This file contains the following functions to test the functionality developed in _Polygon.py_ and _Polygons.py_.

_**test_readme_exists()**_ : function checks if _README.md_ exists in the repo.

_**test_readme_contents()**_ : function checks if there is sufficient description added to the _README.md_ file.

_**test_readme_proper_description()**_ : function checks if the _README.md_ contains essential keywords in description.

_**test_readme_file_for_formatting()**_ : function verifies if formatting is applied to text in _README.md_.

_**test_indentations()**_ : function verifies if indentations are in line with PEP8 standards.

_**test_function_name_had_cap_letter()**_ : function verifies if naming conventions for functions were maintained.

_**test_polygon_properties()**_ : function verifies if all properties of a known polygon are calculated correctly.

_**test_polygon_invalid_arg_type_or_val_and_provides_relevant_message()**_ : function verifies if all arguments when 
invalid raise proper Value and Type errors respectively with error description.

_**test_polygon_repr()**_ : function verifies if there is proper description added in repr function.

_**test_polygon_equality()**_ : function verifies if equality check based on number of edges and radius of polygon is correct.

_**test_polygon_greater_than()**_ : function verifies if greater than check based on number of edges of polygon is correct.

_**test_poly_seq_max_eff_polygon()**_ : function verifies max efficiency polygon property is calculated correctly.

_**test_polygon_seq_invalid_arg_type_or_val_and_provides_relevant_message()**_ : function verifies if all arguments when 
invalid raise proper Value and Type errors respectively with error description.

_**test_poly_seq_len()**_ : function verifies length of known polygon sequence is calculated correctly.

_**test_polygon_seq_repr()**_ : function verifies if there is proper description added in repr function.

_**test_polygon_seq_is_iterable()**_ : function verifies if there is proper implementation of built in iter() function 
in order to make the class Iterable.

_**test_polygon_seq_has_valid_iterator()**_ : function verifies if there is proper implementation of an Iterator within
the sequence Polygons class.

_**test_polygon_seq_for_loop()**_ : function verifies if there is proper implementation of an Iterator and Iterable for 
the sequence Polygons class and test it with for loop.

_**test_polygon_seq_get_item_and_slicing()**_ : function verifies if builtin getitem function is implemented correctly 
and the slicing is verified.


Link to Deepnote notebook 
https://deepnote.com/project/TSAI-Sess-12-Iterables-and-Iterators-9l0aTI4qQDeem9kPukc4Qg/%2Ftest_modules.ipynb




