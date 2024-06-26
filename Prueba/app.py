import os
from pathlib import Path
#from modules.costruccion import menup, ans, ver
#from modules.eliminar import eliminar
#from modules.exportar import exportar
from modules.agregar import agregar_pintura
pinturas = {'codigo':'380560',
            'nombre':'Azul',
            'tipo':'latex',
            'valor': '13999',
            'stock':'10'}

menup = ['Ver listado de pinturas',
         'Buscar pintura',
         'Agregar pintura',
         'Eliminar pintura',
         'Exportar pnturas']
ruta = Path('D:/carpeta.json')
while True:
    for i, opt in enumerate(menup, start=1):
        print(f'{i}. {opt}')
    ans = input('Ingrese una opcion\n')
    if ans == '1':
        pass
    elif ans == '2':
        pass
    elif ans == '3':
        agregar_pintura()
    elif ans == '4':
        pass
    elif ans == '5':
        pass
    else:
        os.system('cls')
        print('Opcion invalida')