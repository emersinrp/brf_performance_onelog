from locust import between, task, HttpUser, tag
import os
from dotenv import load_dotenv
from helpers.bodycreatormonit import BodyCreatorMonit

failureMessage = "Não foi possível acessar ou visualizar o valor de total"
load_dotenv()


class CargaApiMonitoramentoOnelog(HttpUser):
    host = os.environ["IP_ONELOG_QAS"]
    wait_time = between(1.0, 3.0)
    prefix_monitoramento = os.environ["PREFIX_MONITORAMENTO"]
    token_apim_prd = os.environ["TOKEN_APIM_PRD"]

    @tag('test1')
    @task
    def retorno_monitoramento_filtro_data(self):
        consult_onelog_endpoint = f"{self.prefix_monitoramento}"
        body = BodyCreatorMonit.create_default_monit_body()

        # Subscription key APIM-PRD:
        # self.client.headers['Ocp-Apim-Subscription-Key'] = f'{self.token_apim_prd}'
        with self.client.post(url=consult_onelog_endpoint,
                              name="CargaApiOnelog - Retorna monitoramento c/ filtro data",
                              catch_response=True, json=body) as response:

            if response.status_code == 200:
                resposta = response.json()

                if resposta['total']['viagensProgramadas'] > 0:
                    print(
                        f"---- SUCESSO NA CONSULTA ----\n Viagens Programadas: {resposta['total']['viagensProgramadas']} \n STATUS CODE: {response.status_code}")

                else:
                    print(
                        f"---- FALHA NA CONSULTA ----\n {response.text} \n STATUS CODE: {response.status_code}")
                    response.failure(
                        failureMessage + f" Status CODE: {response.status_code}"
                    )
            else:
                print(
                    f"---- FALHA NA CONSULTA ----\n {response.text} \n STATUS CODE: {response.status_code}")
                response.failure(
                    failureMessage + f" Status CODE: {response.status_code}"
                )
