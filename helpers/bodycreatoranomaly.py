from random import choice


class BodyCreatorAnomalyPost:

    @staticmethod
    def create_default_post_anomaly(null=None):
        PAGES = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        NUMERO_VIAGENS = []
        PLACAS_ALEAT = ["JCG6I55", "RNF2G41", "FZA1479", "CPB4919", "ETU9721", "AVQ1A88", "ITG9E17", "COF1J02",
                        "OYN5H30", "KOB5D18", "POC6E17", "DET9E09", "FWB1H58", "EMU7D21", "PGZ7G05"]
        UNIDADES_CLIENTES = ["CD APG",
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
                             ]
        STATUS_ANOM = [0, 1, 2, 3]
        PRIORIDADE_ANOM = [0, 1, 2]
        TIPOS_ANOM = [0, 1, 2, 3, 6, 8, 9, 10, 11, 12, 19, 20, 21, 22, 23, 24, 25, 26, 28]

        body = {
            "page": choice(PAGES),
            "pageSize": 200,
            "logistica": "distribuicao",
            "placas": [choice(PLACAS_ALEAT)],
            "unidades": [choice(UNIDADES_CLIENTES)],
            "clientes": ["null"],
            "transportadora": ["null"],
            "status": [choice(STATUS_ANOM)],
            "prioridade": [choice(PRIORIDADE_ANOM)],
            "dtCreatedStart": "2023-12-12T15:14:33.4552322Z",
            "tipoAnomalia": [choice(TIPOS_ANOM)]
        }

        return body

    @staticmethod
    def create_default_get_anomaly(null=None):
        PAGES = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        PAGE_SIZE = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200
        STATUS_ANOM = [0, 1, 2, 3]
        PRIORIDADE_ANOM = [0, 1, 2]
        TIPOS_ANOM = [0, 1, 2, 3, 6, 8, 9, 10, 11, 12, 19, 20, 21, 22, 23, 24, 25, 26, 28]
        PLACAS_ALEAT = ["JCG6I55", "RNF2G41", "FZA1479", "CPB4919", "ETU9721", "AVQ1A88", "ITG9E17", "COF1J02",
                        "OYN5H30", "KOB5D18", "POC6E17", "DET9E09", "FWB1H58", "EMU7D21", "PGZ7G05"]

        body_get = {
            "logistica": "distribuicao",
            "page": choice(PAGES),
            "pageSize": choice(PAGE_SIZE),
            "prioridade": [choice(PRIORIDADE_ANOM)],
            "placas": [choice(PLACAS_ALEAT)],
            "status": [choice(STATUS_ANOM)],
            "tipoAnomalia": [choice(TIPOS_ANOM)]
        }

        return body_get
