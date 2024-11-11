from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PartnerStatus
from django.core.paginator import Paginator


@login_required
def partner_list(request):
    partners = PartnerStatus.objects.filter(user=request.user)
    paginator = Paginator(partners, 4)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'partners/index.html', 
                  {'page_obj': page_obj, 
                   'user_balance': request.user.profile.points_balance})

@login_required
def redeem(request, partner_status_id):
    partner_status = get_object_or_404(PartnerStatus, pk=partner_status_id)
    if partner_status.user != request.user:
        messages.error(request, 'Ви не маєте доступу до цього партнера')
    elif request.user.profile.points_balance < partner_status.partner.points_required:
        messages.error(request, 'Нажаль у вас недостатньо бонусів')
    else:
        success = partner_status.redeem()
        if success:
            request.user.profile.points_balance -= partner_status.partner.points_required
            request.user.profile.save()
            messages.success(request, 'Ура! Ви успішно використали бонуси')
        else:
            messages.error(request, 'Немає доступних промокодів')
    return redirect('partner_list')