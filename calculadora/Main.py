from Calculadora import Calculadora

def ejecutar_aplicacion():

    mi_calculadora = Calculadora(impuesto_base=21.0)
    
    productos = [
        {"nombre": "Laptop", "precio": 1200, "desc": 10},
        {"nombre": "Mouse", "precio": 25, "desc": 0},
        {"nombre": "Monitor", "precio": 300, "desc": 15}
    ]

    print("--- RECIBO DE COMPRA ---")
    for p in productos:
        try:
            total = mi_calculadora.calcularTotal(p["precio"], p["desc"])
            print(f"{p['nombre']}: ${total} (IVA incluido)")
        except ValueError as e:
            print(f"Error en {p['nombre']}: {e}")

if __name__ == "__main__":
    ejecutar_aplicacion()