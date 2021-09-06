from django.db.models.query import QuerySet
from django.views import generic
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    model = Post
    # template_name = "blog/post_list.html"

    def get_queryset(self):
        querySet = Post.objects.order_by("-created_at")
        keyword = self.request.GET.get("keyword")

        if keyword:
            queryset = queryset.filter(title=keyword)
        return queryset
    