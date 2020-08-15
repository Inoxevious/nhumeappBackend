from django.contrib import admin
from .models import *
from mapwidgets.widgets import GooglePointFieldInlineWidget
from django.contrib.gis.db.models import PointField
class PackageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('packageOwner','reference','pickupAddressCity','deliveryAddressCity','available')
    list_filter = ('packageOwner','available')

admin.site.register(User)
admin.site.register(Rides)
admin.site.register(Package,PackageAdmin)
admin.site.register(DeliveryAddressEntity)
admin.site.register(TransactionLineItemEntity)
