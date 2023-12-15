from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreatoranomaly import BodyCreatorAnomalyPost

failureMessage = "Resultado diferente do esperado"
load_dotenv()


class CargaApiMonitoramentoOnelog(HttpUser):
    host = os.environ["IP_ONELOG_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_post_anomaly = os.environ["PREFIX_POST_ANOMALY"]

    # token_apim_prd = os.environ["TOKEN_APIM_PRD"]

    @tag('test1')
    @task
    def create_generic_anomaly(self):
        consult_onelog_endpoint = f"{self.prefix_post_anomaly}"
        body = BodyCreatorAnomalyPost.create_default_post_anomaly()

        # Subscription key APIM-PRD:
        # self.client.headers['Ocp-Apim-Subscription-Key'] = f'{self.token_apim_prd}'
        with self.client.post(url=consult_onelog_endpoint,
                              name="CargaApiOnelogAnomaly - Gera anomalias genericas",
                              catch_response=True, json=body) as response:
            print(body)

            if response.status_code == 200:
                resposta = response.json()
                print(resposta)

                if resposta['currentPage'] > 0:
                    print(
                        f"---- SUCESSO NA INSERÇÃO ----\n Anomalias: "
                        f"{resposta['totalRegisters']} \nSTATUS CODE: {response.status_code}")

                else:
                    print(
                        f"---- FALHA NA INSERÇÃO ----\n {response.text} \n "
                        f"STATUS CODE: {response.status_code} \n {body}")
                    response.failure(
                        failureMessage + f" Status CODE: {response.status_code}"
                    )
            else:
                print(
                    f"---- FALHA NO POST ----\n {response.text} \n STATUS CODE: {response.status_code}")
                response.failure(
                    failureMessage + f" Status CODE: {response.status_code}"
                )

    @tag('test2')
    @task
    def get_all_anomaly(self):
        consult_onelog_endpoint = f"{self.prefix_post_anomaly}"
        body_get = BodyCreatorAnomalyPost.create_default_get_anomaly()

        # Subscription key APIM-PRD:
        # self.client.headers['Ocp-Apim-Subscription-Key'] = f'{self.token_apim_prd}'
        with self.client.get(url=consult_onelog_endpoint,
                             name="CargaApiOnelogAnomaly - Retorna todas anomalias",
                             catch_response=True, json=body_get) as response:
            print(body_get)

            if response.status_code == 200:
                resposta = response.json()

                if resposta['registers']:
                    for register in resposta['registers']:
                        if 'id' in register and register['id'] is not None:
                            print(
                                f"---- SUCESSO NA CONSULTA ----\n Anomalias: "
                                f"{register['id']} \n STATUS CODE: {response.status_code}")

                else:
                    print(
                        f"---- FALHA NA CONSULTA ----\n {response.text} \n "
                        f"STATUS CODE: {response.status_code} \n {body_get}")
                    response.failure(
                        failureMessage + f" Status CODE: {response.status_code}"
                    )
            else:
                print(
                    f"---- FALHA NO GET ----\n {response.text} \n STATUS CODE: {response.status_code}")
                response.failure(
                    failureMessage + f" Status CODE: {response.status_code}"
                )
