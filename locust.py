from locust import HttpUser, task


class Test(HttpUser):

    @task
    def listado_productos(self):
        self.client.request(method="GET", url="/banco-azteca/adquirente/acepta-pagos/comercios/v1/comercios/2208172622/productos?no-pagina=1&no-items=10",
                            headers={"Authorization": "Bearer 6oXj6GMd0G28jiBTHoOTKDw1liAw",
                                     "x-idAcceso": "2209022204545248",
                                     "x-usuario": "2208172723",
                                     "x-sesion": "1df81eb3d3574c8d8058",
                                     }
                             )