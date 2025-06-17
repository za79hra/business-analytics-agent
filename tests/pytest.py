import pytest
from biz_insight_agent.nodes import input_node, processing_node
from biz_insight_agent.utils import calculate_cac


def test_input_node_invalid():
    with pytest.raises(ValueError):
        input_node({})

    with pytest.raises(ValueError):
        input_node({"input_data": "not a dict"})


def test_processing_node_missing_keys():

    with pytest.raises(ValueError):
        processing_node({"input_data": {"yesterday": {}}})


    with pytest.raises(ValueError):
        processing_node({"input_data": {
            "today": {"cost": 10, "customers": 5},
            "yesterday": {"revenue": 100, "cost": 50, "customers": 3}
        }})


def test_processing_node_wrong_types():
    with pytest.raises(TypeError):
        processing_node({"input_data": {
            "today": {"revenue": "100", "cost": 50, "customers": 5},
            "yesterday": {"revenue": 100, "cost": 50, "customers": 3}
        }})


def test_calculate_cac_zero_customers():

    assert calculate_cac(100, 0) == 0.0
    assert calculate_cac(100, -5) == 0.0

