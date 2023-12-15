from random import choice


class BodyCreatorMonit:

    @staticmethod
    def create_default_monit_body(null=None):
        DATA_INICIO = "2023-12-05T00:56:25.638Z"
        DATA_FIM = "2023-12-05T20:56:25.638Z"
        LOGISTICA = "distribuicao"
        ULTIMA_MSG = "1970-01-01T00:00:00.000Z"
        LIST_UNIDADES = [
            "CD APG",
            "CD BELEM",
            "CD CUIABA",
            "CD FORTALEZA",
            "CD DUQUE DE CAXIAS",
            "CD EMBU",
            "CD FORTALEZA",
            "CD ITAJAI",
            "CD JUNDIAI",
            "CD LONDRINA",
            "CD MANAUS",
            "CD NSR",
            "CD RIBEIRAO DAS NEVES",
            "CD SALVADOR",
            # "CD SAO JOSE DOS PINHAIS", CD indisponivel
            "CD UBERLANDIA",
            "CD VIANA",
            "CD VIDEIRA",
            "CD VISA",
            # "DEPOSITO NAO CADASTRADO", CD indisponivel
            "TSP - PRESIDENTE PRUDENTE",
            "TSP ARACAJU",
            "TSP ARACATUBA",
            "TSP BAURU",
            "TSP BRASILIA",
            "TSP CAMPO GRANDE",
            "TSP CAMPOS DOS GOYTACAZES",
            "TSP DIFAL",
            "TSP FARROUPILHA",
            "TSP GOVERNADOR VALADARES",
            "TSP GUARULHOS",
            "TSP ICARA",
            "TSP ITABUNA",
            "TSP LIMEIRA",
            "TSP MARAU",
            "TSP MARINGA",
            "TSP MONTES CLAROS",
            "TSP NATAL",
            "TSP PALHOÇA",
            "TSP PELOTAS",
            "TSP PONTA GROSSA",
            "TSP POUSO ALEGRE",
            "TSP RIBEIRAO PRETO",
            "TSP SANTA MARIA",
            "TSP SANTA ROSA",
            "TSP SANTOS",
            "TSP SEABRA",
            "TSP SJC",
            "TSP SOROCABA",
            "TSP TOCANTINS",
            "TSPF MACEIO",
            # "TSPF SAO LUIS",
            "TSPF TERESINA",
        ]

        body = {
            "dataEntregaInicio": DATA_INICIO,
            "dataEntregaFim": DATA_FIM,
            "logistica": LOGISTICA,
            "unidade": [choice(LIST_UNIDADES)],
            "ultimaDataMensagemLida": ULTIMA_MSG
        }

        return body
