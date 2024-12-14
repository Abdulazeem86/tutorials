from django.shortcuts import render
from django.views import View


class LandingView(View):

    template_name = 'myapp/landing.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
