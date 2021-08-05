from django.shortcuts import reverse, HttpResponseRedirect

def is_user_logged_in(view):
  def user_wrapper(request, *args, **kwargs):
    if request.session.has_key('isLoggedIn') and request.session['isLoggedIn']:
      return view(request, *args, **kwargs)
    else:
      return HttpResponseRedirect(reverse('account:auth_login'))
  return user_wrapper