def ip_decimal_a_binario(ip_decimal):
    try:
        octetos = ip_decimal.strip().replace(' ', '').split('.')
        if len(octetos) != 4:
            return "❌ Dirección IP inválida. Debe tener 4 octetos."

        octetos_binarios = []
        for octeto in octetos:
            valor = int(octeto)
            if 0 <= valor <= 255:
                octetos_binarios.append(format(valor, '08b'))
            else:
                return "❌ Cada octeto debe estar entre 0 y 255."

        return '✅ ' + '.'.join(octetos_binarios)

    except ValueError:
        return "❌ Entrada inválida. Asegúrese de ingresar solo números."

def ip_binario_a_decimal(ip_binaria):
    try:
        octetos = ip_binaria.strip().replace(' ', '').split('.')
        if len(octetos) != 4:
            return "❌ Dirección IP binaria inválida. Debe tener 4 octetos."

        octetos_decimales = []
        for octeto in octetos:
            if len(octeto) != 8 or any(c not in '01' for c in octeto):
                return "❌ Cada octeto binario debe tener 8 bits y contener solo 0 o 1."
            octetos_decimales.append(str(int(octeto, 2)))

        return '✅ ' + '.'.join(octetos_decimales)

    except ValueError:
        return "❌ Entrada inválida. Verifique el formato binario."

def menu():
    while True:
        print("\n=== 🌐 Conversor de Direcciones IP ===")
        print("1️⃣  Convertir IP decimal a binaria")
        print("2️⃣  Convertir IP binaria a decimal")
        print("3️⃣  Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            ip = input("Ingrese la dirección IP en decimal (ej: 192.168.1.1): ")
            resultado = ip_decimal_a_binario(ip)
            print("Resultado:", resultado)

        elif opcion == "2":
            ip = input("Ingrese la dirección IP en binario (ej: 11000000.10101000.00000001.00000001): ")
            resultado = ip_binario_a_decimal(ip)
            print("Resultado:", resultado)

        elif opcion == "3":
            print("👋 Saliendo del conversor...")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
