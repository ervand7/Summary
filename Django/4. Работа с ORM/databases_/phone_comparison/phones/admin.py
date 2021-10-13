from django.contrib import admin

from phones.models import Phone, PhoneApple, PhoneNokia, PhoneSamsung


class PhoneAdmin(admin.ModelAdmin):
    pass


class PhoneAppleAdmin(PhoneAdmin):
    pass


class PhoneSamsungAdmin(PhoneAdmin):
    pass


class PhoneNokiaAdmin(PhoneAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneApple, PhoneAppleAdmin)
admin.site.register(PhoneSamsung, PhoneSamsungAdmin)
admin.site.register(PhoneNokia, PhoneNokiaAdmin)
