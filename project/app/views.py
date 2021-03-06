from django.shortcuts import render, HttpResponse
import os
import re
from django import http
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
file='FinalData.csv'
file2='ratings.csv'

# Create your views here.
def index(request):
    return render(request,'index.html')
def interestbased (request):
    # return HttpResponse("You search")
    try:
        user_search=request.GET.get("u_search")
        df=pd.read_csv(file)
        result=df.loc[df["title"]==user_search, :]
        a=result.iloc[0][3]
        rec=df.loc[df["Genres"]==a,["book_id","title","authors"]]
        reindex=rec.reset_index(drop=True)
        json_records = reindex.reset_index().to_json(orient ='records') 
        data = [] 
        data = json.loads(json_records) 
        context = {'d': data ,
                   'b': a}
        return render( request,'interestbased.html',context)
    except:
        user_search=request.GET.get("u_search")
        df=pd.read_csv(file)
        result=df.loc[df["title"].str.contains(user_search) ,["book_id","title","authors"]]
        reindex=result.reset_index(drop=True)
        json_records = reindex.reset_index().to_json(orient ='records') 
        data = [] 
        data = json.loads(json_records) 
        context = {'d': data,
                    'b':user_search} 
        return render(request,'interestbased.html',context)
def books(request):
    return render(request,'books.html')
def biography(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Biography",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data} 
    return render(request,'biography.html',context)
def drama(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Drama",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}
    return render(request,'drama.html',context)
def fantasy(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Fantasy",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}
    return render(request,'fantasy.html',context)
def fiction(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Fiction",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}
    return render(request,'fiction.html',context)
def romance(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Romance",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}
    return render(request,'romance.html',context)
def scifi(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="SciFi",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}
    return render(request,'scifi.html',context)
def thriller(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Thriller",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data}
    return render(request,'thriller.html',context) 
def cossim (request):
    user_search=request.GET.get("search")
    df_title=pd.read_csv(file)
    df_title['corpus'] = (pd.Series(df_title[['authors', 'Genres']].fillna('').values.tolist()).str.join(' '))
    tf_corpus = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix_corpus = tf_corpus.fit_transform(df_title['corpus'])
    cosine_sim_corpus = cosine_similarity(tfidf_matrix_corpus, tfidf_matrix_corpus)
    titles = df_title['title']
    indices = pd.Series(df_title.index, index=df_title['title'])
    idx = indices[user_search]
    sim_scores = list(enumerate(cosine_sim_corpus[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    haah = pd.DataFrame(sim_scores, columns = ['index','cosim_score'])
    haah = haah[haah['cosim_score']>=0.25]
    a=titles.iloc[haah['index']]
    a.to_frame()
    b=pd.merge(a,haah,left_index=True,right_on='index')
    b=b.set_index("title")
    b=b.drop(user_search,axis=0)
    del b['index']
    rec = b
    json_records = rec.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'c': user_search,'d': data}
    return render(request,'cossim.html',context)
def pearson(request):
    user_search=request.GET.get("search")
    df = pd.read_csv(file2, encoding = "ISO-8859-1")
    df_title =  pd.read_csv(file, encoding = "ISO-8859-1")
    df_title.set_index('book_id', inplace = True)
    f = ['count']
    df_book = pd.DataFrame(df.groupby('book_id')['rating'].agg(f))
    df_p = pd.pivot_table(df,values='rating',index='user_id',columns='book_id')
    i = int(df_title.index[df_title['title'] == user_search][0])
    target = df_p[i]
    similar_to_target = df_p.corrwith(target)
    corr_target = pd.DataFrame(similar_to_target, columns = ['PearsonR'])
    corr_target = corr_target.sort_values('PearsonR', ascending = False)
    corr_target.index = corr_target.index.map(int)
    corr_target = corr_target.join(df_title).join(df_book)[['title', 'PearsonR','count']]
    corr_target[corr_target['count']>=100]
    corr_target=corr_target.set_index("title")
    corr_target=corr_target.drop("The Fellowship of the Ring",axis=0)
    rec=corr_target[corr_target['PearsonR']>=0.32]
    del rec['count']
    json_records = rec.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'c': user_search,'d': data}
    return render(request,'pearson.html',context)
def submit(request):
    user_search=request.GET.get("s_search").lower()
    df=pd.read_csv(file)
    result=df.loc[df["title"].str.lower().str.contains(user_search) ,["book_id","title","authors"]]
    reindex=result.reset_index(drop=True)
    json_records = reindex.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data,
                'b':user_search} 
    return render(request,'submit.html',context)