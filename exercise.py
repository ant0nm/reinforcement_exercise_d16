def draw_shape(options):
  shape = ""

  for r in range(options['rows']):
    for c in range(options['cols']):
      shape += options['char']

    shape += "\n"


  return shape


# first argument
print(draw_shape({'rows': 4, 'cols': 4, 'char': '*'}))

# second argument
print(draw_shape({'rows': 3, 'cols': 9, 'char': '0'}))
