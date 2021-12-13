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
    #makeing the piroty qeue
	def makeque(self, frequency):
		for key in frequency:
			node = self.HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)
            #building the huffman tree
	def hufftree(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = self.HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)

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


