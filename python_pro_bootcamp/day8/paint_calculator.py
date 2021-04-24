def paint_calc(height,width,cover):
	paint=(height*width)/cover
	return paint

height_wall=float(input('Height of wall: '))
width_wall=float(input('Width of wall: '))
coverage=float(input('Coverage of wall: '))

print(f"You'll need {round(paint_calc(height=height_wall,width=width_wall,cover=coverage))} cans of paint.")
