from app.strategies.breakout import (
    evaluate_breakout
)

from app.strategies.breakdown import (
    evaluate_breakdown
)

from app.strategies.support_bounce import (
    evaluate_support_bounce
)

from app.strategies.resistance_rejection import (
    evaluate_resistance_rejection
)

from app.strategies.fake_breakout import (
    evaluate_fake_breakout
)


def classify_strategy(data):

    evaluators = [
        evaluate_breakout,
        evaluate_breakdown,
        evaluate_support_bounce,
        evaluate_resistance_rejection,
        evaluate_fake_breakout
    ]

    for evaluator in evaluators:

        result = evaluator(data)

        if result:
            return result

    return None