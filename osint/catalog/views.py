from django.http import Http404, HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import generic
from .forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_entities = Entity.objects.all().count()
    num_administrators = Administrator.objects.all().count()
    num_entities_active = Entity.objects.filter(status__exact='a').count()
    num_secondary_business = Business.objects.count() + 1  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_entities': num_entities, 'num_administrators': num_administrators,
                 'num_entities_active': num_entities_active, 'num_secondary_business': num_secondary_business},
    )


class EntityListView(generic.ListView):
    model = Entity
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EntityListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class EntityDetailView(generic.DetailView):
    model = Entity

    def entity_detail_view(request, pk):
        try:
            entity_id = Entity.objects.get(pk=pk)
        except Entity.DoesNotExist:
            raise Http404("Entity does not exist")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/entity_detail.html',
            context={'entity': entity_id, }
        )


class AdministratorListView(generic.ListView):
    model = Administrator
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AdministratorListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class AdministratorDetailView(generic.DetailView):
    model = Administrator

    def administrator_detail_view(request, pk):
        try:
            administrator_id = Administrator.objects.get(pk=pk)
        except Administrator.DoesNotExist:
            raise Http404("Esta persona vinculada no existe")

        return render(
            request,
            'catalog/administrator_detail.html',
            context={'administrator': administrator_id, }
        )


class BusinessDetailView(generic.DetailView):
    model = Business

    def business_detail_view(request, pk):
        try:
            business_id = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            raise Http404("Esta entidad relacionada no existe")

        return render(
            request,
            'catalog/business_detail.html',
            context={'business': business_id, }
        )


class IndividualListView(generic.ListView):
    model = Individual
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndividualListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class IndividualDetailView(generic.DetailView):
    model = Individual

    def individual_detail_view(request, pk):
        try:
            individual_id = Individual.objects.get(pk=pk)
        except Individual.DoesNotExist:
            raise Http404("Este individuo no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/individual_detail.html',
            context={'individual': individual_id, }
        )


# class SocialMediaAccountListView(generic.ListView):
#     model = SocialMediaAccount
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(SocialMediaAccountListView, self).get_context_data(**kwargs)
#         # Get the blog from id and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context


class SocialMediaAccountDetailView(generic.DetailView):
    model = SocialMediaAccount

    def SocialMediaAccount_detail_view(request, pk):
        try:
            socialmediaaccount_id = SocialMediaAccount.objects.get(pk=pk)
        except SocialMediaAccount.DoesNotExist:
            raise Http404("La cuenta no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/socialmediaaccount_detail.html',
            context={'socialmediaaccount': socialmediaaccount_id, }
        )

class VehicleDetailView(generic.DetailView):
    model = Vehicle

    def Vehicle_detail_view(request, pk):
        try:
            vehicle_id = Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404("El vehíulo no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/vehicle_detail.html',
            context={'vehicle': vehicle_id, }
        )

class EmailDetailView(generic.DetailView):
    model = Email

    def Email_detail_view(request, pk):
        try:
            email_id = Email.objects.get(pk=pk)
        except Email.DoesNotExist:
            raise Http404("El email no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/email_detail.html',
            context={'email': email_id, }
        )

class AddressDetailView(generic.DetailView):
    model = Address

    def Address_detail_view(request, pk):
        try:
            address_id = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404("La dirección no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/address_detail.html',
            context={'address': address_id, }
        )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'catalog/signup.html', {'form': form})


from django.contrib.auth.mixins import LoginRequiredMixin


class RegisteredEntitiesByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Entity
    template_name = 'catalog/entity_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Entity.objects.filter(borrower=self.request.user).order_by('nif')


class RegisteredIndividualsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Individual
    template_name = 'catalog/individual_list_registered_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Individual.objects.filter(borrower=self.request.user).order_by('surname1')


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class EntityCreate(CreateView):
    model = Entity
    fields = '__all__'
    # exclude = ['borrower']


class EntityUpdate(UpdateView):
    model = Entity
    fields = '__all__'
    # exclude = ['borrower']

class EntityDelete(DeleteView):
    model = Entity
    success_url = reverse_lazy('my-borrowed')


class AdministratorCreate(CreateView):
    model = Administrator
    fields = '__all__'
    # exclude = ['borrower']

class AdministratorUpdate(UpdateView):
    model = Administrator
    fields = '__all__'
    # exclude = ['borrower']
    # def get_success_url(self):
    #     return self.request.path

class AdministratorDelete(DeleteView):
    model = Administrator
    success_url = reverse_lazy('my-borrowed')


class BusinessCreate(CreateView):
    model = Business
    fields = '__all__'
    # exclude = ['borrower']


class BusinessUpdate(UpdateView):
    model = Business
    fields = '__all__'
    # exclude = ['borrower']


class BusinessDelete(DeleteView):
    model = Business
    success_url = reverse_lazy('administrators')


class IndividualCreate(CreateView):
    model = Individual
    fields = '__all__'
    # exclude = ['borrower']


class IndividualUpdate(UpdateView):
    model = Individual
    fields = '__all__'
    # exclude = ['borrower']


class IndividualDelete(DeleteView):
    model = Individual
    success_url = reverse_lazy('my-registered')


class SocialMediaAccountCreate(CreateView):
    model = SocialMediaAccount
    fields = '__all__'
    # exclude = ['borrower']


class SocialMediaAccountUpdate(UpdateView):
    model = SocialMediaAccount
    fields = '__all__'
    # exclude = ['borrower']


class SocialMediaAccountDelete(DeleteView):
    model = SocialMediaAccount
    success_url = reverse_lazy('my-registered')


class EmailCreate(CreateView):
    model = Email
    fields = '__all__'
    # success_url = reverse_lazy('my-registered')
    # exclude = ['borrower']
    # success_url deberia ser a la pagina anterior -> investigar


class EmailUpdate(UpdateView):
    model = Email
    fields = '__all__'
    # exclude = ['borrower']


class EmailDelete(DeleteView):
    model = Email
    # success_url = reverse_lazy('my-registered')


class AddressCreate(CreateView):
    model = Address
    fields = '__all__'
    # exclude = ['borrower']
    # success_url = reverse_lazy('my-registered')


class AddressUpdate(UpdateView):
    model = Address
    fields = '__all__'
    # exclude = ['borrower']


class AddressDelete(DeleteView):
    model = Address
    #success_url = reverse_lazy('my-registered')


class VehicleCreate(CreateView):
    model = Vehicle
    fields = '__all__'
    # exclude = ['borrower']
    #success_url = reverse_lazy('vehicle-detail')


class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'
    # exclude = ['borrower']
    #success_url = reverse_lazy('vehicle-detail')


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle-detail')



def model_form_upload(request):
    if request.method == 'POST':
        form = EntityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntityForm()
    return render(request, 'templates/catalog/entity_form.html', {
        'form': form
    })

def model_form_upload_individual(request):
    if request.method == 'POST':
        form = IndividualForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IndividualForm()
    return render(request, 'templates/catalog/individual_form.html', {
        'form': form
    })



