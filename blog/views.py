from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse \
    # ,Http404
from django.views.generic import ListView, DetailView

from blog.models import Article, Category


def home(request):
    context = {

        "user": [{"username": "fahimeh",
                  "age": 36,
                  "job": "programmer"}],
        "articles": [
            {
                "article": "تشخیص آفساید نیمه‌خودکار ",
                "description": "این فناوری بسیار شبیه به فناوری خط دروازه است، اما به جای ردیابی خط ثابت دروازه، به‌صورت پیوسته بازیکنان را دنبال می‌کند. این سیستم با کمک هوش مصنوعی به داوران بازی اجازه می‌دهد تا در سریع‌ترین زمان ممکن آفسایدها را تشخیص دهند.",
                "image": "https://digiato.com/wp-content/uploads/2022/11/fifafafafa-sXk4.jpg"
            },
            {
                "article": "توپ متصل به شبکه ",
                "description": "توپ رسمی جام جهانی امسال با نام «الرحله» در داخل خود یک حسگر کروی‌شکل دارد که 500 بار در هر ثانیه اطلاعات خود را به اتاق عملیات ویدیویی می‌فرستد و اجازه شناسایی نقطه دقیق شوت‌شدن را می‌دهد.",
                "image": "https://digiato.com/wp-content/uploads/2022/11/Cum-va-arata-mingea-cu-care-se-vor-juca-meciurile-de-la-Campionatul-Mondial-din-Qatar-inclusiv-cu-acel-senzor-in-ea.-Sursa-news.adidas.com_.jpg"
            },
            {
                "article": "فناوری‌های خنک‌کننده ",
                "description": "فیفا برای برگزاری جام جهانی در قطر مجبور شد این رقابت‌ها را حدود شش ماه به تعویق بیندازد و بازی‌ها را به جای تابستان در اواخر پاییز برگزار کند تا مشکلات ناشی از گرمای شدید در این کشور گریبان‌گیر بازیکنان و تماشاچیان نشود. با این حال، دمای هوا در قطر همچنان به‌طور میانگین بین 21 تا 26 درجه سلسیوس است.",
                "image": "https://digiato.com/wp-content/uploads/2022/11/original.jpeg"

            }]

    }
    return render(request, "blog/home0.html", context)


# def home_from_database(request):
#     article_list = Article.objects.published()
#     paginator = Paginator(article_list,1)
#     page = request.GET.get('page')
#     articles = paginator.get_page(page)
#     context = {
#         # "articles": Article.objects.all()
#         # "articles": Article.objects.filter(status="p").order_by("-publish")[:3]  # display 3 last article
#         # "articles": Article.objects.filter(status="p"),  # or #Article.objects.published() => with ArticleManager
#         "articles": articles,
#
#         # "category": Category.objects.filter(status=True)
#     }
#
#     return render(request, "blog/home_from_database.html", context)

class ArticleList(ListView):
    # model = Article
    template_name = 'blog/home_from_database.html'
    context_object_name = "articles"
    queryset = Article.objects.published()
    # paginate_by = 5


# def detail_article(request, slug):
#     # try:
#     #     article = Article.objects.get(slug = slug)
#     # except Exception as e:
#     #     raise Http404
#     # context = {
#     #     "article": article
#     #
#     # }
#
#     context = {
#         "article": get_object_or_404(Article, slug=slug, status="p"),
#         # or #get_object_or_404(Article.objects.published(), slug=slug)
#         # "category": Category.objects.filter(status=True)
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


# def category(request, slug):
#     context = {
#         "category": get_object_or_404(Category, slug=slug, status=True),
#     }
#     return render(request, "blog/category.html", context)

class CategoryList(ListView):
    # paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


def api(request):
    data = {
        "1": {"title": "مقاله اول",
              "id": 20,
              "edition": "first_edition"},
        "2": {"title": "مقاله دوم",
              "id": 21,
              "edition": "second_edition"},
        "3": {"title": "مقاله سوم",
              "id": 22,
              "edition": "third_edition"}
    }
    return JsonResponse(data)
