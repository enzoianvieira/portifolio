import PySimpleGUI as psg

psg.theme('LightGrey')
psg.set_options(font=('Roboto', 12))

layout = [[psg.Text('----------------------- I Menu Calculadora I ----------------------------')],
          [psg.Button('Somar',size=(21, 1)), psg.Button('Subtrair',size=(21, 1))],
          [psg.Button('Multiplicar',size=(21, 1)), psg.Button('Dividir',size=(21, 1))],
          [psg.Button('Sair',size=(45, 1))]]

window = psg.Window('Calculadora', layout, size=(400, 200), background_color='#d1ffc2' )

while True:
    event, values = window.read()

    if event == psg.WIN_CLOSED or event == 'Sair':
        break

    if event in ['Somar', 'Subtrair', 'Multiplicar', 'Dividir']:
        layout = [[psg.Text(f'Digite o primeiro valor para a operação de {event.lower()}:')],
                  [psg.Input(key='-VALOR1-')],
                  [psg.Text(f'Digite o segundo valor para a operação de {event.lower()}:')],
                  [psg.Input(key='-VALOR2-')],
                  [psg.Button('Calcular'), psg.Button('Cancelar')]]

        sub_window = psg.Window(f'{event} - Digite os valores', layout)

        while True:
            sub_event, sub_values = sub_window.read()

            if sub_event == psg.WIN_CLOSED or sub_event == 'Cancelar':
                break

            if sub_event == 'Calcular':
                try:
                    valor1 = int(sub_values['-VALOR1-'])
                    valor2 = int(sub_values['-VALOR2-'])

                    if event == 'Somar':
                        resultado = valor1 + valor2
                    elif event == 'Subtrair':
                        resultado = valor1 - valor2
                    elif event == 'Multiplicar':
                        resultado = valor1 * valor2
                    elif event == 'Dividir':
                        resultado = valor1 / valor2

                    psg.popup(f'O resultado da operação é: {resultado}')
                    break

                except ValueError:
                    psg.popup('Erro! Digite apenas números inteiros.')
                    continue

        sub_window.close()

window.close()
