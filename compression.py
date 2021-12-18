import heapq
import os



class huffmancode:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

	class HeapNode:
		def __init__(self, char, freq):
			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		def __lt__(self, other):
			return self.freq < other.freq

		def __eq__(self, other):
			if(other == None):
				return False
			if(not isinstance(other, HeapNode)):
				return False
			return self.freq == other.freq

	
    #makeing a ther frequncy dectionary 
	def char_freq(self, xml_data):
		frequency = {}
		for character in xml_data:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1
		return frequency
 

    #makeing the binary codes for each char
	def char_codes_2(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.char_codes_2(root.left, current_code + "0")
		self.char_codes_2(root.right, current_code + "1")


	def char_codes(self):
		root = heapq.heappop(self.heap)
		current_code = ""
		self.char_codes_2(root, current_code)
   #replaceing the char with the codes
	def encoder_data(self, xml_data):
		encoded_text = ""
		for character in xml_data:
			encoded_text += self.codes[character]
		return encoded_text

    #adding a padding so they can be mulitple of 8
	def padded_encode_data(self, encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


	def byte_array(self, padded_encoded_text):
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b


	def compress(self):
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			xml_data = file.read()
			xml_data = xml_data.rstrip()

			frequency = self.char_freq(xml_data)

                        #makeing the piroty qeue
			for key in frequency:
				node = self.HeapNode(key, frequency[key])
				heapq.heappush(self.heap, node)


                       #building the huffman tree
			while(len(self.heap)>1):
				node1 = heapq.heappop(self.heap)
				node2 = heapq.heappop(self.heap)

				merged = self.HeapNode(None, node1.freq + node2.freq)
				merged.left = node1
				merged.right = node2

				heapq.heappush(self.heap, merged)
			self.char_codes()

			encoded_text = self.encoder_data(xml_data)
			padded_encoded_text = self.padded_encode_data(encoded_text)

			b = self.byte_array(padded_encoded_text)
			output.write(bytes(b))

		print("Compressed")
		return output_path





