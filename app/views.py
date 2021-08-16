from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template import loader
from .forms import *
from authentication.forms import *
from .models import *
import json
# from .forms import *

# Create your views here.

@login_required(login_url="/login/")
def home(request):
    

    context = {}
    context['segment'] = 'home'

    html_template = loader.get_template('home.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def new_debate(request):
    form = newDebateForm()
    try:
        if request.method =='POST':
            title = request.POST.get('title')
            text = request.POST.get('text')
            disc = Discussion.objects.create(title=title, text=text, owner=request.user)
            print('Done')
        else:
            print('Error')
    except Exception as e:
        pass

    context = { 'form':form }

    html_template = loader.get_template('newdebate.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def discussion(request,pk):
    d = None
    prt1 = None
    prt2 = None
    debates = None
    sum = 0
    disc = Discussion.objects.get(id=pk)
    print('a: ', disc.participant2)
    cl = Claim.objects.all().filter(for_discussion=disc)
    com = Comment.objects.all().filter(Q(for_claim=disc) , Q(is_deleted=False))
    # form = newDebateForm(instance=disc)
    try:
        if request.method =='POST':
            
            if 'formotion' in request.POST:
                if disc.participant1 is None and disc.participant2 != request.user:
                    Discussion.objects.filter(id=pk).update(participant1=request.user)
                    # if disc.participant1 == request.user and disc.participant1 != disc.participant2:
                    d = User.objects.filter(email = request.user.email)
                    print('Debates: ', d[0].debates)
                    debates = d[0].debates + 1
                    d.update(debates=debates)
            elif 'againstmotion' in request.POST:
                if disc.participant2 is None and disc.participant1 != request.user:
                    Discussion.objects.filter(id=pk).update(participant2=request.user)
                    # if disc.participant2 == request.user and disc.participant2 != disc.participant1:
                    d = User.objects.filter(email = request.user.email)
                    print('Debates2: ', d[0].debates)
                    debates = d[0].debates + 1
                    d.update(debates=debates)
            if 'participant_post' in request.POST:
                cftext = request.POST.get('cftext')
                catext = request.POST.get('catext')
                print('text1: ', cftext)
                print('text: ', catext)
                if cftext:
                    if disc.participant1 is None and disc.participant2 != request.user:
                        Discussion.objects.filter(id=pk).update(participant1=request.user)
                        # if disc.participant1 == request.user and disc.participant1 != disc.participant2:
                        d = User.objects.filter(email = request.user.email)
                        print('Debates: ', d[0].debates)
                        debates = d[0].debates + 1
                        d.update(debates=debates)
                    if disc.participant1 == request.user and disc.participant1 != disc.participant2:
                        claim = Claim.objects.create(owner=request.user, ctype=1, text=cftext, for_discussion=disc)
                        print('Done1')
                if catext:
                    print('in catext')
                    if disc.participant2 is None and disc.participant1 != request.user:
                        Discussion.objects.filter(id=pk).update(participant2=request.user)
                        # if disc.participant2 == request.user and disc.participant2 != disc.participant1:
                        d = User.objects.filter(email = request.user.email)
                        print('Debates2: ', d[0].debates)
                        debates = d[0].debates + 1
                        d.update(debates=debates)
                    if disc.participant2 == request.user and disc.participant2 != disc.participant1:
                        print('in if')
                        claim = Claim.objects.create(owner=request.user, ctype=2, text=catext, for_discussion=disc)
                        print('Done')
            if 'admin_post' in request.POST:
                winner = request.POST.get('winner')
                wpoints = request.POST.get('wpoints')
                print('Points is: ', wpoints)
                print('Points is: ', type(wpoints))
                prt1 = User.objects.get(email=winner)
                wpoints = int(wpoints) + prt1.points
                sum += prt1.debates_won
                print('sum: ', sum)
                User.objects.filter(email=winner).update(points=wpoints, debates_won=sum)
                Discussion.objects.filter(id=pk).update(winner=prt1, loser=disc.participant2)
                print('Winner declared')
            if 'comment_post' in request.POST:
                comment = request.POST.get('comment')
                prt2 = Comment.objects.create(owner=request.user, text=comment, for_claim=disc)
                print('Comment created')
            col_com = request.POST.get('col_com')
            if col_com != '':
                print('in col_com', type(col_com))
                prt2 = Comment.objects.all().filter(id=col_com)
                prt2.update(is_deleted=True)
                print('User: ', prt2)
                msg = 'Comment is deleted successfully'
                context = {'msg': msg,'success':True,'url':'/discussion/'+pk+'/'}
                html_template = loader.get_template('includes/alert.html')
                return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        pass

    context = { 'disc':disc, 'cl':cl, 'com':com }

    html_template = loader.get_template('discussion.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def debates(request):
    disc= None
    if request.user.user_type == "1" or request.user.is_superuser:
        disc = Discussion.objects.all().filter(is_deleted=False)
    if request.user.user_type == "3":
        print('in debater')
        disc = Discussion.objects.all().filter(Q(participant1=request.user) | Q(participant1=request.user) | Q(is_deleted=False))
        print('disc: ', disc)
    try:
        if request.method == 'POST':
            pk = request.POST.get('pk')
            if pk != '':
                print('in pk')
                disc = Discussion.objects.all().filter(id=pk)
                disc.update(is_deleted=True)
                print('User: ', disc)
                msg = 'Debate is deleted successfully'
            context = {'msg': msg,'success':True,'url':'/debates/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
    except Exception as e:
        print('Exception: ', e)
        pass
    context = { 'disc':disc }

    html_template = loader.get_template('debates.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def profile(request, pk=None):
    usr1 = None
    if pk:
        usr = User.objects.get(id=pk)
        disc = Discussion.objects.all().filter(Q(participant1=usr) | Q(participant2=usr))
    else:
        usr = request.user
        disc = Discussion.objects.all().filter(Q(participant1=request.user) | Q(participant2=request.user))
    disc1 = disc.count()
    form = UserForm(instance=usr)
    try:
        if request.method == 'POST':
            usr_type = request.POST.get('user_type')
            usr1 = User.objects.filter(id=usr.pk)
            usr1.update(user_type=usr_type)
            print('Update done')
    except Exception as e:
        print('Exception: ', e)
        pass
    context = { 'disc':disc, 'disc1':disc1, 'usr':usr, 'form':form }

    html_template = loader.get_template('profile.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def users(request):
    if request.user.is_superuser or request.user.user_type == '1':
        usr = User.objects.all().filter(Q(user_type=1) | Q(user_type=2) | Q(user_type=3))
    else:
        usr = User.objects.all().filter(user_type=3)
    try:
        if request.method == 'POST':
            pk = request.POST.get('pk')
            ban_pk = request.POST.get('ban_pk')
            print('Ban', ban_pk)
            print('Pk', pk)
            if pk != '':
                print('in pk')
                usr = User.objects.all().filter(id=pk)
                usr.update(is_deleted=True)
                print('User: ', usr)
                msg = 'User is deleted successfully'
            if ban_pk != '':
                print('in ban_pk', ban_pk)
                usr = User.objects.filter(id=ban_pk)
                if usr[0].is_banned == False:
                    usr.update(is_banned=True)
                    msg = 'User is banned successfully'
                else:
                    usr.update(is_banned=False)
                    msg = 'Ban removed successfully'
                print('User: ', usr)
            context = {'msg': msg,'success':True,'url':'/users/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
    except :
        pass
    context = { 'usr':usr }

    html_template = loader.get_template('users.html')
    return HttpResponse(html_template.render(context, request))


def jsonupdates(request):
    print('pk is: ', request.GET)
    disc = None
    # try:
    #     if pk == 1:
    #         disc = Discussion.objects.all().filter(loser=request.user).count()
        
    # except print(0):
    #     pass
    a = {}
    

    data = json.dumps(a, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')