from django.contrib import admin

from .models import Flat, Complaint, Owner

class FlatInline(admin.TabularInline):
    model = Owner.owned_flat.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = (
        'address', 'price', 'new_building',
        'construction_year', 'town'
    )
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [FlatInline,]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complained_flat', 'user')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owner_pure_phone')
    raw_id_fields = ('owned_flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
