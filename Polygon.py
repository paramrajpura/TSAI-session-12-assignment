import math

MIN_NUM_EDGES = 3


class Polygon:
	def __init__(self, edges: int, radius: float):
		# Validate the edges and radius
		self.num_edges = edges
		self.cir_radius = radius

	@property
	def num_edges(self):
		return self._num_edges

	@num_edges.setter
	def num_edges(self, num_edges):
		if not isinstance(num_edges, int):
			raise TypeError(f' num_edges is of type: {type(num_edges)} instead of type: int')
		if num_edges >= MIN_NUM_EDGES:
			self._num_edges = num_edges
			self._interior_angle = None
			self._angle_rad = None
			self._edge_length = None
			self._apothem = None
			self._area = None
			self._perimeter = None
		else:
			raise ValueError(f'num_edges in polygon must be >= {MIN_NUM_EDGES}')

	@property
	def cir_radius(self):
		return self._cir_radius

	@cir_radius.setter
	def cir_radius(self, radius):
		if not (isinstance(radius, float) or isinstance(radius, int)):
			raise TypeError(f' radius is of type: {type(radius)} instead of type: int/float')
		if radius > 0:
			self._cir_radius = radius
			self._edge_length = None
			self._apothem = None
			self._area = None
			self._perimeter = None
		else:
			raise ValueError(f'radius of polygon must be > 0')

	@property
	def num_vertices(self):
		return self.num_edges

	@property
	def interior_angle(self):
		if self._interior_angle is None:
			self._interior_angle = ((self.num_edges - 2) * 180) / self.num_edges
		return self._interior_angle

	@property
	def angle_rad(self):
		if self._angle_rad is None:
			self._angle_rad = math.pi/self.num_edges
		return self._angle_rad

	@property
	def edge_length(self):
		if self._edge_length is None:
			self._edge_length = 2 * self.cir_radius * math.sin(self.angle_rad)
		return self._edge_length

	@property
	def apothem(self):
		if self._apothem is None:
			self._apothem = self.cir_radius * math.cos(self.angle_rad)
		return self._apothem

	@property
	def area(self):
		if self._area is None:
			self._area = (self.num_edges * self.edge_length * self.apothem) / 2
		return self._area

	@property
	def perimeter(self):
		if self._perimeter is None:
			self._perimeter = self.num_edges * self.edge_length
		return self._perimeter

	def __repr__(self):
		return f'Polygon with {self.num_edges} edges and circum-radius = {self.cir_radius}'

	def __eq__(self, other):
		# check the type before comparing with Polygon
		if not isinstance(other, Polygon):
			raise TypeError(f"Argument passed is of type:{type(other)}, required type: Polygon")
		if (other.num_edges == self.num_edges) and (other.cir_radius == self.cir_radius):
			return True
		else:
			return False

	def __gt__(self, other):
		# check the type before comparing with Polygon
		if not isinstance(other, Polygon):
			raise TypeError(f"Argument passed is of type:{type(other)}, required type: Polygon")
		if self.num_edges > other.num_edges:
			return True
		else:
			return False


