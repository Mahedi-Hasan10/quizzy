from django.contrib import admin
from .models import Quiz,QuesModel,user_history,UserReviewModel
# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display =['title','slug','description','category','created_date','modified_date','has_time_limit']
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Quiz,QuizAdmin)
class QuesModelAdmin(admin.ModelAdmin):
    list_display =['question','quiz','option1','option2','option3','option4','answer']
    
admin.site.register(QuesModel,QuesModelAdmin)

class UserHistoryModelAdmin(admin.ModelAdmin):
    list_display =['user','quiz','correct','wrong','total','parcentage','date_taken']
    
admin.site.register(user_history,UserHistoryModelAdmin)

class UserReviewModelAdmin(admin.ModelAdmin):
    list_display =['user','quiz','rating','details','created_at']
    
admin.site.register(UserReviewModel,UserReviewModelAdmin)