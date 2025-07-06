import utils


class LoanSimulator:
    def __init__(
        self,
        loan_det: complex = None,
        total_years_payment = 30,
        house_price: int = 300000
        ):

        self._initial_payment = loan_det.real # Entrada aportada por el cliente
        self._anual_tax = loan_det.imag # Tasa de interés
        self._total_years_payment = total_years_payment # Años del prestamos
        self._house_price = house_price # Precio vivienda

        self._monthly_payment = (loan_det.imag / 12) / 100 # Tasa de interés anual => mensual
        self._payment_num = total_years_payment * 12 # Duración del préstamo en meses
        self._loan = self._house_price - self._initial_payment # Prestamo vivienda
        self._total_payment = 0 # Simulación de la cuota mensual
   

    def total_payment(self):
        # Cuota mensual = prestamo * 
        # (tasa de interés mensual * 
        # (1 + tasa de interés mensual)**número de pagos) / ((1 + tasa de interés mensual)**snúmero de pagos - 1)
        

        self._total_payment = self._loan * (self._monthly_payment * (1 + self._monthly_payment)**self._payment_num) / ((1 + self._monthly_payment)**self._payment_num - 1)


    def print_loan(self):
        print(f"----- Simulación Hipoteca -----\
              \nPara una vivienda de {self._house_price} euros, aportando una entrada de {self._initial_payment} \
              \ny con una tasa de interés del {self._monthly_payment} anual durante {self._total_years_payment} años: \
              \nCuota mensual a pagar: {self._total_payment} euros \
              \n----- Simulación Hipoteca -----")


if __name__ == "__main__":
    # USO
    loan_det = 50000 + 2.5j # Numero complejo: Real = Entrada | Imaginario = interés
    total_years = 30
    house_price = 300000

    loan_sim = LoanSimulator(
        loan_det,
        total_years,
        house_price
    )

    loan_sim.total_payment()
    loan_sim.print_loan()