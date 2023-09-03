from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from category.models import Category
from .models import Quiz,QuesModel,user_history ,UserReviewModel
from .forms import UserReviewForm

# Create your views here.
def all_quiz(request):
    # print(category_slug)
    # category = None
    # quizes = None
    # if category_slug:
    #     category = get_object_or_404(Category, slug = category_slug)
    #     quizes = Quiz.objects.filter(category=category)
    # else:
    #     quizes = Quiz.objects.all()  
    # for i in quizes:
    #     print(i)  
    quizes = Quiz.objects.all()   
    categories = Category.objects.all()
    # for i in categories:
    #     print(i)
    return render(request,'quiz.html',{'categories':categories,'quizes':quizes})

    
def question(request,quiz_slug):
    quiz = Quiz.objects.get(slug=quiz_slug)
    questions=QuesModel.objects.filter(quiz=quiz)
    if request.method == 'POST':
        # print(request.POST)
        score=0
        wrong=0
        correct=0
        total=0
        parcent = 0
        for q in questions:
            total+=1
            # print(request.POST.get(q.question))
            # print(q.answer)
            # print()
            if q.answer ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        
        history = user_history.objects.create(
            user=request.user,
            quiz = quiz ,
            correct = correct,
            wrong = wrong,
            total = total,
            parcentage =percent,
            
        )
        history.save()
        return render(request,'result.html',context)    
    return render(request,'question.html',{'questions':questions})

def user_total_history(request):
    history = user_history.objects.filter(user=request.user)
    # print(history)
    return render(request,'history.html',{'history':history})


def progress(request):
    history = user_history.objects.filter(user=request.user)
    total = 0
    for i in history:
        total+=i.parcentage
    total_progress = total / len(history)
    
    context ={
        'progress':total_progress,
        'history':history,
    }
    return render(request,"progress.html",context)


#leaderboard=====
def leaderboard(request,quiz_id):
    history = user_history.objects.filter(quiz=quiz_id).order_by('-parcentage')
    print(history)
    return render(request,'leaderboard.html',{'history':history})


# Review Part ================
def review(request,quiz_id):
    review = UserReviewModel.objects.filter(quiz=quiz_id)
    print(quiz_id)
    total = len(review)
    count = 0
    for i in review:
        count += int(i.rating)
    average = count/total
    print(average)
    return render(request,'review.html',{'reviews':review,'count':average})

def add_review(request):
    intaial_data = {
        'user': request.user,
    }
    form = UserReviewForm(initial=intaial_data)
    user_review = UserReviewModel.objects.all()

    
    quiz = request.POST.get('quiz')
    # new_quiz = Quiz.objects.get(id = quiz)
    rating = request.POST.get('rating')
    details = request.POST.get('details')
    
    # user_review.create(
    #     user = request.user,
    #     quiz = quiz,
    #     rating = rating,
    #     details= details,
    # )
    # user_review.save()
    print(request.user)
    print(quiz)
    print(rating)
    print(details)
    # review_create.save()
    return render(request,'add_review.html',{'form':form})
    