import PySimpleGUI as sg

class Tela1ES:

    #telas de perguntas
    def inicio():
        #layout
        layout = [
            [sg.Text('Bem-vindo!',)],
            [sg.Text('Este Sistema Especialista foi criado com o intuito de auxiliar crianças e adolescentes a identificar alguns gêneros de mosquitos. Não é recomendado para identificação taxonômica profissional.')],
            [sg.Button('Entrar')]           
        ]
        return sg.Window('Inicio', layout= layout, finalize=True) 
        #tela
        
    def Pergunta1():
        sg.change_look_and_feel('BrightColors')
        layout = [
            [sg.Text('Quantos pares de asas o inseto apresenta?')],
            [sg.Text('Quais suas características?')],
            [sg.Radio('2 pares de asas escamosas','Pares de asas',key = 'NparAsas1')],
            [sg.Radio('1 par de asas membranosas','Pares de asas',key = 'NparAsas2')],
            [sg.Radio('1 par de asas rigidas e 1 par de asas membranosas','Pares de asas',key = 'NparAsas3')],
            [sg.Radio('1 par de asas membranosas', 'Pares de asas', key = 'NparAsas4')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 1', layout= layout, finalize= True)
    
    def Pergunta2():
        sg.change_look_and_feel('DarkBrown2')
        layout = [
            [sg.Text('Este inseto pertence à Ordem Diptera, o grupo que representa mosquitos e moscas.')],
            [sg.Text('Olhando a cabeça do inseto, ele apresenta aparelho bucal em formato de agulha?',)],
            [sg.Radio('Sim','Forma Bucal',key = 'FormBucal1')],
            [sg.Radio('Nao','Forma Bucal',key = 'FormBucal2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 2', layout= layout, finalize= True)
    
    def Pergunta3s():
        sg.change_look_and_feel('DarkPurple1')
        layout = [
            [sg.Text('Qual a cor do inseto?',)],
            [sg.Radio('Azul','Cor do Inseto',key = 'CorInseto1s')],
            [sg.Radio('Preto','Cor do Inseto',key = 'CorInseto2s')],
            [sg.Radio('Marrom claro/ dourado','Cor do Inseto',key = 'CorInseto3s')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta3', layout=layout, finalize=True)
    
    def Pergunta3n():
        sg.change_look_and_feel('Green')
        layout = [
            [sg.Text('Qual a cor do inseto?',)],
            [sg.Radio('Verde','Cor do Inseto',key = 'CorInseto1n')],
            [sg.Radio('Preto','Cor do Inseto',key = 'CorInseto2n')],
            [sg.Radio('Marrom claro/ dourado','Cor do Inseto',key = 'CorInseto3n')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta3', layout=layout, finalize=True)
    
    def Pergunta4():
        sg.change_look_and_feel('LightBrown3')
        layout = [
            [sg.Text('Apresenta um “tufo de pelo” no segundo par de pernas?',)],
            [sg.Radio('Sim','Tufo de pelo',key = 'TufodePelo1')],
            [sg.Radio('Nao','Tufo de pelo',key = 'TufodePelo2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 4', layout=layout, finalize=True)
    
    def Pergunta5():
        sg.change_look_and_feel('LightGreen5')
        layout = [
            [sg.Text('A coloração do mosquito é mais azulada ou preta?',)],
            [sg.Radio('Azulada','Corloracao Mosquito',key = 'ColoracaoM1')],
            [sg.Radio('Preta','Coloracao Mosquito',key = 'ColoracaoM2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 5', layout=layout, finalize=True)
    
    def Pergunta6():
        sg.change_look_and_feel('Reds')
        layout = [
            [sg.Text('Tem pintinhas ou manchas brancas ou prateadas nas pernas?',)],
            [sg.Radio('Sim','Pintas',key = 'Pintas1')],
            [sg.Radio('Nao','Pintas',key = 'Pintas2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 6', layout=layout, finalize=True)
    
    def Pergunta7():
        sg.change_look_and_feel('DarkRed1')
        layout = [
            [sg.Text('Tem coloração azulada?',)],
            [sg.Radio('Sim','Cor Azulada',key = 'Cor1')],
            [sg.Radio('Nao','Cor Azulada',key = 'Cor2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 7', layout=layout, finalize=True)
    
    def Pergunta8():
        sg.change_look_and_feel('DarkAmber')
        layout = [
            [sg.Text('Como é a coloração da borda das asas do mosquito?',)],
            [sg.Radio('Bicolor','Cor Borda da Asa',key = 'CorBasas1')],
            [sg.Radio('1 so cor','Cor Bordda da Asa',key = 'CorBasas2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 8', layout=layout, finalize=True)

    def Pergunta9():
        sg.change_look_and_feel('DarkBlue4')
        layout = [
            [sg.Text('O inseto apresenta algum desenho no dorso("nas costas")?',)],
            [sg.Radio('Sim','Desenho no Dorso',key = 'Desenho1')],
            [sg.Radio('Nao','Desenho no Dorso',key = 'Desenho2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 9', layout=layout, finalize=True)

    def Pergunta10():
        sg.change_look_and_feel('DarkBlack')
        layout = [
            [sg.Text('Qual o tamanho do inseto?',)],
            [sg.Radio('Grande: aprox. 2 cm','Tamanho do Inseto',key = 'Tamanho1')],
            [sg.Radio('Pequeno: menor que 1 cm','Tamanho do Inseto',key = 'Tamanho2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 10', layout=layout, finalize=True)

    def Pergunta11():
        sg.change_look_and_feel('DarkTeal')
        layout = [
            [sg.Text('A asa possui uma mancha mais escura na parte central superior da borda?',)],
            [sg.Radio('Sim','Mancha Escura',key = 'Mancha1')],
            [sg.Radio('Nao','Mancha Escura',key = 'Mancha2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 11', layout=layout, finalize=True)

    def Pergunta12():
        sg.change_look_and_feel('HotDogStand')
        layout = [
            [sg.Text('Tem estrutura parecida com espinhos nas pernas?',)],
            [sg.Radio('Sim','Espinhos',key = 'Espinho1')],
            [sg.Radio('Nao','Espinhos',key = 'Espinho2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 12', layout=layout, finalize=True)

    def Pergunta13():
        sg.change_look_and_feel('BluePurple')
        layout = [
            [sg.Text('É um mosquito pequeno (~2 mm) e apresenta o corpo e as asas cobertos por cerdas que parecem pelos?')],
            [sg.Radio('Sim','Cerdas',key = 'Cerdas1')],
            [sg.Radio('Nao','Cerdas',key = 'Cerdas2')],
            [sg.Button('Confirmar')]           
        ]
        return sg.Window('Pergunta 13', layout=layout, finalize=True)
    
    #tela de especies
    def Lepidoptera():
        sg.change_look_and_feel('DarkBlack')
        layout = [
            [sg.Text('Este inseto pertence à Ordem Lepidoptera, que não é a Ordem dos mosquitos. Os seus principais representantes são as borboletas e mariposas.', size=(80,5))]
        ]
        return sg.Window('Lepdoptera', layout=layout, finalize=True)
    
    def Hymenoptera():
        layout = [
            [sg.Text('Este inseto pertence à Ordem Hymenoptera, que não é a Ordem dos mosquitos. Os seus representantes mais conhecidos são as vespas, abelhas e formigas.', size=(80,5))]
        ]
        return sg.Window('Hymenoptera', layout=layout, finalize=True)
    
    def Coleoptera():
        layout = [
            [sg.Text('Este inseto provavelmente pertence à Ordem Coleoptera, que não é a Ordem dos mosquitos. Os insetos mais populares desta ordem são os besouros e as joaninhas.', size=(80,5))]
        ]
        return sg.Window('Coleoptera', layout=layout, finalize=True)
    
    def Sabethes():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Sabethes, que pica e pode transmitir o vírus da Febre Amarela. Este gênero é popularmente conhecido como o "mosquito da febre amarela".', size=(80,5))]
        ]
        return sg.Window('Sabethes', layout=layout, finalize=True)
    
    def Haemagogus():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Haemagogus, que pica e pode transmitir o vírus da Febre Amarela. O mosquito deste gênero é popularmente conhecido como "mosquito da febre amarela".', size=(80,5))]
        ]
        return sg.Window('Haemagogus', layout=layout, finalize=True)
    
    def Erro():
        layout = [
            [sg.Text('Volte ao passo em que perguntamos sobre o aparelho bucal do inseto. Pode ter havido confusãoem alguns dos passos anteriores.', size=(80,5))]
        ]
        return sg.Window('Erro', layout=layout, finalize=True)
    
    def Anopheles():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Anopheles, que pica e pode transmitir os parasitas que causam malária ou filariose. O mosquito deste gênero é popularmente conhecido como "mosquito prego".', size=(80,5))]
        ]
        return sg.Window('Anopheles', layout=layout, finalize=True)
    
    def Aedes():
        layout = [
            [sg.Text('O mosquito é provavelmente do gênero Aedes. Dentro desse gênero existe uma espécie que tem alta importância médica: o Aedes aegupti, que pica e pode transmitir principalmente dengue, Zika e chikungunya. Os mosquitos desta espécie apresentam desenho formado por escamas brancas/prateadas em formato de lira. São popularmente conhecidos como "mosquito da dengue".', size=(80,5))]
        ]
        return sg.Window('Aedes', layout=layout, finalize=True)
    
    def Aviso():
        layout = [
            [sg.Text('Pode se tratar de um mosquito que até o momento não foi relacionado com alguma doença. Para mais informações, consulte uma pessoa especialista.', size=(80,5))]
        ]
        return sg.Window('Aviso', layout=layout, finalize=True)
    
    def Culex():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Culex, que pica e pode transmitir doenças como a filariose, também conhecida como elefantíase. O mosquito deste gênero é popularmente conhecido como "pernilongo ou muriçoca".', size=(80,5))]
        ]
        return sg.Window('Culex', layout=layout, finalize=True)
    
    def Tipulidae():
        layout = [
            [sg.Text('Este inseto provavelmente pertence à Família Tipulidae. Este inseto é conhecido popularmente como "mosquito gigante" e não pica.', size=(80,5))]
        ]
        return sg.Window('Tipulidae', layout=layout, finalize=True)
    
    def Chironomidae():
        layout = [
            [sg.Text('Este inseto pode pertencer à Família Chironomidae, que não pica e não está relacionado à nenhuma doença humana/animal.', size=(80,5))]
        ]
        return sg.Window('Chironomidae', layout=layout, finalize=True)
    
    def Culicoides():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Culicoides, que pica e pode transmitir a febre oropouche. O mosquito deste gênero é popularmente conhecido como "mosquitinho do mangue, maruim ou mosquito pólvora".', size=(80,5))]
        ]
        return sg.Window('Culicoides', layout=layout, finalize=True)

    def Simulium():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Simulium, que pica e pode transmitir doenças como a oncocercose e a mansonelose. O mosquito deste genêro é popularmente conhecido como "borrachudo".', size=(80,5))]
        ]
        return sg.Window('Simulium', layout=layout, finalize=True)
    
    def Culicidae():
        layout = [
            [sg.Text('Este inseto não pertence às Famílias Culicidae e Psychodidae. Então provavelmente não tem importância médica. Para maiores informações, consulte uma pessoa especialista.', size=(80,5))]
        ]
        return sg.Window('Culicidae', layout=layout, finalize=True)
    
    def Lutzomyia():
        layout = [
            [sg.Text('O mosquito pode pertencer ao gênero Lutzomyia que pica e pode transmitir doenças como a Leishmaniose. O mosquito deste gênero é popularmente conhecido como "mosquito palha".', size=(80,5))]
        ]
        return sg.Window('Lutzomyia', layout=layout, finalize=True)

    janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, janela11, janela12, janela13, janela14, janela15= inicio(), None, None, None, None, None, None, None, None, None, None, None, None, None, None
    janelaesp1, janelaesp2, janelaesp3, janelaesp4, janelaesp5, janelaesp6, janelaesp7, janelaesp8, janelaesp9, janelaesp10, janelaesp11, janelaesp12, janelaesp13, janelaesp14, janelaesp15, janelaesp16 = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

    while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                break

            if window == janela1 and event == 'Entrar':
                janela2 = Pergunta1()
                janela1.hide()

            #Variavel1
            if window == janela2 and event == 'Confirmar':
                #regra1
                if values['NparAsas1'] == True:
                    janela2.hide()
                    janelaesp1 = Lepidoptera()
                    
                #regra2
                if values['NparAsas2'] == True:
                    janela2.hide()
                    janelaesp2 = Hymenoptera()

                #regra3
                if values['NparAsas3'] == True:
                    janela2.hide()
                    janelaesp3 = Coleoptera()

                if values['NparAsas4'] == True:
                    janela2.hide()
                    janela3 = Pergunta2()
                
                nparasas1 = values['NparAsas1']
                nparasas2 = values['NparAsas2']
                nparasas3 = values['NparAsas3']
                nparasas4 = values['NparAsas4']

            #variavel2
            if window == janela3 and event == 'Confirmar':
                if values['FormBucal1'] == True and nparasas4 == True:
                    janela3.hide()
                    janela4 = Pergunta3s()
                if values['FormBucal2'] == True and nparasas4 == True:
                    janela3.hide()
                    janela15 = Pergunta3n()
                
                boca1 = values['FormBucal1']
                boca2 = values['FormBucal2']

            #varieavel3
            if window == janela4 and event == 'Confirmar':
                if values['CorInseto1s'] == True and boca1 == True and nparasas4 == True:
                    janela4.hide()
                    janela5 = Pergunta4()
                if values['CorInseto2s'] == True and boca1 == True and nparasas4 == True:
                    janela4.hide()
                    janela7 = Pergunta6()
                if values['CorInseto3s'] == True and boca1 == True and nparasas4 == True:
                    janela4.hide()
                    janela7 = Pergunta6()

                corinseto1s = values['CorInseto1s']
                corinseto2s = values['CorInseto2s']
                corinseto3s = values['CorInseto3s']
            
            if window == janela15 and event == 'Confirmar':
                if values['CorInseto1n'] == True and boca2 == True and nparasas4 == True:
                    janela15.hide()
                    janela12 = Pergunta10()
                if values['CorInseto2n'] == True and boca2 == True and nparasas4 == True:
                    janela15.hide()
                    janela9 = Pergunta8()
                if values['CorInseto3n'] == True and boca2 == True and nparasas4 == True:
                    janela15.hide()
                    janela13 = Pergunta12()

                corinseto1n = values['CorInseto1n']
                corinseto2n = values['CorInseto2n']
                corinseto3n = values['CorInseto3n']

            #variavel4
            if window == janela5 and event == 'Confirmar':
                #regra4
                if values['TufodePelo1'] == True and boca1 == True and nparasas4 == True and corinseto1s == True:
                    janela5.hide()
                    janelaesp4 = Sabethes()
                    
                if values['TufodePelo2'] == True and boca1 == True and nparasas4 == True and corinseto1s == True:
                    janela5.hide()
                    janela6 = Pergunta5()
                
                tufo1 = values['TufodePelo1']
                tufo2 = values['TufodePelo2']

            #variavel5
            if window == janela6 and event == 'Confirmar':
                #regra5
                if values['ColoracaoM1'] == True and nparasas4 == True and boca1 == True and corinseto1s == True and tufo2 == True:
                    janela6.hide()
                    janelaesp4 = Sabethes()

                #regra6
                if values['ColoracaoM2'] == True and nparasas4 == True and boca1 == True and corinseto1s == True and tufo2 == True:
                    janela6.hide()
                    janelaesp5 = Haemagogus()

                coloracaom1 = values['ColoracaoM1']
                coloracaom2 = values['ColoracaoM1']

            #variavel6
            if window == janela7 and event == 'Confirmar':
                if values['Pintas1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True:
                    janela7.hide()
                    janela9 = Pergunta8()
                elif values['Pintas2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True:
                    janela7.hide()
                    janela8 = Pergunta7()
                #regra16
                elif values['Pintas1'] == True and nparasas4 == True and boca1 == True and corinseto3s == True:
                    janela7.hide()
                    janelaesp6 = Aedes()
                #regra17
                elif values['Pintas2'] == True and nparasas4 == True and boca1 == True and corinseto3s == True:
                    janela7.hide()
                    janelaesp7 = Culex()
            
                pintas1 = values['Pintas1']
                pintas2 = values['Pintas2']

            if window == janela8 and event == 'Confirmar':
                #regra7
                if values['Cor1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True:
                    janela8.hide()
                    janelaesp5 = Haemagogus()

                elif values['Cor2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True:
                    janela8.hide()
                    janela9 = Pergunta8()
                
                corA1 = values['Cor1']
                corA2 = values['Cor2']

            if window == janela9 and event == 'Confirmar':
                if values['CorBasas1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True and corA2 == True:
                    janela9.hide()
                    janela10 = Pergunta11()
                elif values['CorBasas2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True:
                    janela9.hide()
                    janela11 = Pergunta9()
                elif values['CorBasas1'] and nparasas4 == True and boca1 == True and corinseto2s == True and pintas1 == True:
                    janela9.hide()
                    janela10 = Pergunta11()
                elif values['CorBasas2'] and nparasas4 == True and boca1 == True and corinseto2s == True and pintas1 == True:
                    janela9.hide()
                    janela11 = Pergunta9()
                elif values['CorBasas1'] == True and nparasas4 == True and boca2 == True and corinseto2n == True:
                    janela9.hide()
                    janela10 = Pergunta11()
                #regra22
                elif values['CorBasas2'] == True and nparasas4 == True and boca2 == True and corinseto2n == True:
                    janela9.hide()
                    janelaesp8 = Simulium()

                corB1 = values['CorBasas1']
                corB2 = values['CorBasas2']

            if window == janela10 and event == 'Confirmar':
                #regra8
                if values['Mancha1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True and corA2 == True and corB1 == True:
                    janela10.hide()
                    janelaesp9 = Erro()
                    
                #regra9
                elif values['Mancha2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True and corA2 == True and corB1 == True:
                    janela10.hide()
                    janelaesp10 = Anopheles()
                #regra12
                elif values['Mancha1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas1 == True and corB1 == True:
                    janela10.hide()
                    janelaesp9 = Erro()

                #regra13
                elif values['Mancha2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas1 == True and corB1 == True:
                    janela10.hide()
                    janelaesp10 = Anopheles()
                    
                #regra20
                elif values['Mancha1'] == True and nparasas4 == True and boca2 == True and corinseto2n == True and corB1 == True:
                    janela10.hide()
                    janelaesp11 = Culicoides()
                    
                #regra21
                elif values['Mancha2'] == True and nparasas4 == True and boca2 == True and corinseto2n == True and corB1 == True:
                    janela10.hide()
                    janelaesp9 = Erro()
                
                mancha1 = values['Mancha1']
                mancha2 = values['Mancha2']

            if window == janela11 and event == 'Confirmar':
                #regra10
                if values['Desenho1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True and corA2 == True and corB2 == True:
                    janela11.hide()
                    janelaesp6 = Aedes()
                    
                #regra11
                elif values['Desenho2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas2 == True and corA2 == True and corB2 == True:
                    janela11.hide()
                    janelaesp12 = Aviso()
                    
                #regra14
                elif values['Desenho1'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas1 == True and corB2 == True:
                    janela11.hide()
                    janelaesp6 = Aedes()
                #regra15
                elif values['Desenho2'] == True and nparasas4 == True and boca1 == True and corinseto2s == True and pintas1 == True and corB2 == True:
                    janela11.hide()
                    janelaesp12 = Aviso()
                
                desenho1 = values['Desenho1']
                desenho2 = values['Desenho2']
            
            if window == janela12 and event == 'Confirmar':
                #regra18
                if values['Tamanho1'] == True and nparasas4 == True and boca2 == True and corinseto1n == True:
                    janela12.hide()
                    janelaesp13 = Tipulidae()
                    
                #regra19
                elif values['Tamanho2'] == True and nparasas4 == True and boca2 == True and corinseto1n == True:
                    janela12.hide()
                    janelaesp14 = Chironomidae()

                tamanho1 = values['Tamanho1']
                tamanho2 = values['Tamanho2']
            
            if window == janela13 and event == 'Confirmar':
                #regra23
                if values['Espinho1'] == True and nparasas4 == True and boca2 == True and corinseto3n == True:
                    janela13.hide()
                    janelaesp15 = Culicidae()
                    
                elif values['Espinho2'] == True and nparasas4 == True and boca2 == True and corinseto3n == True:
                    janela13.hide()
                    janela14 = Pergunta13()
                
                espinho1 = values['Espinho1']
                espinho2 = values['Espinho2']
            
            if window == janela14 and event == 'Confirmar':
                #regra24
                if values['Cerdas1'] == True and nparasas4 == True and boca2 == True and corinseto3n == True and espinho2 == True:
                    janela14.hide()
                    janelaesp16 = Lutzomyia()
                    
                #regra25
                elif values['Cerdas2'] == True and nparasas4 == True and boca2 == True and corinseto3n == True and espinho2 == True:
                    janela14.hide()
                    janelaesp15 = Culicidae()
                
                cerdas1 = values['Cerdas1']
                cerdas2 = values['Cerdas2']
            
            

