from django.contrib import admin


from .models import dd, md, siteDtls


from import_export.admin import ImportExportModelAdmin

#admin.site.register(pumpInstData)

# Register your models here.



@admin.register(dd)
@admin.register(md)
@admin.register(siteDtls)




class ddAdmin(ImportExportModelAdmin):
	pass

class mdAdmin(ImportExportModelAdmin):
	pass

class siteDtlsAdmin(ImportExportModelAdmin):
	pass