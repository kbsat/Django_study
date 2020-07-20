from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    fulltext = request.GET['full_text']
    # 안녕하세요 반갑습니다
    word_list = fulltext.split()
    # [안녕하세요,반갑습니다,안녕하세요]
    word_dictionary = {}
    # {안녕하세요:2,반갑습니다:1}
    for word in word_list:
        if word in word_dictionary: 
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request,'result.html',{'full':fulltext,'total':len(word_list),'dictionary':word_dictionary.items()})