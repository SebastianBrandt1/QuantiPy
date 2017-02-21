from abc import abstractmethod, ABCMeta
from quantipy.basics.event import SignalEvent

def create_system_result(**kwargs):
    result = {
        "id": "",
        "system_id": "",
        "profit_factor": 0.0,
        "no_trades": 0,
        "no_trades_win": 0,
        "no_trades_loss": 0,
        "ratio_win_loss": 1.0,
        "ratio_gain_lose": 1.0,
        "avg_win_money": 0.0,
        "avg_loss_money": 0.0,
        "max_win_money": 0.0,
        "max_loss_money": 0.0,
        "max_drawdown_money": 0.0,
        "max_drawdown_pct": 0.0,
        "max_consec_win": 0,
        "max_consec_loss": 0,
        "avg_trade_duration": 0,
        "avg_win_duration": 0,
        "avg_loss_duration": 0}

    if kwargs:
        for key, value in kwargs.items():
            result[key] = value

    return result


def create_system_parameter(**kwargs):
    parameter = {
        "id": "",
        "paramater_group_id": "",
        "name": "",
        "type": "",
        "value_low": "",
        "value_high": ""}

    if kwargs:
        for key, value in kwargs.items():
            parameter[key] = value

    return parameter


class BaseSystem(object):
    """ This class is the base class for all analytical systems """

    __metaclass__ = ABCMeta


    def set_parameters(self, **kwargs):
        pass

    @abstractmethod
    def calculate(self, event):
        raise NotImplementedError("Calculate() should be implemented in system class")



