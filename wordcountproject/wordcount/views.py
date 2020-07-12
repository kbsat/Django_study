from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def count(request):
    full_text = request.GET['fulltext']

    wordlist = full_text.split()

    word_dictionary = {}
    
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1
    return render(request,'count.html',{'fulltext':full_text,'total':len(wordlist),'dictionary':word_dictionary.items()})