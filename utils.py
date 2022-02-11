from requests import get


def currency_rates(code: str) -> float:
    code = code.upper()
    link = get('http://www.cbr.ru/scripts/XML_daily.asp')
    decoder = link.content.decode(encoding=link.encoding)
    result = None
    if code not in decoder:
        return result
    else:
        value = decoder.split('<Valute ID=')
        for elem in value:
            if code in elem:
                result_value = float(elem.replace('/', '').split('<Value>')[-2].replace(',', '.'))
                return f'{result_value} руб.'
