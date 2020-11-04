from django.contrib import admin
from .models import HairCutting, HairColouring, LadiesWaxing, Eyebrows, WaxPackage, MensWaxing, Massage, NonPurchasable, TeamWorkOne, TeamWorkTwo, TeamWorkThree

# Register your models here.
admin.site.register(HairCutting)
admin.site.register(HairColouring)
admin.site.register(LadiesWaxing)
admin.site.register(Eyebrows)
admin.site.register(WaxPackage)
admin.site.register(MensWaxing)
admin.site.register(Massage)
admin.site.register(NonPurchasable)

admin.site.register(TeamWorkOne)
admin.site.register(TeamWorkTwo)
admin.site.register(TeamWorkThree)