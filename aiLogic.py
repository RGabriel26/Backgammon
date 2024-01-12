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
        if len(self.gameLogic.dices) > 0:
            return self.aiMove()
        else:
            print('launchAI - NU SE MAI POT REALIZA MUTARI PENTRU CA NU MAI EXISTA ZARURI')
            return QTimer.singleShot(0, lambda: self.gameLogic.actionCanMakeMove())


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
        print('######################### AIMOVE 1 ########################')
        print("AI-ul face mutari...")
        oponentTeam = 'black' if self.teamAI == 'white' else 'white'
        print(f"Zarurile AI-ului: {self.gameLogic.getDices()}")

        if self.gameLogic.canMakeMove():
            print("AI-ul poate face mutari!")
            self.delay(1000)

            # lista de mutari posibile
            listMovePossibility = self.createMoveList(self.teamAI)
            # doar de test - afisarea listei de mutari posibile
            for move in listMovePossibility:
                print(f"pozitia initiala: {move[0].objectName()}, pozitia finala: {move[1][0]}, zarul folosit: {move[1][1]}")

            # alegerea unei mutari random din lista de mutari posibile
            move = listMovePossibility[randint(0, len(listMovePossibility) - 1)]

            # extragerea pozitiilor din mutarea aleasa
            initialPosition = move[0]
            initialPositionID = self.gameLogic.getPosID(initialPosition.objectName())
            moveToPositionID = move[1][0]
            usedDice = move[1][1]

            print(f'informatiile extrase din pozitia aleasa: pozitia initiala: {initialPosition.objectName()}, pozitia finala: {moveToPositionID}, zarul folosit: {usedDice}')

            # LOGICA DE MUTARE A PIESILOR

            # # pozitionarea unei piese ghost pe pozitia unde AI urmeaza sa mute piesa
            # self.gameLogic.addCheckerToPosition(f'pos{moveToPositionID}', 'ghost')
            # # aplicarea unui delay pentru a se vedea piesa ghost
            # self.delay(500)
            # # stergerea piesei ghost
            # self.gameLogic.deleteGhostCheckers(True)

            # # stergerea piesei de pe pozitia initiala
            # # daca piesa initial se afla pe gard, atunci aceasta se sterge din layout-ul respectiv, nu din pos
            # if initialPositionID == 0:
            #     self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().hide()
            #     self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().deleteLater()
            #     self.gameLogic.numberWhiteFenceCheckers -= 1
            # elif initialPositionID == 25:
            #     self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().hide()
            #     self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().deleteLater()
            #     self.gameLogic.numberBlackFenceCheckers -= 1
            # else:
            #     self.gameLogic.deleteCheckerFromPosition(initialPositionID)

            # adaugarea piesei pe pozitia mutata a piesei
            # verificare intervalului unde urmeaza sa fie mutata piesa
            if moveToPositionID > 0 and moveToPositionID < 25:
                layoutPosition = getattr(self.layouts, f'pos{moveToPositionID}')
                # pozitionarea unei piese ghost pe pozitia unde AI urmeaza sa mute piesa
                self.gameLogic.addCheckerToPosition(f'pos{moveToPositionID}', 'ghost')
                # aplicarea unui delay pentru a se vedea piesa ghost
                self.delay(500)
                # stergerea piesei ghost
                self.gameLogic.deleteGhostCheckers(True)

                # stergerea piesei de pe pozitia initiala
                # daca piesa initial se afla pe gard, atunci aceasta se sterge din layout-ul respectiv, nu din pos
                if initialPositionID == 0:
                    self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().hide()
                    self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().deleteLater()
                    self.gameLogic.numberWhiteFenceCheckers -= 1
                elif initialPositionID == 25:
                    self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().hide()
                    self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().deleteLater()
                    self.gameLogic.numberBlackFenceCheckers -= 1
                else:
                    self.gameLogic.deleteCheckerFromPosition(initialPositionID)  
                # se verifica daca pe pozitia unde urmeaza sa fie mutata piesa exista alte piese
                if layoutPosition.count() > 0:
                    # daca exista
                    # se verifica daca este o singura piesa pe pozitia respectiva
                    # IMPORTANT: datorita piesei ghost, cauzeaza o problema la verificarea acestui caz, deoarece piesa ghost nu se sterge din memorie pana cand toata functia nu este finalizata
                    # deci verificam daca exista 2 piese pe pozitie
                    # care ar trebui sa insemne ca pe pozitia 0 este o piesa a adversarului si pe pozitia 1 este piesa ghost
                    if layoutPosition.count() == 2:
                        if (layoutPosition.itemAt(0).widget().objectName() == f'{oponentTeam}Checker' and 
                            layoutPosition.itemAt(1).widget().objectName() == 'ghostChecker'):
                            # se sterge piesa adversarului si se adauga pe gard
                            layoutPosition.itemAt(0).widget().hide()
                            layoutPosition.itemAt(0).widget().deleteLater()
                            # se adauga piesa adversarului pe gard
                            self.gameLogic.addCheckerToFence(oponentTeam)
                            # se adauga piesa AI-ului pe pozitia mutata
                            self.gameLogic.addCheckerToPosition(f'pos{moveToPositionID}', self.teamAI)
                            print(f'aiMove - conditia 1: exista o piesa a adversarului pe pozitia: {moveToPositionID}')
                        # exista piesa doar a AI-ului teoretic
                        # practic sunt 2 piese pe pozitia respectiva, deoarece piesa ghost nu este stearsa din memorie
                        else:
                            # se adauga piesa AI-ului pe pozitia mutata
                            self.gameLogic.addCheckerToPosition(f'pos{moveToPositionID}', self.teamAI)
                            print(f'aiMove - conditia 2: exista o piesa a AI-ului pe pozitia: {moveToPositionID}')
                    # cazul in care piesa trebuie adaugata deoarece pozitia a fost verificate daca este permisa in functia createMoveList
                    else:
                        self.gameLogic.addCheckerToPosition(f'pos{moveToPositionID}', self.teamAI)
                        print(f'aiMove - conditia 3: exista o piesa a AI-ului pe pozitia: {moveToPositionID}')
                # daca nu sunt alte piese, inseamna ca AI ul poate muta fara probleme 
                # acest caz nu este posibil, deoarece piesa ghost nu este stearsa din memorie si mereu va exista o piesa pe pozitia unde se muta
                else:
                    self.gameLogic.addCheckerToPosition(f'pos{moveToPositionID}', self.teamAI)
                    print(f'aiMove - conditia 4: nu au fost alte piese pe pozitia: {moveToPositionID}')
            # situatia in care AI ul scoate piesa din joc
            else:
                # se da highlight
                self.gameLogic.highlightOutPosibility()
                self.delay(500)
                # se sterge piesa de pe pozitia initiala
                self.gameLogic.deleteCheckerFromPosition(initialPositionID)
                # se adauga piesa pe pozitia de scoatere a pieselor
                self.gameLogic.addOutCheker()
                self.gameLogic.highlightOutPosibility(False)

                # se verifica daca Ai a castigat jocul
                QTimer.singleShot(0, lambda: self.gameLogic.winConditionFromOutCheckersLayoutClick())



            # stergerea zarului folosit din lista de zaruri
            self.gameLogic.dices.remove(usedDice)
            # stergerea zarului folosit din layoutul zarurilor
            self.gameLogic.deleteDiceFromLayout(usedDice)
            print('######################### AIMOVE 2 ########################')
            return QTimer.singleShot(0, lambda: self.launchAI())
        else:
            print("AI-ul nu poate face mutari!")
            print('######################### AIMOVE 2 ########################')
            return QTimer.singleShot(0, lambda: self.gameLogic.actionCanMakeMove())

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
                                        break
                                # excluderea pozitiilor unde exista piese ale opentului si sunt mai mult de 1 piese
                                lastChecker = layoutPosition.count() - 1
                                if layoutPosition.itemAt(lastChecker).widget().objectName() not in [f'{oponentTeam}Checker']:
                                    # DACA NU SUNT PIESE ALE OPONENTELOR, INSEAMNA CA PE POZITIA RESPECTIVA EXISTA MAI MULT DE 1 PIESA A JUCATORULUI ACTUAL
                                    listMovePossibility.append((pos, (move, useDice)))
                                    break
                            else:
                                #CAZUL CAND PE POZITIA POSIBILA DE MUTARE NU EXISTA ALTE PIESE
                                listMovePossibility.append((pos, (move, useDice)))
                                break
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
                                        listMovePossibility.append((pos, (move, usedDiceForOutCheckers)))
                                        break
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
                                                    listMovePossibility.append((pos, (move, usedDiceForOutCheckers)))
                                                    break
                                            position += 1
                                else:
                                    position = 0 + useDice
                                    if posID == position:
                                        # verificarea pozitiei mai mari sau egale cu cea a zarului folosit
                                        if getattr(self.layouts, f'pos{position}').count() == 0:
                                            usedDiceForOutCheckers = min(self.getDices())
                                        else:
                                            usedDiceForOutCheckers = useDice
                                        listMovePossibility.append((pos, (move, usedDiceForOutCheckers)))
                                        foundOutMove = True
                                        break
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
                                                    listMovePossibility.append((pos, (move, usedDiceForOutCheckers)))
                                                    break
                                            position -= 1
            
        return listMovePossibility

        