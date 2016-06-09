from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from tracks.models import Track, Genre
from .forms import AddTrackForm, AddGenreForm
from django.db.models import Q


class TrackListView(ListView, FormView):
    """
    List of all tracks
    """

    model = Track
    template_name = "tracklist.html"
    form_class = AddTrackForm
    success_url = "/tracks/"
    paginate_by = 8

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            title1 = form.cleaned_data['title']
            genre1 = form.cleaned_data['genre']
            rating1 = form.cleaned_data['rating']
            trackobj = Track.objects.create(title=title1, genre=genre1, rating=rating1)
            trackobj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(TrackListView, self).get_context_data(**kwargs)
        trackobj = Track.objects.all()
        paginator = Paginator(trackobj, self.paginate_by)
        page_no = self.request.GET.get('page', 1)

        try:
            trackob = paginator.page(page_no)
        except PageNotAnInteger:
            trackob = paginator.page(1)
        except EmptyPage:
            trackob = paginator.page(paginator.num_pages)

        context['trackobj'] = trackob
        context['page'] = paginator.page(page_no)
        context['paginator'] = paginator
        return context


def EditTrack(request):
    """
    Update the track fields
    """
    if request.method == 'POST':

        editdata = dict(request.POST.items())

        try:
            instance = Track.objects.get(id=editdata['trackid'])
        except DoesNotExist:
            raise Http404()
        else:
            instance.title = editdata['title']
            instance.rating = editdata['rating']
            instance.genre = editdata['genre']
            instance.save()
        return HttpResponseRedirect(reverse("track-view"))


class TrackDetailView(DetailView):
    """
    Details of a particular Track
    """
    model = Track
    template_name = "trackdetail.html"
    pk_url_kwargs = 'pk'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)

        if pk is not None:
            queryset = queryset.filter(pk=pk)
        try:
            obj = queryset.get()

        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})

        return obj

    def get_context_data(self, **kwargs):
        context = super(TrackDetailView, self).get_context_data(**kwargs)
        if self.object:
            context['object'] = self.object
        return context


class GenreListView(ListView, FormView):

    """
    List of all Genres
    """

    model = Genre
    template_name = "genrelist.html"
    form_class = AddGenreForm
    success_url = '/genres/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            genre1 = form.cleaned_data['genre_name']
            genreobj = Genre.objects.create(genre_name=genre1)
            genreobj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        return context


class GenreDetailView(DetailView):

    """
    Details of a particular Genre
    """

    model = Genre
    template_name = "genredetail.html"
    pk_url_kwargs = 'pk'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)

        if pk is not None:
            queryset = queryset.filter(pk=pk)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})

        return obj

    def get_context_data(self, **kwargs):
        context = super(GenreDetailView, self).get_context_data(**kwargs)
        if self.object:
            context['object'] = self.object
        return context


def SearchView(request):
    """
    Search track by title or Genre
    """
    if request.method == "GET":

        q1 = request.GET.get('search_box', '')
        qs = Track.objects.get(Q(title__icontains=q1) | Q(genre__genre_name__icontains=q1))
        if qs:
            return render(request, 'tracklist.html', {'searchdata': qs})
