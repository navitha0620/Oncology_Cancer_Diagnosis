from django.shortcuts import render
from django.http import HttpResponse,FileResponse,Http404,HttpResponseNotFound
from .models import Register
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os
from django.conf import settings

def room(request):
    return render(request,"room.html")

def aboutus(request):
    return render(request,"aboutus.html")

def patient(request):
    return render(request,"patient.html")

def visited(request):
    return render(request,"visited.html")
    
def contactus(request):
    return render(request,"contactus.html")

def actionHCG(request):
    email=request.GET['Mail']
    #firstname=request.GET['firstname']
    subject=request.GET['subject']
    hospitalname=request.GET['HospitalName']
    contact=request.GET['Phoneno']
    
    r=Register()
    r.email=email
    #r.firstname=firstname
    r.subject=subject
    r.hospitalname=hospitalname
    r.contact=contact
    r.save()
    return render(request,"contactus.html",{"msg":"Successfully Submitted"})

"""

def download_pdf(request):
    # Define the file path
    filename='download_pdf.pdf'
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    
    # Serve the file as a downloadable attachment
    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')
    except FileNotFoundError:
        # Handle the case where the file does not exist
        return HttpResponseNotFound('<h1>File not found</h1>')

"""
"""
def visited(request, filename):
    # Construct the file path
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        return HttpResponse("File not found", status=404)
    
    # Return the file response
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/pdf'  # Set the content type based on the file
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
"""
"""
# views.py
from django.http import HttpResponse, Http404
import os

def visited(request, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, 'templates', filename)

    if not os.path.isfile(filepath):
        raise Http404("File not found")

    with open(filepath, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
"""
"""
def downloadfile(request, filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, 'templates', filename)

    if not os.path.isfile(filepath):
        raise Http404("File not found")

    with open(filepath, 'rb') as f:
        response = HttpResponse(FileWrapper(f), content_type=mimetypes.guess_type(filepath)[0])
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response['Content-Length'] = os.path.getsize(filepath)
        return response


"""
"""
def download_pdf(request):
    #base_dir= os.path.dirname(os.path.abspath(__file__))
    filename='Patient -1 Ram.pdf'
    content = FileWrapper(filename)
    
    
    filepath =base_dir + 'templates/' + filename
    thefile = filepath
    filename=os.path.basename(thefile)
    chunk_size= 8192
    
    response=StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
                                   content_type=mimetypes.guess_type(thefile)[0])
    
    response = HttpResponse(content, content_type='application/pdf')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename=%s' % 'Patient -1 Ram.pdf'
    return response
"""
def view(request):
    email=request.GET['Mail']
    Name=request.GET['Name']
    UMR=request.GET['UMR']
    try:
        r=Register.objects.get(email=email,Name=Name,UMR=UMR)
    except Exception as ex:
        return render(request,"patient.html",{"msg":"Invalid Designation"})
    return render(request,"visited.html")
   # r=Register()
   # r.email=email
   # r.Name=Name
   # r.UMR=UMR
   # r.save()
   # return render(request,"visited.html",{"msg":"Successfully Submited"})

"""

    r=None
    try:
        r=Register.objects.get(email=email)
        print("r=",r)
    except Exception as ex:
        print(ex)
        return render()
    print(r!=None)
    if(r.design=="UMR")
        return redirect("")
        return render(request,"patient.html",{"msg":"Invalid Email-ID"})
"""

def logincheck2(request):
    email=request.GET['Mail']
    Name=request.GET['Name']
    UMR=request.GET['UMR']
    #password=request.GET['Password']
    #department=request.GET['department']
    #hospitalname=request.GET['HospitalName']
    #contact=request.GET['Phoneno']
   # r=None
    try:
        r=Register.objects.get(email=email)
    #    print("r=",r)
    except Exception as ex:
   #     print(ex)where 
        return render(request,"patient.html",{"msg":"Invalid Designation"})
    #if(r!=None):
     #   if(r.design=="user"):
      #      return redirect("/userhome")
       # if(r.design=="admin"):
        #    return redirect("/adminhome")
    #else:
     #   return render(request,"login.html",{"msg":"Invalid Designation"})
    #r=Register.objects.get(email=email)
    return render(request,"visited.html")

