productos = []

while True:
    print('\033[1m\033[34m' + '='*40 + '\033[0m')
    print('\033[1m\033[34mSistema de gestión de productos\033[0m')
    print('\033[1m\033[34m' + '='*40 + '\033[0m')
    print('''
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Eliminar producto
    5. Salir''')

    opcion = input('\033[1mSeleccione una opción (1-5): \033[0m').strip()

    if opcion == '1':
        print('\033[1mAgregar producto\033[0m')

        nombre = input('Nombre del producto: ').strip()
        while nombre == '':
            print('El nombre del producto no puede estar vacío.')
            nombre = input('Nombre del producto: ').strip()

        categoria = input('Categoría del producto: ').strip()
        while categoria == '':
            print('La categoría no puede estar vacía.')
            categoria = input('Categoría del producto: ').strip()

        precio_str = input('Precio del producto (sin centavos): ').strip()
        while not precio_str.isdigit():
            print('El precio del producto debe ser positivo y sin centavos.')
            precio_str = input('Precio del producto (sin centavos): ').strip()
        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)

    elif opcion == '2':
        print('\033[1m' + '--- Lista de productos ---' + '\033[0m')
        
        if len(productos) == 0:
            print('No hay productos registrados.')
        else:
            for i in range(len(productos)):
                print(f'{i+1} -Nombre: {productos[i][0]}\n -Categoría: {productos[i][1]}\n -Precio: ${productos[i][2]} ')

    elif opcion == '3':
        print('\033[1mBuscar producto\033[0m')
        
        if len(productos) == 0:
            print('No hay productos registrados.')
            print('Elegí la opción 1 para agregar productos.')
        else:
            busqueda = input('Ingrese el nombre del producto a buscar: ').strip().lower()
            encontrados = []
            while busqueda== '':
                        print('Error: escribí algo para buscar.')
                        busqueda = input('Ingrese el nombre del producto a buscar: ').strip().lower()
            for producto in productos:
                if busqueda in producto[0].lower():
                    encontrados.append(producto)
            if encontrados:
                print('--- Productos encontrados ---')
                for i, producto in enumerate(encontrados, start=1):
                    print(f'{i} - Nombre: {producto[0]}\n   Categoría: {producto[1]}\n   Precio: ${producto[2]} ')
            else:
                print('No se encontraron productos con ese nombre.')
    elif opcion == '4':
            print('\033[1m' + '--- Eliminar producto ---' + '\033[0m)')
            if len(productos) == 0:
                print('No hay productos registrados.')
            else:
                nombre = input('Ingrese el nombre del producto a eliminar: ').strip().lower()
                eliminados = []
                for i in range(len(productos)-1, -1, -1):
                    if nombre in productos[i][0].lower():
                        eliminados.append(productos[i])
                        del productos[i]
                if eliminados:
                    print(f'Se eliminaron {len(eliminados)} producto(s).')
                else:
                    print('No se encontró ningún producto con ese nombre.')

    elif opcion == '5':
        print('\033[1mSaliendo del sistema...\033[0m')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 5.')
