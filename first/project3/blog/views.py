from django.db.models.query import QuerySet
from django.views import generic
from django.db.models import Q
from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    # template_name = "blog/post_list.html"

    def get_queryset(self):
        queryset = Post.objects.order_by("-created_at")
        keyword = self.request.GET.get("keyword")

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset
    