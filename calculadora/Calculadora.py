class Calculadora:

    def __init__(self, impuesto_base: float = 21.0):
        self.impuesto_base = impuesto_base
    
    def calcularTotal(self, precio: float, descuento: float = 0.0) -> float:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        precioRebajado = precio * (1 - (descuento / 100))
        total = precioRebajado * (1 + (self.impuesto_base / 100))

        return round(total, 2)
    
if __name__ == "__main__":
    calcTest = Calculadora()
    print(f"Prueba interna: {calcTest.calcularTotal(100, 10)}")    