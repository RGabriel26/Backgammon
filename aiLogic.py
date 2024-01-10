from PyQt6.QtCore import QTimer, QCoreApplication, QElapsedTimer

from random import randint

from checkers import Checkers

from time import sleep


class AILogic:
    def __init__(self, gameLogic):
        print('Initializare AI Logic')
        self.gameLogic = gameLogic
        self.teamAI = self.gameLogic.teamTurn
        self.layouts = self.gameLogic.layouts

    def delay(self, milliseconds) -> None:
        timer = QElapsedTimer()
        timer.start()
        while timer.elapsed() < milliseconds:
            QCoreApplication.processEvents()

    def launchAI(self) -> None:
        if self.gameLogic.canMakeMove():
            self.aiMove()
        else:
            self.gameLogic.actionCanMakeMove()


    def aiMove(self) -> None:
        # TODO: implementeaza sistemul de mutari pentru AI
        # Cat timp exista zaruri, aceasta se va reapela
        # aici se verifica daca se pot realiza mutari cu zarurile primite prin functia candMakeMove
        # daca da, se face o lista cu seturi de pozitii posibilie
            # set de pozitie posibila => (pozitia_unde_este_piesa_initial - pozitia_unde_se_va_muta_piesa, zarul_folosit)
            # se va "muta piesa", adica se va sterge de pe pozitia anterioara si se va adauga pe pozitia noua
            # si se va sterge zarul folosit atat din lista care il stocheaza cat si din layout zarurilor destinat afisarii
        # daca mai exista zaruri, functia se va apela recursiv
        # cand nu mai exista piese, sau functia canMakeMove returneaza False, se va apela functia logic pentru a trece la jucatorul urmator
        # se va folosit si functia showPossibleMove pentru a afisa pozitiile posibile de pe pozitia de unde urmeaza sa se realizeze mutarea, pentru 
        # ca celalalt jucator sa inteleaga ce se intampla
        # Se va folosi un DELAY pentru a nu se intampla tot instant
        print("AI-ul face mutari...")
        oponentTeam = 'black' if self.teamAI == 'white' else 'white'
        
        # verificare daca ai ul are posibilitatea de a realiza mutari cu zarurile disponibile de undeva de pe tabla de joc
        if self.gameLogic.canMakeMove():
            print("AI-ul poate realiza mutari")
            # se face o lista cu seturile de pozitii posibile ale acestuia
            # crearea listei cu mutari posibile
            # TODO
            listMovePossibility = self.createMoveList(self.teamAI)
            print(f"lista de mutari pe care le poate face AI-ul:")
            # doar de test ########
            for move in listMovePossibility:
                print(f"pozitia initiala: {move[0].objectName()}, pozitia finala: {move[1][0]}, zarul folosit: {move[1][1]}")
            #######################
            # alegerea random a unei mutari din lista pe care Ai poate sa o faca
            lengthList = len(listMovePossibility) - 1
            indexMoveAi = randint(0, 0 if lengthList == 0 else lengthList)
            # executarea mutarii
            # extragerea detaliilor din listMovePossibility corespunzatoare indexului generat
            initialPos = listMovePossibility[indexMoveAi][0].objectName() #id-ul pozitiei de unde se sterge piesa mutata
            print(f'pozitia initiala: {listMovePossibility[indexMoveAi][0].objectName()}')
            actualPos = f'pos{listMovePossibility[indexMoveAi][1][0]}' #pozitia unde se va muta piesa
            usedDice = listMovePossibility[indexMoveAi][1][1]
            # se va afisa o piesa ghost pentru a informa celalalt jucator cu privire la ce mutare va urma sa faca ai ul
            self.gameLogic.addCheckerToPosition(actualPos, 'ghost')
            print('inainte de delay 1')
            self.delay(1000)
            print('dupa delay 1')
            # inainte de executia mutarii piesei, trebuie stearsa piesa ghost
            self.gameLogic.deleteGhostCheckers(True)
            # getattr(self.gameLogic.layouts, actualPos).itemAt(getattr(self.gameLogic.layouts, actualPos).count() - 1).widget().deleteLater()
                # stergerea piesei de unde se muta piesa
            if self.gameLogic.getPosID(initialPos) == 0:
                self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().hide()
                self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().deleteLater()
                # TODO: cerd ca trebuie sa se stearga si din lista de piese de pe gard
                self.gameLogic.numberWhiteFenceCheckers -= 1
            elif self.gameLogic.getPosID(initialPos) == 25:
                self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().hide()
                self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().deleteLater()
                self.gameLogic.numberBlackFenceCheckers -= 1
            else:
                self.gameLogic.deleteCheckerFromPosition(self.gameLogic.getPosID(initialPos))
                # adaugarea piesei pe pozitia unde se muta piesa
            # TODO: aici trebuie verificat daca nu cumva piesa adaugata nu arunca piesa adversarului pe gard
            layoutPosition = getattr(self.gameLogic.layouts ,actualPos)
            # verificam daca pe pozitia unde urmeaza sa fie adaugata piesa ai ului exista piese
            if layoutPosition.count() > 0:
                # verificam cate piese sunt
                # daca este doar una, verificam daca aceasta este a adversarului
                # TODO: Nu se sterg corect obiectele ghost
                print(layoutPosition.count())
                if layoutPosition.count() == 2:
                    # daca este a adversarului, se arunca piesa acestuia pe gard
                    if layoutPosition.itemAt(0).widget().objectName() == f'{oponentTeam}Checker' and layoutPosition.itemAt(layoutPosition.count() - 1).widget().objectName() == 'ghostChecker':
                        print("conditia 1")
                        # stergerea piesei adversarului 
                        self.gameLogic.deleteCheckerFromPosition(self.gameLogic.getPosID(actualPos))
                        # adaugarea sa pe gard
                        self.gameLogic.addCheckerToFence(oponentTeam)
                        if oponentTeam == "white":
                            self.gameLogic.numberWhiteFenceCheckers += 1
                        else:
                            self.gameLogic.numberBlackFenceCheckers += 1 
                        # adaugarea piesei ai ului
                        self.gameLogic.addCheckerToPosition(actualPos, self.teamAI)
                    # daca nu este piesa adversarului, inseamna ca este piesa ai ului si se poate adauga piesa
                    else:
                        self.gameLogic.addCheckerToPosition(actualPos, self.teamAI)
                        print("conditia 2")
                # daca sunt mai multe piese se verifica ca aceste sa nu fie ale adversarului
                else:
                    if layoutPosition.itemAt(0).widget().objectName() not in [f'{oponentTeam}Checker']:
                        self.gameLogic.addCheckerToPosition(actualPos, self.teamAI)
                        print("conditia 3")
                # stergerea zarului din lista de zaruri
            # daca nu sunt deloc piese pe pozitie, ai poate adauga piesa fara restrictii
            else:
                self.gameLogic.addCheckerToPosition(actualPos, self.teamAI)
                print("conditia 4")

            # stergera zarului folosit
            print(f'moveAI - zarurile disponibile: {self.gameLogic.dices}')
            print(f' moveaAI - zarul folosit pentru realizarea mutarii: {usedDice}')
            self.gameLogic.dices.remove(usedDice)   
            print(f'moveAI - zarurile disponibile: {self.gameLogic.dices}')
            self.gameLogic.deleteDiceFromLayout(usedDice)
            # ai nu mai poate face mutari
        print("FINALIZARE FUNCTIE AIMOVE")
        if self.gameLogic.dices:
            self.launchAI()
        else:
            self.gameLogic.actionCanMakeMove()
    
    def deleteDices(self, usedDice) -> None:
        print(f'moveAI - zarurile disponibile: {self.gameLogic.dices}')
        print(f' moveaAI - zarul folosit pentru realizarea mutarii: {usedDice}')
        self.gameLogic.dices.remove(usedDice)   
        print(f'moveAI - zarurile disponibile: {self.gameLogic.dices}')
        self.gameLogic.deleteDiceFromLayout(usedDice)


    def createMoveList(self, team) -> None:
        # lista care va fi returnata cu mutarile posibile de unde ai poate realiza mutari
        # forma listei: 
        # [pozitie_piesa_initiala, (pozitie_piesa_finala, zarul_folosit)]
        listMovePossibility = []
        oponentTeam = "black" if team == "white" else "white"
        foundOutMove = False
        possibleMove = []
        positions = self.gameLogic.getPositionsList()
        # navigarea prin pozitiile tablei
        # pentru a cauta pozitii unde sunt piesele Ai-ului
        for pos in positions:
            # daca se gaseste pe pozitia pos piese ale jucatorului
            # se creaza o lista de mutari losibile de pe aceasta pozitie folosind zarurile curente
            # VERIFICARE CA PE POZITIA N SA FIE PIESA AI-ULUI   
            if pos.count() > 0:
                if pos.itemAt(0).widget().objectName() == f"{self.teamAI}Checker":
                    posID = self.gameLogic.getPosID(pos.objectName())
                    possibleMove.clear()
                    # crearea listei cu mutari posibile de pe pozitia n
                    if self.teamAI == "white":
                        for dice in self.gameLogic.getDices():
                            possibleMove.append(posID + dice)
                    else:
                        for dice in self.gameLogic.getDices():
                            possibleMove.append(posID - dice)
                    # pentru fiecare mutare pozibila de pe pozitia de unde s-au gasit piese
                    for move in possibleMove:
                        useDice = self.gameLogic.getUsedDice(move, posID, team)
                        # CONDITIA CA MUTAREA POSIBILA SA FIE IN INTERIORUL TABLEI
                        if move >= 1 and move <= 24:
                            layoutPosition = getattr(self.layouts, f'pos{move}')
                            # cazul in care pe pozitia posibila exista alte piese
                            if layoutPosition.count() > 0:
                                # veificam ca pe pozitia respectica sa existe doar o piesa
                                if layoutPosition.count() == 1:
                                    # daca exista doar o piesa, atunci se verifica daca acesta este a adversarului
                                    if layoutPosition.itemAt(0).widget().objectName() == f'{oponentTeam}Checker':
                                        # daca piesa existenta este a adversarului
                                        # se ia in considerare ca AI ul poate face o mutare peste piesa adversarului
                                        # scotand piesa adversarului pe gard
                                        listMovePossibility.append((pos, (move, useDice)))
                                        # break
                                # excluderea pozitiilor unde exista piese ale opentului si sunt mai mult de 1 piese
                                lastChecker = layoutPosition.count() - 1
                                if layoutPosition.itemAt(lastChecker).widget().objectName() not in [f'{oponentTeam}Checker']:
                                    # DACA NU SUNT PIESE ALE OPONENTELOR, INSEAMNA CA PE POZITIA RESPECTIVA EXISTA MAI MULT DE 1 PIESA A JUCATORULUI ACTUAL
                                    listMovePossibility.append((pos, (move, useDice)))
                                    # break
                            else:
                                #CAZUL CAND PE POZITIA POSIBILA DE MUTARE NU EXISTA ALTE PIESE
                                listMovePossibility.append((pos, (move, useDice)))
                                # break
                        else:
                            # RESTRICTII
                            # se verifica daca jucatorul poate face mutari de scoatere a pieselor din joc
                            # momentul cand zona de scoatere a pieselor devine activa si jucatorul poate realiza mutari in afara tablei, rezultand scoaterea pieselor din joc
                            if self.gameLogic.allCheckersHouse() and not foundOutMove:

                                # cazul in care zarul folosit scoaterii piesei este egal cu pozitia piesei
                                if self.teamAI == "white":
                                    # daca pozitia selectata este corespunzatoare zarului care arunca piesa in afara jocului
                                    position = 25 - useDice
                                    if posID == position:
                                        # verificarea pozitiei mai mari sau egale cu cea a zarului folosit
                                        if getattr(self.layouts, f'pos{position}').count() == 0:
                                            usedDiceForOutCheckers = min(self.getDices())
                                        else:
                                            usedDiceForOutCheckers = useDice
                                        foundOutMove = True
                                        listMovePossibility.append(pos, (move, usedDiceForOutCheckers))
                                        # break
                                    # pentru poztitiile corespunzatoare zarurilor unde nu sunt piese, se activeaza zona de out a pieselor
                                    # pentru a folosi zarul ramas pentru a scoate ultima piesa disponobila
                                    else:
                                        position = 25 - 6
                                        while position < 25:
                                            # restrictie in cazul in care pe o pozitie mai mare decat zarul primit, poti face mutari, nu va permite scoaterea pieselor de pe pozitii mai mici decat zarul curent]
                                            # pentru a se obliga sa fie folosit zarul pentru facut mutari, nu pentru scos piese
                                            if getattr(self.layouts, f'pos{position}').count() > 0 and getattr(self.layouts, f'pos{position}').itemAt(0).widget().objectName() != f'{oponentTeam}Checker':
                                                break
                                            if posID == position + 1:
                                                # DACA PE POZITIA ZARULUI NU SUNT PIESE, INSEAMNA CA SE POT SCOATE PIESE DE PE POZITIA URMATORE
                                                if getattr(self.layouts, f'pos{posID - 1}').count() == 0:
                                                    foundOutMove = True
                                                    usedDiceForOutCheckers = useDice
                                                    listMovePossibility.append(pos, (move, usedDiceForOutCheckers))
                                                    # break
                                            position += 1
                                else:
                                    position = 0 + useDice
                                    if posID == position:
                                        # verificarea pozitiei mai mari sau egale cu cea a zarului folosit
                                        if getattr(self.layouts, f'pos{position}').count() == 0:
                                            usedDiceForOutCheckers = min(self.getDices())
                                        else:
                                            usedDiceForOutCheckers = useDice
                                        listMovePossibility.append(pos, (move, usedDiceForOutCheckers))
                                        foundOutMove = True
                                        # break
                                    # pentru poztitiile corespunzatoare zarurilor unde nu sunt piese, se activeaza zona de out a pieselor
                                    # pentru a folosi zarul ramas pentru a scoate ultima piesa disponobila
                                    else:
                                        position = 0 + 6
                                        while position > 0:
                                            # restrictie in cazul in care pe o pozitie mai mare decat zarul primit, poti face mutari, nu va permite scoaterea pieselor de pe pozitii mai mici decat zarul curent]
                                            # pentru a se obliga sa fie folosit zarul pentru facut mutari, nu pentru scos piese
                                            if getattr(self.layouts, f'pos{position}').count() > 0 and getattr(self.layouts, f'pos{position}').itemAt(0).widget().objectName() != f'{oponentTeam}Checker':
                                                break
                                            if posID == position - 1:
                                                # DACA PE POZITIA ZARULUI NU SUNT PIESE, INSEAMNA CA SE POT SCOATE PIESE DE PE POZITIA URMATORE
                                                if getattr(self.layouts, f'pos{posID + 1}').count() == 0:
                                                    foundOutMove = True
                                                    usedDiceForOutCheckers = useDice
                                                    listMovePossibility.append(pos, (move, usedDiceForOutCheckers))
                                                    # break
                                            position -= 1
            
        return listMovePossibility

        