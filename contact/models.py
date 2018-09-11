from django.db import models


class Message(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Ad')
    last_name = models.CharField(max_length=100, verbose_name='Soyad')
    email_address = models.EmailField(verbose_name='Eposta Adresi')
    phone_number = models.CharField(max_length=18, verbose_name='Telefon Numarası')
    subject = models.CharField(max_length=255, verbose_name='Konu')
    message = models.TextField(verbose_name='Mesajınız')
    published_at = models.DateTimeField(verbose_name='Gönderilme Tarihi', auto_now_add=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    full_name = property(get_full_name)

    class Meta:
        ordering = ['-id']
        db_table = 'messages'
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'

    def __str__(self):
        return self.subject
