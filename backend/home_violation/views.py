# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from home_violation import models
# from home_violation.models import vid_stream_violations, vid_stream_cameras
# from django.core.paginator import Paginator
# from django.shortcuts import render
# #from django.db.models import RawSQL



# # from django.template import loader
# # Create your views here.
# def home(request):
#      return render(request, "home/home.html")
# #---------------------table logic--------------------------------
# def ppe(request):
     
#      via1 = vid_stream_violations.objects.all()
#      count = vid_stream_violations.objects.all().count()
#      # count_time = vid_stream_violations.objects.all().count()
#      paginator = Paginator(via1, 10)
#      page_number =request.GET.get('page')
#      via1 = paginator.get_page(page_number)

#      loc1 = vid_stream_cameras.objects.distinct()

#      # sql = "SELECT a.camera,a.cam_location,c.* FROM home_violation_vid_stream_cameras as a INNER JOIN public.home_violation_vid_stream_violations as c on a.id = c.'viol_camera_id' where viol_camera_id=1"
#      # print("1")
#      # print(sql)





#      # print(q1) 

#      context = {'via1':via1,'count': count, 'loc1':loc1,}
#      return render(request, 'Personal_Protective_Equipment/ppe.html', context )
# #-----------------------end table logic--------------------------------
# def camera1(request):
#      return render(request, 'Camera-1/')

# def dropdownsearch(request):
#     if request.method=="POST":
#         searchlocation=request.POST.get('loc1')
#         searchcamera=request.POST.get('camera1')
        
#      #    sql = "SELECT a.camera,a.cam_location,c.* FROM home_violation_vid_stream_cameras as a INNER JOIN public.home_violation_vid_stream_violations as c on a.id = c.'viol_camera_id' where viol_camera_id=1"
#      #    print("1")
#      #    print(sql)


#      #    dropdownsearch.execute(sql)

#      #    myresult = mycursor.fetchall()

#      #    for x in myresult:
#      #        print(x)

#      #    que = vid_stream_cameras INNER JOIN public.home_violation_vid_stream_violations as c on a.id = c."viol_camera_id
#      #    que = user.object.raw("SELECT a.camera,c.viol_camera_id FROM home_violation_vid_stream_cameras as a INNER JOIN public.home_violation_vid_stream_violations as c on a.id = c."viol_camera_id"")

#      #    tableque = vid_stream_cameras.objects.filter(vid_stream_violations__viol_camera_id=models.F('id')).values('camera', 'vid_stream_violations__viol_camera_id')

#         tablesearch=via1.objects.filter(location=searchlocation,camera1=searchcamera)
#         return render(request,'Personal_Protective_Equipment/ppe.html',{"data":tablesearch})
#     else:
#         via1 = vid_stream_violations.objects.all()
#         return render(request,'home.html',{"via1":via1})


##############################################################################################################
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from home_violation.models import vid_stream_violations, vid_stream_cameras
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
# from django.template import loader
# Create your views here.
def home(request):
     return render(request, "home/home.html")
#---------------------table logic--------------------------------
def ppe(request):
     via1 = vid_stream_violations.objects.all()
     count = vid_stream_violations.objects.all().count()
     # count_time = vid_stream_violations.objects.all().count()
     paginator = Paginator(via1, 10)
     page_number =request.GET.get('page')
     via1 = paginator.get_page(page_number)
     loc1 = vid_stream_cameras.objects.all()
     context = {'via1':via1,'count': count, 'loc1':loc1}
     return render(request, 'Personal_Protective_Equipment/ppe.html', context )
#-----------------------end table logic--------------------------------
def camera1(request):
     return render(request, 'Camera-1/')
def filter_emp(request):
    if request.method == 'POST':
        cam_location = request.POST['cam_location']
        camera = request.POST['camera']
        sql = vid_stream_cameras.objects.raw("SELECT a.camera,c.viol_camera_id FROM home_violation_vid_stream_cameras as a INNER JOIN public.home_violation_vid_stream_violations as c on a.id = c.'viol_camera_id'")
     # via1 = vid_stream_violations.objects.all()
     #    if cam_location:
     #        via1 = via1.filter(cam_location__name__icontains = cam_location)
     #        if camera:
     #           via1 = via1.filter(camera__name__icontains = camera)