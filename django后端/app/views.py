import json
import operator

from app.models import Pyq, WxUser, Friends, Review
from django.core import serializers
from django.http import HttpResponse, JsonResponse


# Create your views here.


def login(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('nickname') is not None and request.POST.get('password') is not None:  # 判断用户名或密码不为空
            nickname = request.POST['nickname']
            password = request.POST['password']

            user = WxUser.objects.filter(nickname=nickname)
            if user.count():
                user = user.first()
                user_id = user.id
                if user.password == password:

                    ret = {'result': 'success', 'user_id': user_id}
                    return JsonResponse(ret)
                else:
                    return HttpResponse('password mistake!')
            else:
                return HttpResponse('user is not exist!')
        else:
            return HttpResponse('nickname or password is None!')

    else:
        return HttpResponse('need request.method POST!')


def pyq(request):
    if request.GET:  # 获取朋友圈
        userid = request.GET['userid']  # 获取用户id

        friends = Friends.objects.filter(userid1=userid)  # 根据好友列表获取好友信息

        friend_list = []  # 设置好友id列表

        for f in friends:  # 将好友id加入列表中
            friend_list.append(f.userid2.id)

        self_pyq = Pyq.objects.filter(userid=userid)  # 获取用户自己的朋友圈

        pyqs_list = [object.as_dict() for object in self_pyq]

        for f_l in friend_list:  # 把循环得到的好友的QuerySet结果存入到朋友圈列表
            friends_pyq = [object.as_dict() for object in Pyq.objects.filter(userid=f_l)]
            pyqs_list = pyqs_list + friends_pyq

        pyqs_list.sort(key=operator.itemgetter('time'), reverse=True)

        for i in pyqs_list:  # 根据朋友圈id获取评论
            i['review'] = [object.as_dict() for object in Review.objects.filter(pyqid=i['id']).order_by('time')]

        pyq_all = json.dumps(pyqs_list, ensure_ascii=False)

        return HttpResponse(pyq_all)
    else:
        ret = json.loads(request.body)
        print(ret)
        if "id" in ret:  # 删除时先删除评论，再删除朋友圈
            Review.objects.filter(pyqid=ret['id']).delete()
            Pyq.objects.filter(id=ret['id']).delete()
            return HttpResponse('delete success!')
        else:  # 增加
            userid = WxUser.objects.get(id=ret['userid'])
            Pyq.objects.create(userid=userid, content=ret['content'], time=ret['time'])
            return HttpResponse('add success!')


def review(request):
    ret = json.loads(request.body)
    if "id" in ret:  # 删除
        Review.objects.get(id=request.POST['id']).delete()
        return HttpResponse('delete success!')
    else:  # 增加
        # 外键数据项：先获取要插入的外键的对象，将对象作为外键字段插入数据库
        pyqid = Pyq.objects.get(id=ret['pyqid'])
        commentsid = WxUser.objects.get(id=ret['userid'])
        Review.objects.create(pyqid=pyqid, commentsid=commentsid, comments=ret['comments'], time=ret['time'])
        return HttpResponse('add success!')
