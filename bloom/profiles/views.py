from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from partners.models import PartnerStatus
from django.contrib.auth import logout
from .forms import ProfileForm
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Зміни на бажану URL-адресу після входу
            else:
                messages.error(request, 'Неправильне ім’я користувача або пароль.')
        else:
            messages.error(request, 'Неправильне ім’я користувача або пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})

@login_required
def info_view(request):
    return render(request, "info/index.html")

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html', {
        'user': request.user,
        'statuses': PartnerStatus.objects.filter(user=request.user, status='redeemed'), 
    })

@login_required
def profile_settings_view(request):
    user = request.user
    if request.method == 'POST':
        if 'delete_account' in request.POST:
            logout(request)
            user.delete()
            messages.success(request, "Ваш акаунт було видалено.")
            return redirect('home')
        else:
            form = ProfileForm(request.POST, instance=user)
            if 'photo' in request.FILES:
                user.profile.avatar = request.FILES['photo']
            if form.is_valid():
                form.save()
                messages.success(request, "Ваші зміни збережено.")
                return render(request, "profile_set/profile_set.html")
    else:
        form = ProfileForm(instance=user) 

    return render(request, "profile_set/profile_set.html", {'form': form})

def leaderboard_and_statistics_view(request):
    top_users = Profile.objects.filter(level__isnull=False).order_by('-level')[:5]
    completed_tasks = 150  

    return render(request, 'statistics/index.html', {
        'top_users': top_users,
        'completed_tasks': completed_tasks,
    })

def statistics(request):
    return render(request, 'statistics/index.html')


def tasks_view(request):
    return render(request, 'tasks/index.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request) 
        user.delete() 
        messages.success(request, "Your account has been deleted.")
        return redirect('home')  
    return redirect('profile')



from django.shortcuts import render

def info_view(request):
    question = request.GET.get('question')
    
    content = {
        '1': {
            'title': 'Яке пакування обрати?',
            'text': "Використовуйте перероблені матеріали: обирайте пакування з переробленого картону, паперу або пластику, щоб зменшити кількість відходів. Біорозкладне пакування: вибирайте матеріали, які розкладаються в природі, як-от кукурудзяний крохмаль або картон. Мінімізація упаковки: обирайте продукти з мінімальною кількістю упаковки або використовуйте багаторазові упаковки. Пакування з повторним використанням: використовувати матеріали, які можна багаторазово використовувати, наприклад, тканинні сумки або металеві контейнери. Вибір натуральних матеріалів: обирайте пакування з натуральних матеріалів, таких як дерево, бамбук чи скло."
        },
        '2': {
            'title': 'Як сортувати?',
            'text': '''
                <h1 id="paper">Папір</h1>
                <p>Паперові відходи включають газети, журнали, картон, офісний папір тощо. Перш ніж викидати папір, переконайтеся, що він чистий і сухий, оскільки забруднені паперові вироби можуть не підлягати переробці.</p>
                <hr class="divider-line">
                <h1 id="plastic">Пластик</h1>
                <p>Пластик слід сортувати за типами: PET (пляшки для напоїв), HDPE (флакони для миючих засобів) та інші види. Зверніть увагу на маркування на пластикових виробах, щоб визначити, як їх можна переробити.</p>
                <hr class="divider-line">
                <h1 id="glass">Скло</h1>
                <p>Скло слід розділяти за кольором (прозоре, зелене, коричневе). Ніколи не змішуйте скло з іншими відходами, і переконайтеся, що воно не містить кришок чи металевих елементів.</p>
                <hr class="divider-line">
                <h1 id="metal">Метал</h1>
                <p>До металевих відходів відносяться алюмінієві банки, жерстяні кришки, кухонне приладдя. Метал легко переробляється, але перед цим бажано його очистити від залишків їжі.</p>
                <hr class="divider-line">
                <h1 id="organic">Органічні відходи</h1>
                <p>Органічні відходи включають залишки їжі, обрізки рослин, компостовані матеріали. Їх можна використовувати для створення компосту, що зменшує кількість відходів і збагачує ґрунт.</p>
            '''
        },
        '3': {
            'title': 'Чи можна це переробити?',
            'text': 'Ось матеріали, які підлягають переробці: папір і картон (газети, коробки), пластик (пляшки, контейнери, пакети), метал (алюмінієві банки, консерви), скло (пляшки, банки), електроніка (телефони, комп’ютери), текстиль (старий одяг), батарейки та акумулятори, а також хімічні речовини (фарби, розчинники). Переробка цих матеріалів допомагає зменшити відходи та зберегти ресурси.'
        },
        '4': {
            'title': 'Поради з повторного використання',
            'text': ' Використовуйте багаторазові сумки замість пластикових, а пластикові та скляні пляшки або контейнери повторно для води чи зберігання їжі. Старий одяг можна перетворити на тряпки, сумки або передавати для повторного використання. Картонні коробки та банки слід використовувати для зберігання речей, організації простору або навіть для декору. Ці звички допоможуть вам зменшити кількість відходів і підтримувати екологічний спосіб життя.'
        }
    }
    
  
    selected_content = content.get(question, None)
    
    return render(request, 'info/index.html', {'selected_content': selected_content})

