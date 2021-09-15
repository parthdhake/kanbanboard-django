from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from templates.formtemplate import BoardForm, CardForm
from home.models import Board, Card

# Create your views here.


@login_required(login_url='login')
def home(request):
    user = request.user
    form = BoardForm()

    boards = Board.objects.filter(user=user)
    # print(boards[1].id)
    context = {'user': user, 'form': form, 'boards': boards}

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'home/dashboard.html', context)

    return render(request, 'home/dashboard.html', context)


@login_required(login_url='login')
def board_details(request, pk):
    context = {}
    form = CardForm()
    context['form'] = form

    if request.user.is_authenticated:
        cards = Card.objects.filter(board=pk)
        context['cards'] = cards
        print(cards)

    if request.method == 'POST':
        form = CardForm(request.POST)
        form.instance.board = Board.objects.get(id=pk)
        form.instance.user = request.user
        # if form.instance.status == "MEDIUM":
        #     form.instance.color = "WHITE"
        # elif form.instance.status == "HIGH":
        #     form.instance.color = "RED"
        # elif form.instance.status == "LOW":
        #     form.instance.color = "GREEN"
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('board', pk=pk)

    return render(request, 'home/board_details.html', context)