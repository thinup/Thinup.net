from re import search
from django.urls import path
from app import views
from app import search
from app import forms

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sns/twitter/', views.TwitterView.as_view(), name='twitter'),
    path('sns/instagram/', views.InstagramView.as_view(), name='instagram'),
    path('sns/youtube/', views.YoutubeView.as_view(), name='youtube'),
    path('pc/pc-index/', views.PcIndexView.as_view(), name='pc_index'),
    path('pc/pc-1/', views.Pc1View.as_view(), name='pc_1'),
    path('pc/pc-2/', views.Pc2View.as_view(), name='pc_2'),
    path('pc/pc-3/', views.Pc3View.as_view(), name='pc_3'),
    path('python/python-index/', views.PythonIndexView.as_view(), name='python_index'),
    path('python/python-1/', views.Python1View.as_view(), name='python_1'),
    path('python/python-2/', views.Python2View.as_view(), name='python_2'),
    path('python/python-3/', views.Python3View.as_view(), name='python_3'),
    path('python/python-4/', views.Python4View.as_view(), name='python_4'),
    path('python/python-5/', views.Python5View.as_view(), name='python_5'),
    path('python/python-6/', views.Python6View.as_view(), name='python_6'),
    path('python/python-math/', views.PythonMathView.as_view(), name='python_math'),
    path('python/python-random/', views.PythonRandomView.as_view(), name='python_random'),
    path('html-css/html-css-index/', views.HtmlCssIndexView.as_view(), name='html_css_index'),
    path('html-css/html-css-1/', views.HtmlCss1View.as_view(), name='html_css_1'),
    path('search/', search.get_search, name='search'),
    path('thinup/contact-form/', views.ContactFormView.as_view(), name='contact_form'),
    # path('thinup/complete-form/', forms.send_email, name='form'),
]
