import random


class GamblingProb:

    def Gambler(self, goal, stake):
        bet = 1
        win = loss = num_of_bet = 0
        while stake <= goal & stake > 0:
            betCheck = random.randint(0, 1)
            if betCheck == 1:
                win += 1
                print("Total win is ", win)
                stake += bet
                if stake == goal:
                    break
                else:
                    loss += 1
                    stake -= bet
                    print("total loss is ", loss)
                    if stake == 0:
                        break

            num_of_bet = num_of_bet + 1
            print("Win percentage:", (win / num_of_bet) * 100)
            print("Loss percentage", (loss / num_of_bet) * 100)
            break


obj = GamblingProb()
obj.Gambler(100, 200)

