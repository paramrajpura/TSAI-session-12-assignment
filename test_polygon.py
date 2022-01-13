from Polygon import Polygon
from Polygons import Polygons
from datetime import datetime
import pytest
from io import StringIO
import sys, math
import time, re
import inspect
import os

README_CONTENT_CHECK_FOR = [
    "polygon",
    "iterable",
    "iterator",
    "next",
    "iter",
    "getitem",
    "edges",
    "vertices",
    "class",
    "repr",
    "len",
    "apothem",
    "angle",
    "sequence",
    "setter",
    "init"
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Polygon, inspect.isfunction)
    functions.extend(inspect.getmembers(Polygons, inspect.isfunction))
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_polygon_properties():
    tri = Polygon(edges=3, radius=2)
    assert tri.num_edges == 3
    assert tri.cir_radius == 2
    assert tri.angle_rad == math.pi / 3
    assert tri.edge_length == 2 * 2 * math.sin(math.pi / 3)
    assert tri.apothem == 2 * math.cos(math.pi / 3)
    assert tri.interior_angle == ((3 - 2) * 180) / 3
    assert tri.area == (3 * 2 * 2 * math.sin(math.pi / 3) * 2 * math.cos(math.pi / 3)) / 2
    assert tri.perimeter == 3 * 2 * 2 * math.sin(math.pi / 3)


def test_polygon_invalid_arg_type_or_val_and_provides_relevant_message():
    with pytest.raises(TypeError, match=r".*int.*"):
        poly = Polygon(edges='abc', radius=2)
    with pytest.raises(TypeError, match=r".*float.*"):
        poly = Polygon(edges=3, radius='abc')
    with pytest.raises(ValueError, match=r".*>= 3.*"):
        poly = Polygon(edges=2, radius=2)
    with pytest.raises(ValueError, match=r".*> 0.*"):
        poly = Polygon(edges=3, radius=-1)


def test_polygon_repr():
    n_edges = 3
    rad = 2
    tri = Polygon(edges=n_edges, radius=rad)
    assert tri.__repr__() == f'Polygon with {n_edges} edges and circum-radius = {rad}', \
        'The representation of the Polygon object does not meet expectations'


def test_polygon_equality():
    tri = Polygon(edges=3, radius=5)
    another_triangle = Polygon(edges=3, radius=5)
    assert tri == another_triangle, "equality check of two triangles failed"

    square = Polygon(edges=4, radius=5)
    assert tri != square, "Triangle and Square cant be equal polygons"


def test_polygon_greater_than():
    tri = Polygon(edges=3, radius=5)
    square = Polygon(edges=4, radius=5)
    assert square > tri, "Square should be greater than triangle for polygon comparison"


def test_poly_seq_max_eff_polygon():
    seq = Polygons(max_num_edges=6, cir_rad=2)
    hexagon = Polygon(edges=6, radius=2)
    assert seq.max_eff_polygon == hexagon, "Polygon sequence max efficiency polygon check failed"


def test_polygon_seq_invalid_arg_type_or_val_and_provides_relevant_message():
    with pytest.raises(TypeError, match=r".*int.*"):
        poly = Polygons(max_num_edges='abc', cir_rad=2)
    with pytest.raises(TypeError, match=r".*float.*"):
        poly = Polygons(max_num_edges=3, cir_rad='abc')
    with pytest.raises(ValueError, match=r".*>= 3.*"):
        poly = Polygons(max_num_edges=2, cir_rad='abc')
    with pytest.raises(ValueError, match=r".*> 0.*"):
        poly = Polygons(max_num_edges=3, cir_rad=0)


def test_poly_seq_len():
    seq = Polygons(max_num_edges=6, cir_rad=2)
    assert len(seq) == 4, "Length of polygon sequence is incorrect!"


def test_polygon_seq_repr():
    seq = Polygons(max_num_edges=6, cir_rad=2)
    assert "polygon sequence" in seq.__repr__(), 'The representation of the Polygon seq does not meet expectations'


def test_polygon_seq_is_iterable():
    seq = Polygons(max_num_edges=6, cir_rad=2)
    assert '__iter__' in dir(seq), 'The sequence doesnt have an __iter__ function, hence is not iterable!'


def test_polygon_seq_has_valid_iterator():
    seq = Polygons(max_num_edges=6, cir_rad=2)
    itr_seq = iter(seq)
    assert '__next__' in dir(itr_seq), 'The sequence iterator doesnt have a __next__ function, hence not a ' \
                                       'valid iterator!'
    assert '__iter__' in dir(itr_seq), 'The sequence iterator doesnt have an __iter__ function, hence not a ' \
                                       'valid iterator!'


def test_polygon_seq_for_loop():
    rad = 2
    seq = Polygons(max_num_edges=6, cir_rad=rad)
    n = 3
    for poly in seq:
        assert poly == Polygon(edges=n, radius=rad)
        n += 1


def test_polygon_seq_get_item_and_slicing():
    seq = Polygons(max_num_edges=6, cir_rad=2)
    assert '__getitem__' in dir(seq), 'The sequence iterator doesnt have a __getitem__ function, hence not a ' \
                                      'valid iterable!'
    assert seq[0] == Polygon(edges=3, radius=2), "Item extracted from poly seq using __getitem__ is not correct!"
    assert len(seq[:3]) == 3, "Slice extracted from poly seq using __getitem__ is not correct!"
