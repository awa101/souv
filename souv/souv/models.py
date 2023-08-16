from django_countries.fields import CountryField
from django.db import models
import pytz
from datetime import datetime


class Country(models.Model):
    country = CountryField()

    @property
    def timezone(self):
        timezones = pytz.country_timezones.get(self.country.code)
        return timezones[0] if timezones else None

    def get_current_time(self):
        tz = pytz.timezone(self.timezone) if self.timezone else pytz.utc
        return datetime.now(tz)
    
    def __str__(self):
        return self.country.name
    

'''
{{ country.country.name }}  <!-- 전체 국가 이름, 예: "South Korea" -->
{{ country.country }}       <!-- 국가 코드, 예: "KR" -->
{{ country.country.flag }}  <!-- 국가 플래그의 유니코드 이모지, 예: 🇰🇷 -->
'''

class Gift(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='gifts/')

    def __str__(self):
        return self.name