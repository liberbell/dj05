from django.views import generic
from django.db.models import Q, fields
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentCreateForms

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
    
class CategoryView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])

        queryset = Post.objects.order_by("-created_at").filter(category=category)
        return queryset
    
class DetailView(generic.DetailView):
    model = Post

class CommentView(generic.CreateView):
    # model = Comment
    # form_class = CommentCreateForms

    # def form_valid(self, form):
    #     post_pk = self.kwargs["post_pk"]
    #     comment = form.save(commit=False)
    #     comment.post = get_object_or_404(Post, pk=post_pk)
    #     comment.save()
    #     return redirect("blog:detail", pk=post_pk)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            fields.widget.attrs["class"] = "form-control"