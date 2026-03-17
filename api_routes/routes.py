import requests
from flask import request

base_url = "https://api.thecatapi.com/v1"
def get_gatos():
    url = f"{base_url}/breeds"

    headers = {

        "x-api-key": "live_Uxfa1Bzyqoliroesb8Mpg8YOWsWnXHUCv2Lr8dlGYoq1NEY9eCIorAAmatE8Ln9P"


    }

    resposta = requests.get(url, headers=headers)

    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)


    return resposta.json()[0]

