from django.contrib import admin
from .models import Partner, PointTransaction

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'points_required')

@admin.register(PointTransaction)
class PointTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'partner', 'status', 'timestamp')
    list_filter = ('status',)