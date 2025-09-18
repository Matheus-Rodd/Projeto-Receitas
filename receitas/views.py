from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Receita, Mensagem
from .forms import ContatoForm


def home(request):
    return render(request, "receitas/home.html")


def sobre(request):
    return render(request, "receitas/sobre.html")


def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            mensagem_texto = form.cleaned_data["mensagem"]

            # Salvar a mensagem no banco
            Mensagem.objects.create(nome=nome, email=email, mensagem=mensagem_texto)

            # Enviar e-mail (apenas no console)
            send_mail(
                subject=f"Mensagem de {nome}",
                message=f"De: {nome} <{email}>\n\n{mensagem_texto}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "✅ Sua mensagem foi enviada com sucesso!")
            form = ContatoForm()  # limpa o formulário
        else:
            messages.error(request, "⚠️ Preencha todos os campos corretamente.")
    else:
        form = ContatoForm()

    return render(request, "receitas/contato.html", {"form": form})


def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, "receitas/receita_detail.html", {"receita": receita})


def pesquisar_receitas(request):
    query = request.GET.get("q", "")
    resultados = []
    if query:
        resultados = Receita.objects.filter(title__icontains=query)
    return render(
        request, "receitas/pesquisa.html", {"query": query, "resultados": resultados}
    )


def categoria_receitas(request, categoria):
    receitas = Receita.objects.filter(categoria__iexact=categoria)
    return render(
        request,
        "receitas/categoria.html",
        {"categoria": categoria, "receitas": receitas},
    )
