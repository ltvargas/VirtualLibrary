from django.db.models import manager
from django.db.models.fields import DateTimeField
from django.shortcuts import render
from biblioteca.models import Book,Borrow
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json


def to_json(object):
    return ({
        "code" : object.code,
        "title" : object.title,
        "author" : object.author,
        "amount" : object.amount     
    })


def to_json_borrow(object):
    date_devolution=object.date_devolution
    if not date_devolution:
        date_devolution="unreturned book"
    else:
        date_devolution="{}-{}-{}".format(date_devolution.year, date_devolution.month,date_devolution.day)

    return ({
        "date_issue": "{}-{}-{}".format(object.date_issue.year, object.date_issue.month, object.date_issue.day),
        "date_devolution" :date_devolution,
        "book" : to_json(object.book),
        "user_email" : object.user_email, 
    })


def check_book(book):
    if not book:
        raise Exception()
    if not(book["code"] and book["title"] and book["author"] and book["amount"]):
        raise Exception()
    

def inc_amount(book,response):
    int_amout = int(book.amount)
    int_amout+=response["amount"]
    book.amount = str(int_amout)
    book.save(update_fields = ["amount"])

    
@require_http_methods(["GET"])
def load_books(request):
    response = []
    books = Book.objects.all().filter(amount__gte=1)
    for book in books:
        response.append(to_json(book))
    return HttpResponse(json.dumps(response))


@require_http_methods(["GET"])
def load_borrow(request,user):
    response = []
    borrows = Borrow.objects.filter(user_email=user,date_devolution=None)
    for borrow in borrows:
        response.append(to_json_borrow(borrow))
    return HttpResponse(json.dumps(response))


@require_http_methods(["GET"])
def search_books(request,code):
    book = Book.objects.filter(code=code)
    if book.exists():
        return HttpResponse(
            json.dumps(
                to_json(book.get()
            )
        )
    )
    else:
        return HttpResponse(json.dumps(
        {
            "error":"Book not found in database."
        }
    )
)


@require_http_methods(["GET"])
def borrow_history(request,user):
    response = []
    borrows = Borrow.objects.filter(user_email=user)
    for borrow in borrows:
        response.append(to_json_borrow(borrow))
    return HttpResponse(json.dumps(response))



@csrf_exempt
@require_http_methods(["POST"])
def create_book(request):
    try:
        data = json.loads(request.body) 
        check_book(data)
        book = Book.objects.filter(code=data["code"])
        if not book.exists() :
            book = Book(**data)
            book.save()
            return HttpResponse(json.dumps(to_json(book)))
        else: 
            inc_amount(book.get(),data)
            return HttpResponse(json.dumps(
            {
                "notice":"Book already exist. Now you have {} books".format(str(book.get().amount))
            }
            )
        )
    except Exception as e:
        return HttpResponse(json.dumps(
        {
            "error":"All data should be provided"
        }
        )
    )
    

@csrf_exempt
@require_http_methods(["POST"])
def return_book(request):
    data = json.loads(request.body) 
    borrow = Borrow.objects.filter(book__code=data["code"],date_devolution=None)
    if borrow.exists():
        borrow_objet=borrow.get()
        borrow_objet.date_devolution=date.today()
        borrow_objet.save(update_fields = ["date_devolution"])
        return HttpResponse(json.dumps(to_json_borrow(borrow_objet)))
    else:
        return HttpResponse(json.dumps(
            {
                "error":"you do not have the borrow pending"
            }
            )
        )


@csrf_exempt
@require_http_methods(["POST"])
def unreserver_book(request):
    data = json.loads(request.body) 
    book = Book.objects.filter(code=data["code"])
    if book.exists() :
        book_objet=book.get()
        book_objet.amount+=1
        book_objet.save(update_fields = ["amount"])
        return HttpResponse(json.dumps(to_json(book_objet)))


@csrf_exempt
@require_http_methods(["POST"])
def reserver_book(request):
    data = json.loads(request.body) 
    book = Book.objects.filter(code=data["code"])
    if book.exists() :
        book_objet=book.get()
        book_objet.amount-=1
        book_objet.save(update_fields = ["amount"])
        return HttpResponse(json.dumps(to_json(book_objet)))


@csrf_exempt
@require_http_methods(["POST"])
def borrow_book(request):
    data = json.loads(request.body) 
    borrow = Borrow.objects.filter(book__code=data["book"]["code"],date_devolution=None)
    if not borrow.exists():
        book = Book.objects.filter(code=data["book"]["code"])
        borrw_objet = Borrow.objects.create(user_email=data["user_email"],book=book.get())
        return HttpResponse(json.dumps(to_json_borrow(borrw_objet)))
    else: 
        return HttpResponse(json.dumps(
        {
            "error":"you have already borrow a volume equal to this book"
        }
        )
    )
    