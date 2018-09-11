from django.db import models


class TeamMember(models.Model):
    first_name = models.CharField(verbose_name='Ad', max_length=100)
    last_name = models.CharField(verbose_name='Soyad', max_length=100)
    title = models.CharField(verbose_name='Ünvan', max_length=100)
    email_address = models.EmailField(verbose_name='E-posta Adresi')
    linkedin_url = models.URLField(verbose_name='Linkedin Adresi', null=True, blank=True)
    image = models.ImageField(verbose_name='Profil Fotoğrafı', null=True, blank=True)
    published_at = models.DateTimeField(verbose_name='Oluşturulma Tarihi', auto_now_add=True, editable=False)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    full_name = property(get_full_name)

    class Meta:
        db_table = 'team_members'
        verbose_name = 'Ekip Üyesi'
        verbose_name_plural = 'Ekip Üyeleri'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
