from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from soul.views import send_favmail
from website.models import Blog
from django.template.loader import render_to_string


def index(request):
    template_used = 'website/index.html'

    blog_items = Blog.objects.filter(active=True).values('id', 'title', 'url', 'image_link')

    return render(request, template_used, {
                                'static_url': settings.STATIC_URL,
                                'sub_url': settings.SUB_URL,
                                'facebook_url': settings.FACEBOOK_URL,
                                'twitter_url': settings.TWITTER_URL,
                                'blog_items': blog_items
                                })


def contact(request):
    template_used = 'website/contact.html'
    return render(request, template_used, {
                                'static_url': settings.STATIC_URL,
                                'sub_url': settings.SUB_URL,
                                'facebook_url': settings.FACEBOOK_URL,
                                'twitter_url': settings.TWITTER_URL
                                })


def contact_post(request):
    if request.POST:
        template_used = 'mail/mail.html'
        to_email = request.POST.get('email', '')
        name = request.POST.get('first_name', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        comapny = request.POST.get('company', '')
        text_message = request.POST.get('text_area', '')
        message = render_to_string(template_used, {
            'email': to_email,
            'name': name,
            'city': city,
            'phone': phone,
            'comapny': comapny,
            'text_message': text_message
        })

        if to_email:
            send_favmail('hi', message, [to_email], is_html_message="True")
        return HttpResponseRedirect('/')
