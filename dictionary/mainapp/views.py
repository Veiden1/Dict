from django.shortcuts import render, redirect


# Create your views here.
def indexpage(request):
    return render(request, "index.html", {"articles": []})

def wordspage(request,):
    with open('./mainapp/files/words.txt', 'r', encoding="utf-8") as file:
        lines = [line[:-1].split(" ") for line in file]
        print(type(lines))
    return render(request, "words.html", context={"words": lines})

def add_words(request):
    if request.method == 'GET':
        return render(request, "add_words.html")
    else:
        print("------------------------------------------")
        print(f'{request.POST['rus']} {request.POST['eng']}')
        with open("./mainapp/files/words.txt", 'a', encoding='utf-8') as file:
            file.writelines(f'{request.POST['rus']} {request.POST['eng']}\n')
        return(redirect(indexpage))
