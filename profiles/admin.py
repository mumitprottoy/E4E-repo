from django.contrib import admin
from . import models

admin.site.register([models.Phone, models.UserStatus, models.SixDigitCode])
