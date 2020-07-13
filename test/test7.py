import sys
reload(sys)
sys.setdefaultencoding('utf8')
def checkchinese(check_str):
     for ch in check_str.decode('utf-8'):
         if u'\u4e00' <= ch <= u'\u9fff':
             aaaaaaaaaaaaaaaaaaaaaaa=1
         else:
             return False
     return True