class Tree:
	def __init__(self, appearance, letter, leftChild=None, rightChild=None):
		self.appearance = appearance
		self.letter = letter
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.code = ''

def createTree(file):
	appearances = countAppearances(file)
	leavesTab = []

	for i, j in appearances.items():
		leavesTab.append(Tree(j, i))

	while len(leavesTab) > 1:
		HeapSort(leavesTab)

		leftChild = leavesTab[0]
		rightChild = leavesTab[1]
		leftChild.code = 0
		rightChild.code = 1

		newLeaf = Tree(leftChild.appearance + rightChild.appearance, leftChild.letter + rightChild.letter, leftChild, rightChild)

		leavesTab.remove(leftChild)
		leavesTab.remove(rightChild)
		leavesTab.append(newLeaf)
	return leavesTab

def countAppearances(file):
	txt = open(file, 'r').read()
	dict = {}
	for char in txt:
		if char in dict:
			dict[char] += 1
		else:
			dict[char] = 1
	return dict

def Heapify(tab, i, size):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i

	if l < size and tab[l].appearance > tab[largest].appearance:
		largest = l
	if r < size and tab[r].appearance > tab[largest].appearance:
		largest = r

	if largest != i:
		tab[i], tab[largest] = tab[largest], tab[i]
		Heapify(tab, largest, size)

def HeapSort(tab):
	size = len(tab)

	for i in range(size // 2 - 1, -1, -1):
		Heapify(tab, i, size)

	for i in range(size - 1, 0, -1):
		tab[i], tab[0] = tab[0], tab[i]
		Heapify(tab, 0, i)

def encode(leaf, str, txt):
	leftCode = "0"
	rightCode = "1"
	if leaf is None:
		return txt
	if leaf:
		if len(leaf.letter) <= 1:
			txt = txt.replace(leaf.letter, str)
	txt = encode(leaf.leftChild, str + leftCode, txt)
	txt = encode(leaf.rightChild, str + rightCode, txt)
	return txt

def dictionary(leaf, value=''):
	f = open("output.txt", 'a')
	newCode = value + str(leaf.code)

	if leaf.leftChild:
		dictionary(leaf.leftChild, newCode)
	if leaf.rightChild:
		dictionary(leaf.rightChild, newCode)
	if not leaf.leftChild and not leaf.rightChild:
		f.writelines(" " + leaf.letter + "     -->     " + newCode + "\n")

def saveTreeToFile(tree, destination):
	f = open(destination, 'w')
	f.writelines(" Word: " + open("input.txt", 'r').read() + "\n")
	f.writelines(" Code: " + encode(tree[0], "", open("input.txt", 'r').read()) + "\n")
	f.writelines(" Char | Huffman code " + "\n" + "-------------------" + "\n")
	f.close()
	dictionary(tree[0])

tree = createTree("input.txt")
saveTreeToFile(tree, "output.txt")