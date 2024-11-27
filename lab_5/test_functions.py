import json
import numpy as np
import os
import pytest
import scipy.stats as sts
import statistics as st

from functions import check_card_number, get_card_number, luhn_algorithm, graphing
from stats import find_expectation, find_expectation_no_dis
from working_with_a_file import read_json, write_file


SETTINGS = {
        "hash": "70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473",
        "bins": [413064, 415028, 427230, 427275, 429749, 446674, 462017, 462043, 489327],
        "last_numbers": 1378
    }


def test_check_card_number():
    result = check_card_number(745836, SETTINGS["bins"], SETTINGS["last_numbers"], SETTINGS["hash"])
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


@pytest.mark.parametrize("path", ["parametrs_cardssss.json"])
def test_read_json(path):
    with pytest.raises(Exception):
        read_json(path)


def test_write_file():
    path = "card/card.json"
    data = [1, 2, 3]
    write_file(path, data)
    assert not os.path.exists(path)


def test_graphing():
    graphing(SETTINGS["hash"], SETTINGS["bins"], SETTINGS["last_numbers"])
    with open("card.json") as json_file:
        data = json.load(json_file)
    assert data["card_number"] == "4466747458361378"
    assert os.path.isfile("graph.png")


@pytest.mark.parametrize(("a", "sigma2", "gamma", "n", "accuracy"),
                         [(5.0, 2.0, 0.99, 25, 0.001), (15.0, 3.5, 0.85, 40, 0.001), (50.0, 10.0, 0.95, 30, 0.001)])
def test_find_expectation(a, sigma2, gamma, n, accuracy):
    sample = np.random.normal(loc=a, scale=np.sqrt(sigma2), size=n)
    left, right = find_expectation(sample, gamma, np.sqrt(sigma2))
    expected_left, expected_right = sts.norm.interval(gamma, loc=sample.mean(), scale=np.sqrt(sigma2)/np.sqrt(n))
    assert np.isclose(left, expected_left, rtol=accuracy)
    assert np.isclose(right, expected_right, rtol=accuracy)


@pytest.mark.parametrize(("a", "sigma2", "gamma", "n", "accuracy"),
                         [(5.0, 2.0, 0.99, 25, 0.001), (15.0, 3.5, 0.85, 40, 0.001), (50.0, 10.0, 0.95, 30, 0.001)])
def test_find_expectation_no_dis(a, sigma2, gamma, n, accuracy):
    sample = np.random.normal(loc=a, scale=np.sqrt(sigma2), size=n)
    left, right = find_expectation_no_dis(sample, gamma)
    expected_left, expected_right = sts.t.interval(gamma, df=n - 1, loc=sample.mean(),
                                                   scale=np.sqrt(st.pvariance(sample)) / np.sqrt(n))
    assert np.isclose(left, expected_left, rtol=accuracy)
    assert np.isclose(right, expected_right, rtol=accuracy)
