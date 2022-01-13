from Polygon import Polygon, MIN_NUM_EDGES


class Polygons:

    def __init__(self, max_num_edges, cir_rad):
        self.max_num_edges = max_num_edges
        self.cir_radius = cir_rad

    @property
    def max_num_edges(self):
        return self._max_num_edges

    @max_num_edges.setter
    def max_num_edges(self, max_edges):
        if not isinstance(max_edges, int):
            raise TypeError(f' max_edges is of type: {type(max_edges)} instead of type: int')
        if max_edges >= MIN_NUM_EDGES:
            self._max_num_edges = max_edges
            self._max_eff_polygon = None
        else:
            raise ValueError(f'max_edges in polygon must be >= {MIN_NUM_EDGES}')

    @property
    def cir_radius(self):
        return self._cir_radius

    @cir_radius.setter
    def cir_radius(self, radius):
        if not (isinstance(radius, float) or isinstance(radius, int)):
            raise TypeError(f' radius is of type: {type(radius)} instead of type: int/float')
        if radius > 0:
            self._cir_radius = radius
            self._max_eff_polygon = None
        else:
            raise ValueError(f'radius of polygon must be > 0')

    @property
    def max_eff_polygon(self):
        if self._max_eff_polygon is None:
            self._max_eff_polygon = Polygon(edges=self.max_num_edges, radius=self.cir_radius)
        return self._max_eff_polygon

    def __iter__(self):
        return self.PolygonIter(self.max_num_edges, self.cir_radius)

    class PolygonIter:
        def __init__(self, max_num_edges, cir_rad):
            self.n_edges = MIN_NUM_EDGES
            self.radius = cir_rad
            self.max_edges = max_num_edges

        def __iter__(self):
            return self

        def __next__(self):
            if self.n_edges > self.max_edges:
                raise StopIteration
            next_poly = Polygon(edges=self.n_edges, radius=self.radius)
            self.n_edges += 1
            return next_poly

    def __getitem__(self, item):
        if isinstance(item, int):
            # single item requested
            if item < 0:
                item = self._max_num_edges - MIN_NUM_EDGES + 1 + item
            if item < 0 or item > self._max_num_edges - 1:
                raise IndexError
            return Polygon(edges=MIN_NUM_EDGES + item, radius=self._cir_radius)
        else:
            # handling for slice
            print(f'requesting [{item.start}:{item.stop}:{item.step}]')
            idx = item.indices(self._max_num_edges - MIN_NUM_EDGES + 1)
            rng = range(idx[0] + MIN_NUM_EDGES, idx[1] + MIN_NUM_EDGES, idx[2])
            return [Polygon(edges=n, radius=self._cir_radius) for n in rng]

    def __len__(self):
        return self._max_num_edges - MIN_NUM_EDGES + 1

    def __repr__(self):
        return f'A polygon sequence with num_edges = {[i for i in range(MIN_NUM_EDGES,self._max_num_edges+1)]} and ' \
               f'circum-radius = {self._cir_radius}'
