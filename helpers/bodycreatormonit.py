from random import choice


class BodyCreatorMonit:

    @staticmethod
    def create_default_monit_body(null=None):
        DATA_INICIO = "2023-09-01T20:56:25.638Z"
        DATA_FIM = "2023-09-01T20:56:25.638Z"
        LOGISTICA = "distribuicao"
        ULTIMA_MSG = "1970-01-01T00:00:00.000Z"

        body = {
            "dataEntregaInicio": DATA_INICIO,
            "dataEntregaFim": DATA_FIM,
            "logistica": LOGISTICA,
            "ultimaDataMensagemLida": ULTIMA_MSG
        }

        return body
