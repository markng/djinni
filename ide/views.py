from django.views.generic import *

class ProjectView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, *args, **kwargs):
        ctx = super(ProjectView, self).get_context_data(*args, **kwargs)
        return ctx
        