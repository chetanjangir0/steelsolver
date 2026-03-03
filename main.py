from loading import Loading
from staad_writer import StaadModel

span = 20
height = 6
slope = 10

model = StaadModel()

model.add_node(1, 0, 0, 0) # base left
model.add_node(2, span, 0, 0) # base right
model.add_node(3, 0, height, 0) # eave left
model.add_node(4, span, height, 0) # eave right
model.add_node(5, span / 2, height + (span/(2*slope)), 0) # ridge

model.add_member(1, 1, 3)
model.add_member(2, 2, 4)
model.add_member(3, 3, 5)
model.add_member(3, 4, 5)

model.set_fixed_supports([1, 2])

loading = Loading()
loading.add_selfweight()

model.set_load_block(loading.generate())

model.write("portal.std")
