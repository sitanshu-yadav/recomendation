import os
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
file='C://Users/Situ/Desktop/django/recomendation/FinalData.csv'

def index (request):
    return render(request,'index.html')
def books (request):
    # return HttpResponse("You search")
    user_search=request.GET.get("u_search")
    df=pd.read_csv(file)
    result=df.loc[df["title"]==user_search, :]
    a=result.iloc[0][3]
    rec=df.loc[df["Genres"]==a,["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())