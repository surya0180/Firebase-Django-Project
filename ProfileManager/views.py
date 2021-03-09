from django.shortcuts import redirect, render
from Profiles.settings import Firebase, Database, Auth, Storage
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request, 'index.html')

def saveData(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        Data = {"firstname": firstname, "lastname": lastname}
        Fullname = firstname+lastname
        Database.child("Database").child(Fullname).set(Data)
        
        image = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        Path = "media/"+str(image.name)
        k = Storage.child("images").child(Fullname).put(Path)

    return render(request, 'index.html')

def profiles(request):
    Data = Database.child("Database").get()
    firstname=[]
    lastname=[]
    image=[]
    for data in Data.each():
        firstname.append(data.val()['firstname'])
        lastname.append(data.val()['lastname'])
        Fullname = data.val()['firstname']+data.val()['lastname']
        image_url = Storage.child("images").child(Fullname).get_url(None)
        image.append(image_url)
    
    Data = zip(firstname, lastname, image)
    return render(request, 'profiles.html', {"Data": Data})