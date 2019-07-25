from PIL import Image, ImageDraw

class SquareEncoder:
	def __init__(self, text, width, gap = 2):
		self.text = text
		self.width = width
		self.gap = gap
		self.maxWidth = 10 # maximum number of squares per line (99 uses the most, 10)
		self.boxDict = { 1 : (0xc0, 0xc0, 0xc0), 5: (0x66, 0xff, 0xff), 10: (0xff, 0x99, 0x33), 50: (0xff, 0x33, 0x33) }

	def charToBoxes(self, char):
		so = ord(char)
		sc = so
		bx = []
		for i in sorted(self.boxDict.keys(), reverse=True):
			while sc >= i:
				sc -= i
				bx.append(i)
		return bx

	def draw(self, filename = None):
		'''if filename passed, returns true/false, otherwise returns resulting image object'''
		l = len(self.text)
		curx, cury = 0, 0
		im = Image.new('RGB', ( (self.maxWidth + self.gap) * self.width, (l + self.gap) * self.width ), color = 'white')
		id = ImageDraw.Draw(im)

		for ch in self.text:
			bx = self.charToBoxes(ch)
			curx = 0
			for bi in bx:
				id.rectangle( ((curx, cury), (curx+self.width,cury+self.width)), fill=self.boxDict[bi] )
				curx += self.width + self.gap
			cury += self.width + self.gap
		if filename:
			try:
				im.save(filename)
				return True
			except:
				print("Error saving to file: ", sys.exc_info()[0])
				return False
		else:
			return im



if __name__ == "__main__":
	try:
		f = open(__file__)
	except:
		print("Couldn't open myself! ", sys.exc_info()[0])
		sys.exit()
	s = f.read()
	f.close()
	sq = SquareEncoder(s, 8)
	sq.draw("squared.png")
	
