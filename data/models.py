from django.db import models
from enum import Enum
import uuid

class File(models.Model):

    class Type(Enum):
        NOTES='Notes'
        TEST='Test'
        ASSIGNMENT='Assignment'
        ESSAY='ESSAY'
        SLIDES='Slides'
        OTHER='OTHER'

    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    course_code=models.CharField(max_length=1024)
    course_title=models.CharField(max_length=1024)
    type=models.CharField(max_length=1024)
    ext=models.CharField(max_length=1024)
    size=models.FloatField()

    url=models.CharField(max_length=1024)
    pic_url=models.CharField(max_length=1024)

    upload_by=models.IntegerField()
    upload_at=models.DateTimeField()

    upvote=models.IntegerField()
    downvote=models.IntegerField()

    last_download_at=models.DateTimeField()
    last_download_by=models.IntegerField()

    download_count=models.IntegerField()

    def dcit(self)->dict:
        content={
            'uid':self.uid,
            'course_code':self.course_code,
            'course_title':self.course_title,
            'type':self.type,
            'ext':self.ext,
            'size':self.size,
            'pic_url':self.pic_url,
            'upload_by':self.upload_by,
            'upload_at':self.upload_at,
            'upvote':self.upvote,
            'downvote':self.downvote,
            'download_count':self.download_count
        }
        return content

class Vote(models.Model):

    class Val(Enum):
        UP=1
        DOWN=-1

    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    user=models.IntegerField()
    file=models.OneToOneField(File,on_delete=models.CASCADE)

    val=models.IntegerField()

    create_at=models.DateTimeField()

class Comment(models.Model):

    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    user=models.IntegerField()
    file=models.OneToOneField(File,on_delete=models.CASCADE)

    content=models.TextField()

    create_at=models.DateTimeField()

    def dict(self)->dict:
        content={
            'uid':self.uid,
            'create_by':self.user,
            'create_at':self.create_at,
            'content':self.content
        }
        return content

class User(models.Model):
    id=models.IntegerField(primary_key=True, editable=False, unique=True)

    upload_num=models.IntegerField()

    download_num=models.IntegerField()

    downloadable_count=models.IntegerField(default=10)

    total_upvote=models.IntegerField()
    total_downvote=models.IntegerField()

    def dict(self,with_downloadable_count=False)->dict:
        content={
            'id':self.id,
            'upload_num':self.upload_num,
            'download_num':self.download_num,
            'total_upvote':self.total_upvote,
            'total_downvote':self.total_downvote,
        }
        if with_downloadable_count:
            content['downloadable_count']=self.downloadable_count
        
        return content

class DownloadRecord(models.Model):

    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    file=models.OneToOneField(File,on_delete=models.CASCADE)
    by=models.IntegerField()

    at=models.DateTimeField()

    


