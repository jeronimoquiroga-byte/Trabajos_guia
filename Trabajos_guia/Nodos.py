class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

nodo_1 = Node ("H")
nodo_2 = Node ("D")
nodo_3 = Node ("M") 

nodo_1.left = nodo_2
nodo_1.right = nodo_3

print (nodo_1.value, nodo_1.left.value, nodo_1.right.value)


from logging import root
from symtable import Class
from typing import Any


class BinaryTree():

    def __init__(self):
        self.root = Node(None)

    def insert_node(self, root, value: Any) -> None:

       def __insert_node (root, value):
            if root is None:
                print ("Lugar vacio insertar", value)
                root = Node(value)
                return root
            
            elif value < root.value:
                 #print ("Ir a la izquierda de", root.value)
                 root.left = __insert_node(root.left, value)
            else:
                #print ("Ir a la derecha de", root.value)
                root.right = __insert_node(root.right, value)
            
            return root
            
        self.root = __insert_node(self.root, value)

    def inroden(self) -> None: 
        
        def __inorden(root):
            __inorden(root.left)   #CORREJIR
            print(root.value)
            __inorden(root.right)

        __inorden(self.root)



       

arbol = BinaryTree()

arbol.insert_node("H")
a = input()
arbol.insert_node("D")
a = input()
arbol.insert_node("M")
a = input()
arbol.insert_node("L")
a = input()

print(arbol.root.right.left.value)






