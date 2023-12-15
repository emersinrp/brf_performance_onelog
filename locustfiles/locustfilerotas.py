from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreatorrotas import BodyCreatorRotasGet

failureMessage = "Resultado diferente do esperado"
load_dotenv()


class CargaApiMonitoramentoOnelog(HttpUser):
    host = os.environ["IP_ONELOG_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_post_anomaly = os.environ["PREFIX_ROTAS"]

    # token_apim_prd = os.environ["TOKEN_APIM_PRD"]

    @tag('test1')
    @task
    def create_generic_anomaly(self):
        consult_onelog_endpoint = f"{self.prefix_post_anomaly}"
        body = BodyCreatorRotasGet.create_default_body_rotas()

        # Subscription key APIM-PRD:
        # self.client.headers['Ocp-Apim-Subscription-Key'] = f'{self.token_apim_prd}'
        with self.client.post(url=consult_onelog_endpoint,
                              name="CargaApiOnelogRotas - Retorna rotas criadas por placa",
                              catch_response=True, json=body) as response:
            print(body)

            if response.status_code == 200:
                resposta = response.json()
                print(resposta)

                if resposta['currentPage'] > 0:
                    print(
                        f"---- SUCESSO NA BUSCA ----\n Rotas: "
                        f"{resposta['totalRegisters']} \nSTATUS CODE: {response.status_code}")

                else:
                    print(
                        f"---- FALHA NA BUSCA ----\n {response.text} \n "
                        f"STATUS CODE: {response.status_code} \n {body}")
                    response.failure(
                        failureMessage + f" Status CODE: {response.status_code}"
                    )
            else:
                print(
                    f"---- FALHA NO GET ----\n {response.text} \n STATUS CODE: {response.status_code}")
                response.failure(
                    failureMessage + f" Status CODE: {response.status_code}"
                )
