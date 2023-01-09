from data.utils import check_account_status
from data.msg import Msg, Error, TestMsg

@check_account_status
def login(request):
    return Msg.msg(TestMsg())