А = 0
В = 0
С = 0

def on_forever():
    global А, В, С
    Текущая_широта = 0
    Текущая_широта_цели = 0
    Текущая_долгота = 0
    Текущая_долгота_цели = 0
    if Текущая_долгота_цели > Текущая_долгота and Текущая_широта_цели > Текущая_широта:
        А = Текущая_широта_цели - Текущая_широта
        В = Текущая_долгота_цели - Текущая_долгота
        С = А / В
    elif Текущая_долгота_цели > Текущая_долгота and Текущая_широта_цели < Текущая_широта:
        А = Текущая_широта - Текущая_широта_цели
        В = Текущая_долгота_цели - Текущая_долгота
        С = А / В
    elif Текущая_долгота_цели < Текущая_долгота and Текущая_широта_цели < Текущая_широта:
        А = Текущая_долгота - Текущая_долгота_цели
        В = Текущая_широта - Текущая_широта_цели
        С = А / В
    else:
        А = Текущая_широта_цели - Текущая_широта
        В = Текущая_долгота - Текущая_долгота_цели
        С = А / В
basic.forever(on_forever)