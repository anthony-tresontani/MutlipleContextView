from django.template import RequestContext

# Create your views here.
class ExtraContext(RequestContext):
    """ This subclass of RequestContext add some specific view  context.

        It's allow to not use TemplateTag to add some context variable on multiple views.
    """

    def __init__(self, request,view,dict=None, processors=None, current_app=None, use_l10n=None,*args,**kwargs):
        RequestContext.__init__(self,request, dict, current_app=current_app, use_l10n=use_l10n)
        if view is not None and hasattr(view,"get_view_processors"):
            for processor in view.get_view_processors():
                p = processor()
                new_context = p.get_context(request,*args,**kwargs)
                if new_context is not None:
                    self.update(p.get_context(request,*args,**kwargs))
