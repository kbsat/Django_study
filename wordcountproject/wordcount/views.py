from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def count(request):
    full_text = request.GET['fulltext']
    # full_text = '안녕하세요 반갑습니다'
    wordlist = full_text.split()
    # wordlist = ['안녕하세요','반갑습니다','안녕하세요']
    word_dictionary = {}
    # {key : value}  word_dictionary[key] => value 
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1   
        else :
            word_dictionary[word] = 1
            # word_dictionary {'안녕하세요':2,'반갑습니다':1}
    return render(request,'count.html',{'fulltext':full_text,'total':len(wordlist),'dictionary':word_dictionary.items()})