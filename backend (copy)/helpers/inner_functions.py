# from django.core.paginator import Paginator
from subjects.models import SubjectRegistered


def compare_course_entry(u,s,l2):
    r=SubjectRegistered.objects.filter(student=u,subject=s).values_list('student','subject').distinct()
    l1=[]
    print('compare_result_entry '+str(r))
    for r in r:
        for r in r:
            l1.append(int(r))
    
        print("list "+str(l1)+"and "+str(l2))
        if (l1==l2):
            return 1
        l1=[]
    return 0


# def pagenate(request,query,num=None):
#     paginator = Paginator(query, num) # Show 25 contacts per page.
#     page_number = request.GET.get('page')
#     object_list = paginator.get_page(page_number)
#     return object_list