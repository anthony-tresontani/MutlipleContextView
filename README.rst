Multiple context
================

Sometimes, you want to add to your views few other datas.
In Django, that mean addded some contexts variable throught template tags.

But what if you had to this to a lot's of widget spread over lot's of views.
Even if  template tags are great, there are not always accurate and easy to  write.
There is better to do the job.

The basic django approch is to design a view for a main purpose:
 - to see an object - DetailView
 - a list of object - ListView
 ...

 Multiple Context allow to have views focused over multiple subjects.

 You know why, let's see how:

 Installation
 ------------

 After downloading the package with Git, just apply::

    python setup.py install


 Usage
 -----

 Multiple context only apply to class-based view as it work with a Mixin.

 Let's say you have a base view::

    class MyView(View):

        def get(self,request,text):
            my_object = MyObject.objects.all()
            return render_to_response("myTemplate.html",RequestContext(request,{"my_object":my_object,"text":text}))

 And you want add to the left pane a widget with the 5 last blog post.

 You just have to:

 1. Extend the MultipleContextMixin::
 
        class MyView(View, MultipleContextMixin):

 2. Provide a ContextProvider and add it to the extra_context argument::

        class FiveLastBlogPost(ContextProvider):

            def get_context(self,request,*args,**kwargs):
                posts = BlogPosts.objects.all()[5]
                return {'posts':posts}

        class MyView(View, MultipleContextMixin):
            extra_context = (FiveLastBlogPost,)

 3. Add an ExtraContext in your render_to_response

         def get(self,request,text):
             my_object = MyObject.objects.all()
             return render_to_response("myTemplate.html",
                                        ExtraContext(request,
                                                     self,
                                                     {"my_object":my_object,"text":text},
                                                     text=text
                                                     ))

 4. That's it





 
 