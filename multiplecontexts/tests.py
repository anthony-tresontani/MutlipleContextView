"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.shortcuts import render_to_response

from django.views.generic.base import  View
from django.test.client import RequestFactory
from django.template import Template
from django.http import HttpResponse
from extra_context import ExtraContext
from views import  MultipleContextMixin,ContextProvider

from django.test import TestCase

class Bang(ContextProvider):
    def get_context(self,request,*args,**kwargs):
        return {"She": "Bang"}

class ReBang(ContextProvider):

    def get_context(self,request,*args,**kwargs):
        return {"reBing": "Bing"}

class AddString(ContextProvider):

    def get_context(self,request,text):
        return {"new":text}

class NoneProvider(ContextProvider):
    pass

class TestView(MultipleContextMixin):
    extra_context = (Bang,ReBang,AddString)

    def get(self, request, *args, **kwargs):
        t = Template("Base sample: {{foo}} and {{She}} and {{reBing}} and {{new}}")
        context = ExtraContext(request, self, {"foo": "bar"},*args,**kwargs)
        return HttpResponse(t.render(context))

class RealView(MultipleContextMixin):
    extra_context = (Bang,ReBang,AddString)

    def get(self,request,text=None):
        return render_to_response("test/test.html",ExtraContext(request,self,{"foo": "bar"},text=text))

class SimpleView(View):

    def get(self,request):
        return render_to_response("test/test.html",ExtraContext(request,self,{"foo": "bar"}))

class ViewTest(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        self.view = TestView()

    def test_it(self):
        response = self.view.get(self.request,text="toto")
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "bar")
        self.assertContains(response, "Bang")
        self.assertContains(response, "Bing")

    def test_with_params(self):
        s = "toto"
        response = self.view.get(self.request,text=s)
        self.assertContains(response, s)

    def test_real(self):
        view = RealView()
        response = view.get(self.request,text="titi")
        self.assertContains(response,"titi")

        RealView.extra_context += (NoneProvider,)
        self.assertRaises(NotImplementedError,view.get,self.request,text="titi")

    def test_simple(self):
        """ If extraContext is used without a MutlitpleContextView mixin,
            that should also work.
        """
        view = SimpleView()
        response = view.get(self.request)
        self.assertEqual(response.status_code,200)