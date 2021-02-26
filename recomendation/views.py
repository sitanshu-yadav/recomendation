import os
from django import http
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
file='C://Users/Situ/Desktop/django/recomendation/FinalData.csv'

def index (request):
    return render(request,'index.html')
def books (request):
    # return HttpResponse("You search")
    try:
        user_search=request.GET.get("u_search")
        df=pd.read_csv(file)
        result=df.loc[df["title"]==user_search, :]
        a=result.iloc[0][3]
        rec=df.loc[df["Genres"]==a,["book_id","title","authors"]]
        reindex=rec.reset_index(drop=True)
        return HttpResponse( reindex.to_html())
    except:
        user_search=request.GET.get("u_search")
        df=pd.read_csv(file)
        result=df.loc[df["title"].str.contains(user_search) , :]
        reindex=result.reset_index(drop=True)
        return HttpResponse(reindex.to_html())

def Biography(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Biography",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def Drama(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Drama",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def Fantasy(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Fantasy",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def Fiction(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Fiction",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def Romance(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Romance",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def Scifi(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="SciFi",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def Thriller(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Thriller",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())