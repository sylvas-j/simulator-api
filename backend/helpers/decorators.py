from django.shortcuts import redirect

# THIS FUNCTION PREVENT USER 
# FROM ACCESSING CERTAIN URL IF AUTHENTICATED
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			# print('authenticatedddddd')			
			return view_func(request, *args, **kwargs)
		else:
			# print('not authenticatedddddd')
			return redirect('home')
			

	return wrapper_func
