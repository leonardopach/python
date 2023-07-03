# from sys import path
# from packagee.module import soma_do_modulo
# from packagee import module
# # from packagee.module import *

# print(__name__)
# print(*path, sep="\n")
# print(soma_do_modulo(10, 2))
# print(module.soma_do_modulo(10, 2))
# # print(variavel)

from packagee import module, module_b

print(module.soma_do_modulo(2, 2))
module_b.qualquer_valor()
