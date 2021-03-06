from deuces import Evaluator

from pack import WHOLE_PACK

def best_holdem_hand(board, hand1, hand2):
    evaluator = Evaluator()
    return cmp(evaluator.evaluate(board, hand2), evaluator.evaluate(board, hand1))


def count_outs(turn, hand1, hand2):
    cards = WHOLE_PACK - set(turn + hand1 + hand2)
    values = [ best_holdem_hand(turn + [card], hand1, hand2) for card in cards ]
    return tuple([ len(list(v for v in values if v == x)) for x in [1, -1, 0] ])
