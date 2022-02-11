from requests import get


def currency_rates(code: str) -> float:
    link = get('http://www.cbr.ru/scripts/XML_daily.asp')
    decoder = link.content.decode(encoding=link.encoding)
    result = None
    if code not in decoder:
        return result
    else:
        value = decoder.split('<Valute ID=')
        for elem in value:
            if code.upper() in elem:
                return float(elem.replace('/', '').split('<Value>')[-2].replace(',', '.'))


print(currency_rates('USD'))
print(currency_rates('noname'))
