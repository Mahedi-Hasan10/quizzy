from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_quiz,name = 'categories'),
    # path('category/<slug:category_slug/',views.all_quiz,name = 'products_by_categories'),
    path('question/<slug:quiz_slug>/',views.question,name = 'question'),
    path('history/',views.user_total_history,name = 'history'),
    path('progress/',views.progress,name = 'progress'),
    path('leaderboard/<int:quiz_id>/',views.leaderboard,name = 'leaderboard'),
    path('review/<int:quiz_id>/',views.review,name = 'review'),
    path('add_review/',views.add_review,name = 'add_review'),
]