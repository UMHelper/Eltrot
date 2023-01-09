from data.msg import Msg, Error, TestMsg
import requests

BBS_URL='https://test.umbbs.xyz/'
def verifyEmail(token,userid):
    try:
        r=requests.get(
        url="{}{}{}".format(BBS_URL,'api/users/',userid),
        headers={
            'authorization': "{}{}".format("Token ",token)
            }
        )
        res=r.json()['data']['attributes']
        if 'isEmailConfirmed' in res and 'email' in res:
            return res['isEmailConfirmed'], res['email']
        return False,""
    except Exception:
        return False,""

def check_account_status(func):
    def warp(request):
        token=""
        userid=""
        if 'bbs_token' in request.COOKIES and 'bbs_userid' in request.COOKIES:
            token=request.COOKIES['bbs_token']
            userid=request.COOKIES['bbs_userid']
            isEmailConfirmed, email=verifyEmail(token=token,userid=userid)
            if isEmailConfirmed:
                return func(request)
            else:
                return Msg.error(Error.LOGIN)
        else:
            return Msg.error(Error.LOGIN)
    return warp



        