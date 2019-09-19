from django.contrib import admin
from .models import Customer,Task
from django.db import models
from django.forms import TextInput, Textarea

def mark_finished(modeladmin, request, queryset):
    queryset.update(is_finished=True)
mark_finished.short_description = "Mark selected tasks as finished"


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})},
    }

    fk_name = "customer"
    exclude = ['sales_rep']


class CustomerAdmin(admin.ModelAdmin):
    fieldsets =  [('Basic Info',{'fields':[('username','phone_number'),('email','address')]}),
    ('Option Inof',{'fields':[('industry','where_to_hear')]})
    ]
    inlines = [TaskInline]
    list_display = ['username','email','phone_number','created_at','address','industry']
    list_filter = ['industry']
    search_fields = ['username','email','phone_number']
    exclude = ['created_at']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'30'})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':50})},
        models.EmailField: {'widget': TextInput(attrs={'size':'30'})},
    }

    def save_model(self, request, obj, form, change):
        obj.sales_rep = request.user
        super().save_model(request, obj, form, change)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_type','sales_rep','created_at','follow_up_date','is_finished','short_notes',]
    list_filter = ['task_type','follow_up_date']
    search_fields = ['notes']
    exclude = ['created_at','sales_rep']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':45})},
    }

    date_hierarchy = 'follow_up_date'
    actions = [mark_finished]

    def save_model(self, request, obj, form, change):
        obj.sales_rep = request.user
        super().save_model(request, obj, form, change)
    
    
   
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Task,TaskAdmin)