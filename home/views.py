from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from templates.formtemplate import BoardForm
from home.models import Board

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
            return render(request, 'home.html', context)

    return render(request, 'home/dashboard.html', context)


@login_required(login_url='login')
def board_details(request, pk):

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'home.html')

    if request.method == 'DELETE':
        board = Board.objects.get(pk=pk)
        board.delete()
        return render(request, 'home.html')

    if request.method == 'PUT':
        board = Board.objects.get(pk=pk)
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'home.html')

    if request.method == 'UPDATE':
        board = Board.objects.get(pk=pk)
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'home.html')

    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'home/board_details.html', context)