from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from category.models import Category
from .models import Quiz,QuesModel,user_history ,UserReviewModel
from .forms import UserReviewForm

# Create your views here.
def all_quiz(request,category_slug=None):
    quizes = None
    if category_slug is not None:
        print(category_slug)
        quizes = Quiz.objects.filter(category__slug=category_slug)
    else:
        quizes = Quiz.objects.all()  
   
    # # quizes = Quiz.objects.all()   
    categories = Category.objects.all()
    # for i in categories:
    #     print(i.slug)
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
    if request.user.is_authenticated:
        history = user_history.objects.filter(user=request.user).exists()
        print(history)
        total = 0
        total_progress = 0
        if history:
            history = user_history.objects.filter(user=request.user)
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
    total = len(review)
    count = 0
    for i in review:
        count += int(i.rating)
    average = count/total
    print(average)
    return render(request,'review.html',{'reviews':review,'count':average})

def add_review(request):
    if request.method =="POST":
        form = UserReviewForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            form.save()
            return redirect('profile') 
    else:
        form = UserReviewForm()
        
    return render(request,'add_review.html',{'form':form})
    