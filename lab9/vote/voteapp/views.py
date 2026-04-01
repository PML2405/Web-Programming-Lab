from django.shortcuts import render

votes = {
    'good': 0,
    'satisfactory': 0,
    'bad': 0
}

# Create your views here.
def vote(request):
    percent=None
    if request.method=='POST':
        choice = request.POST.get('choice')
        if choice:
            votes[choice]+=1
        total=sum(votes.values())

        if total>0:
            percent = {
                'good': (votes['good']/total)*100,
                'satisfactory': (votes['satisfactory']/total)*100,
                'bad': (votes['bad']/total)*100,
            }

    return render(request,'vote.html',{
        'percent': percent
    })