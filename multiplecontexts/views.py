from django.views.generic.base import  View

class MultipleContextMixin(object):
    """ Mixin to easily integrate some additional
        contexts.

        Just define extra_context on the view.
        
        extra_context
            A tuple of ContextProvider.

        To use it on your own view, you should:
        1. Add the mixin to your class-based view
        2. Add some ContextProvider
        3. Define the extra_context class argument
        4. Add an ExtraContext in your render_to_template

        No need to include this app in your INSTALLED_APPS
    """

    def get_view_processors(self):
        return getattr(self.__class__,"extra_context",())

class ContextProvider(object):
    """ Object which add some new context to a view

        Any object which implement ContextProvider
        should define a get_context method.

        get_context
           return additional context into a Dict

        You should always let *args, **kwargs as
        arguments as every context provider for one
        class view will received same arguments
    """

    def get_context(self,request,*args,**kwargs):
        raise NotImplementedError()
