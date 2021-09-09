from django.db import models


class Video(models.Model):
    """動画"""

    title = models.CharField('Video Title', max_length=255)
    description = models.TextField('Description', blank=True)
    thumbnail = models.ImageField('Thumbnail', upload_to='thumbnails/', null=True, blank=True)  # /media/thumbnails/ファイル名
    upload = models.FileField('File', upload_to='uploads/%Y/%m/%d/')  # /media/uploads/2018/3/20/ファイル名
    created_at = models.DateTimeField('Created Date', auto_now_add=True)  # default=timezone.nowと違い、入力欄は表示されない
    updated_at = models.DateTimeField('Modified Date', auto_now=True)  # 更新するたびにその日時が格納される

    def __str__(self):
        return self.title
