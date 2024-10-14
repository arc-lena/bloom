from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Partner, PointTransaction

def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'partners/partner_list.html', {'partners': partners})


@login_required
def use_points(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    user_balance = request.user.profile.points_balance


    if user_balance >= partner.points_required:
        transaction = PointTransaction.objects.create(
            user=request.user,
            partner=partner,
            status='pending',  
        )

        request.user.profile.points_balance -= partner.points_required
        request.user.profile.points_balance.save()

        return redirect('partner_list')
    else:
        return render(request, 'some_template.html', {'error': 'Not enough points'})