from django.shortcuts import redirect, render
from django.views.generic import View
# from .models import Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html',)


class TwitterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sns/twitter.html',)


class InstagramView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sns/instagram.html',)


class YoutubeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sns/youtube.html',)


class PcIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pc/pc_index.html',)


class Pc1View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pc/pc#1.html',)


class Pc2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pc/pc#2.html',)


class Pc3View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pc/pc#3.html',)


class PcMemoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pc/pc_memo.html',)


class PythonIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python_index.html',)


class Python1View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python#1.html',)


class Python2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python#2.html',)


class Python3View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python#3.html',)


class Python4View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python#4.html',)


class Python5View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python#5.html',)


class Python6View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python#6.html',)


class PythonMathView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python_math.html',)


class PythonRandomView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'python/python_random.html',)


class HtmlCssIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'html_css/html_css_index.html',)


class HtmlCss1View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'html_css/html_css#1.html',)


class HtmlCss2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'html_css/html_css#2.html',)
