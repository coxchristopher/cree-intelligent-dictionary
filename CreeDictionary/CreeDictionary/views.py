from django.http import HttpResponse
from django.shortcuts import render

from CreeDictionary.forms import WordSearchForm


def index(request, query_string=None):
    """
    homepage with optional initial query

    :param request:
    :param query_string: initial word and search results to display
    :return:
    """
    context = {"word_search_form": WordSearchForm()}
    if query_string is not None:
        context.update({"query_string": query_string})
    return HttpResponse(render(request, "CreeDictionary/index.html", context))


def display_word(request, query_string=None):
    """
    display paradigms for a word

    :param request:
    :param query_string: word to display paradigm for
    :return:
    """
    context = {}
    if query_string is not None:
        context.update({"query_string": query_string})

    return HttpResponse(render(request, "CreeDictionary/display-word.html", context))
