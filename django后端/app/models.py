# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms import model_to_dict


class Friends(models.Model):
    userid1 = models.ForeignKey('WxUser', models.DO_NOTHING, db_column='userid1', related_name='userid1')
    userid2 = models.ForeignKey('WxUser', models.DO_NOTHING, db_column='userid2', related_name='userid2')

    class Meta:
        managed = False
        db_table = 'friends'

    def as_dict(self):
        return model_to_dict(self)


class Pyq(models.Model):
    userid = models.ForeignKey('WxUser', models.DO_NOTHING, db_column='userid')
    content = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pyq'

    def as_dict(self):
        data = model_to_dict(self, exclude=['userid'])  # 使用model_to_dict把对象转字典，并去掉其中的userid字段
        data['time'] = self.time.strftime('%Y-%m-%d %H:%M:%S')  # 时间转化
        data['wx_user'] = self.userid.as_dict()  # 将userid字段转为wx_user对象的as_dict方法，返回该对象的所有需要字段
        return data


class Review(models.Model):
    pyqid = models.ForeignKey(Pyq, models.DO_NOTHING, db_column='pyqid')
    commentsid = models.ForeignKey('WxUser', models.DO_NOTHING, db_column='commentsid')
    comments = models.CharField(max_length=255)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'

    def as_dict(self):
        data = model_to_dict(self, exclude=['commentsid'])
        data['time'] = self.time.strftime('%Y-%m-%d %H:%M:%S')
        data['wx_user'] = self.commentsid.as_dict()
        return data


class WxUser(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wx_user'

    def __str__(self):
        return self.nickname

    def as_dict(self):
        return model_to_dict(self, exclude='password')
