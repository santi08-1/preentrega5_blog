from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag

if __name__ == "__main__":
    while True:
        opcion_elegida = mostrar_menu()
        
        try:
            opcion_num = int(opcion_elegida)
            
            if opcion_num == 1:
                print("Opción 1 seleccionada")
                listar_posts(posts)
            elif opcion_num == 2:
                print("Opción 2 seleccionada")
                termino = input("Ingresá el título a buscar: ")
                buscar_por_titulo(posts, termino)
            elif opcion_num == 3:
                print("Opción 3 seleccionada")
                tag = input("Ingresá el tag a filtrar: ")
                filtrar_por_tag(posts, tag)
            elif opcion_num == 4:
                print("¡Hasta luego! Gracias por usar el sistema del blog.")
                break
            else:
                print("Opción inválida. Por favor, elige un número del 1 al 4.")
                
        except ValueError:
            print("Debes ingresar un número válido (1-4), no letras ni símbolos.")