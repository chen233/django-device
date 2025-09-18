from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class ProxyResource(resources.ModelResource):
    class Meta:
        model = table_view


    # Register your models here.
@admin.register(table_view)
class RecordAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):

    resource_class = ProxyResource

    list_display = (
        'id',
        # 'time_map',
        'type_map',
        'name_map',
        'type_map_choices',
        'id_map',
        'install_map',
        'install_map_1',
        'type_map',
        # 'Pixel',
        # 'night',
        'Electrical_type',
        'phone_number_map',
        'electrical_map',
        'electrical_max',
        'net_max',
        'Carrier_map',
        'image_map',
        'image_map1',
        'all_in_map',
                    )
    list_per_page = 10
    readonly_fields = ('image_map','image_map1')
    list_display_links = ('id', 'all_in_map')
