from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging

logger = logging.getLogger(__name__)


# def log(func):
#     def wrapper(*args, **kwargs):
#         logger.info(f'The view function {func.__name__} was called and has returned {(result := func(*args, **kwargs))}')
#
#         return result
#
#     return wrapper


def coin(request):
    logger.info(f'The view function {coin.__name__} was called and has returned {(result := choice(["tail", "head"]))}')
    return HttpResponse(result)


def dice(request):
    logger.info(f'The view function {dice.__name__} was called and has returned {(result := randint(1, 6))}')
    return HttpResponse(result)
