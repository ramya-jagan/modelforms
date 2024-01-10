from django.contrib import admin

# Register your models here.
from app.models import *

class customizeWebpage(admin.ModelAdmin):
  list_display=['topic_name','name','url','email']
  list_display_links=['url']
  list_editable=['email']
  list_filter=['name']
  #list_per_page=2
  search_fields=['name']
  #list_max_show_all=2
  list_select_related=['topic_name']


admin.site.register(Topic)

admin.site.register(Webpage,customizeWebpage)

admin.site.register(AccessRecord)