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
class FileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('car_id','image','owner')
    list_filter = ('car_id','owner')

class PackageFileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('package_id','file','owner')
    list_filter = ('package_id','owner')

class RidesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('reg_number','ride_category','owner')
    list_filter = ('reg_number','ride_category')
    
class DriversAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('license_number','years_experience','owner')
    list_filter = ('license_class','years_experience')
class AppVersionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('version_name','app_version','app_upload_date','app_expire_date')
    list_filter = ('app_version','app_upload_date')

admin.site.register(User)
admin.site.register(Rides,RidesAdmin)
admin.site.register(AppVersion,AppVersionAdmin)
admin.site.register(Driver,DriversAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(PackageFile,PackageFileAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(DeliveryAddressEntity)
admin.site.register(TransactionLineItemEntity)
