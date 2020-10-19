import requests
from backoff import on_exception, constant
from ratelimit import limits, RateLimitException
import logging

logging.getLogger().setLevel(logging.INFO)


@on_exception(constant, RateLimitException, interval=60, max_tries=3)
@limits(calls=20, period=60)
@on_exception(constant,
              requests.exceptions.HTTPError,
              max_tries=3,
              interval=10)
def get_daily_summary(coin, year, month, day):
    """
    Utiliza API pública do Mercado Bitcoin
    https://www.mercadobitcoin.com.br/api-doc/

    :param coin:  Acrônimo da moeda digital
    :param year, month, day: Respectivamente ano, mês e dia referente ao dia do ano requisitado.
    :return:
    """
    endpoint = f'https://www.mercadobitcoin.net/api/{coin}/day-summary/{year}/{month}/{day}'

    logging.info(f'Getting data from API with: {endpoint}')

    response = requests.get(endpoint)
    response.raise_for_status()

    return response.json()
