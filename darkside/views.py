from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .forms import RecruitForm, ResultTestForm
from .models import Recruit, Sith, Test, Question, ResultTest
from django.forms import formset_factory
from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):                                                 #Главная
    return render(request, 'darkside/index.html')

class RecruitCreateView(CreateView):                                #Класс для вывода формы добавления нового рекрута
    ownrecruit = None                                               #В случае валидной формы, редиректим на страницу прохождения теста
    template_name = 'darkside/recruit.html'
    form_class = RecruitForm
    success_url = 'darkside/test.html'

    def form_valid(self, form):                                 
        self.ownrecruit = form.save()
        self.request.session['recruit'] = self.ownrecruit.id        #На странице теста понадобится рекрут которого создали, закидываем в сессию
        return redirect('test')


def Sithview(request):                                              #функция страницы для выбора ситха из списка
    if request.method == "POST":                                    #Если POST получаем выбранного ситха   
        sithid = int(request.POST['selectsith'])                    #и редиректим на просмотр рекрутов
        request.session['sithid'] = sithid
        return redirect('viewrecruits')
    else:                                                           #Если get формируем контекст из ситхов
        setsith = Sith.objects.all()
        context = {
            'setsith':setsith,
        }
        return render(request,'darkside/sith.html',context)


def viewrecruits(request):                                          #функция просмотра рекрутов прошедших тест
    if 'sithid' not in request.session:                             #Если ситх не выбран редиректим обратно
        return redirect('sith')

    findrecruitid = ResultTest.objects.filter(recruit__handshadow = None).values('recruit').distinct()
                                                                    #Не нашёл, как делать красивую группирову group_by,  
                                                                    #пришлось вытаскивать по колонке recruit и ставить уникальность.
    findrecruit = []                                                #Так как 'values' предоставляет только ключ-значение(id), будем делаеть ещё один запрос с get-ом по id
    for i in findrecruitid:
        findrecruit.append(Recruit.objects.get(id = i['recruit']))  #Не оптимально, запрос в цикле (но работает)

    context = {'findrecruit':findrecruit}
    return render(request, 'darkside/viewrecruits.html',context)


def detailrecruit(request,idrecruit):                               # Просмотр ответов рекрута
    findrecruit = Recruit.objects.get(id=idrecruit)
    if request.method == "POST":
        findsith = Sith.objects.get(id = request.session['sithid'])

        findrecruit.handshadow = findsith
        findrecruit.save() 

        send_mail('Вы стали Рукой Тени!','Вы стали Рукой Тени, поздравляем.',findrecruit.email,[findrecruit.email]) #отправка письма на почту

        return HttpResponse('Рекрут зачислен Рукой Тени. Письмо отправлено.')
    else:
        findqustions = ResultTest.objects.filter(recruit=findrecruit)
        context =  {
            'findrecruit':findrecruit,
            'findqustions':findqustions
        }
        return render(request,'darkside/detailrecruit.html',context)

def viewtest(request):                                              #Формирование списка вопросов и вывод клиенту
    if 'recruit' not in request.session:                            #защита от хакеров которые переходят сразу на страницу теста без создания рекрута
        return redirect('recruit')
    else:
        ownrecruit = Recruit.objects.get(id=request.session['recruit'])
        masinitial = []
        owntest = get_object_or_404(Test, id=1)                     #Оставлю для фильтра по тесту
        questions = Question.objects.filter(test=owntest)

        for i in questions:
            masinitial.append({'question': i})

        formset = formset_factory(form=ResultTestForm,extra=0)      #Создаем набор форм

        if request.method == 'POST':
            formshtml = formset(request.POST, initial = masinitial) #Инициализируем форму и заполняем данными из POST
            if formshtml.is_valid():
                for form in formshtml.forms:
                    form.save(ownrecruit)                           #Если форма валидна, сохраняем. Передаем аргументом рекрута под которым прошли тест
                return HttpResponse('Успешно!')
        else:
            formshtml = formset(initial = masinitial)               #Инициализируем форму и заполняем данными из БД
            context = {
                'formshtml': formshtml,
            }
            return render(request, 'darkside/test.html', context)