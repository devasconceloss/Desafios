from typing import Dict, Any, Union


def notas(*num, status=False):
    """
    Nesta função será lido um número n de notas, sem definir quantidade e será informado a maior, a menor nota e a média
    das notas inseridas.
    :param num: Uma ou mais notas a serem lidas e guardadas no dicionário ficha
    :param status: Se o status for True, será informado a situação da 'turma' em relação a sua média, se for false, esta
    informação será ocultada
    :return: dicionário com total de notas, maior, menor, média e status
    """
    ficha: Dict[str, Union[Union[int, float, str], Any]] = dict()
    ficha['Total'] = len(num)
    ficha['Maior'] = max(num)
    ficha['Menor'] = min(num)
    ficha['Média'] = sum(num)/len(num)
    if status:
        if ficha['Média'] >= 6 and ficha['Média'] <= 7:
            ficha['Situação'] = 'razoavél'
        if ficha['Média'] > 7:
            ficha['Situação'] = 'Boa'
        if ficha['Média'] < 6:
            ficha['Situação'] = 'Ruim'
    print(ficha)


notas(10, 3, 4, 8, status=True)

notas(3, 4, 5, 7, 10, 0)
