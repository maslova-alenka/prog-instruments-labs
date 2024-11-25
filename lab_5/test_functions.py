import json
import os
import pytest

from functions import check_card_number, get_card_number, luhn_algorithm, graphing


SETTINGS = {
        "hash": "70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473",
        "bins": [413064, 415028, 427230, 427275, 429749, 446674, 462017, 462043, 489327],
        "last_numbers": 1378
    }


def test_check_card_number():
    result = \
        check_card_number(745836,
                          [413064, 415028, 427230, 427275, 429749, 446674, 462017, 462043, 489327], 1378,
                          "70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473")
    assert result == "4466747458361378"


def test_get_card_number():
    get_card_number(SETTINGS["hash"], SETTINGS["bins"], SETTINGS["last_numbers"])
    with open("card.json") as json_file:
        data = json.load(json_file)
    assert data["card_number"] == "4466747458361378"


@pytest.mark.parametrize(("numbers", "result"),
                         [('4466747458361378', False), ('7638294589620560', True)])
def test_luhn_algorithm(numbers, result):
    assert luhn_algorithm(numbers) == result


def test_graphing():
    graphing(SETTINGS["hash"], SETTINGS["bins"], SETTINGS["last_numbers"])
    with open("card.json") as json_file:
        data = json.load(json_file)
    assert data["card_number"] == "4466747458361378"
    assert os.path.isfile("graph.png")

