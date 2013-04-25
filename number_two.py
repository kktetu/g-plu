# -*- coding: utf-8 -*-

from django.db import models


class CachedMasterModel(models.Model):
    """
    キャッシュ機能を持つ Model
    更新が少ないマスターデータの管理に使用する
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super(CachedMasterModel, self).save(*args, **kwargs)
        self.delete_cache()

    def delete(self, *args, **kwargs):
        self.delete_cache()
        super(CachedMasterModel, self).delete(*args, **kwargs)

    def delete_cache(self):
        """
        get と get_all キャッシューを削除
        """
        pass
        
    @classmethod
    def get(cls, pk):
        # メソッドキャッシュを使う
        # Djangoキャッシュを使う
        return cls.objects.get(pk=pk)

    @classmethod
    def get_all(cls):
        # メソッドキャッシュを使う
        # Djangoキャッシュを使う
        return list(cls.objects.all())


class Item(CachedMasterModel):
    pass


class Player(CachedMasterModel):
    pass


class PlayerItem(models.Model):
    player_id = models.CharField(db_index=True, max_lenght=10, null=False)
    item_id = models.PositiveIntegerField(null=False)
    quantity = models.IntegerField(default=0)
    
    class Meta(object):
        unique_together = ('player_id', 'item_id')
