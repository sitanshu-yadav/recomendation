import os
from django import http
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
# from surprise import Reader, Dataset, SVD
file='C://Users/Situ/Desktop/django/recomendation/FinalData.csv'
file2='C://Users/Situ/Desktop/recomendation/ratings.csv'

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
def cossim(request):
    user_search=request.GET.get("search")
    df=pd.read_csv(file)
    col_list= ["book_id", "title"]
    df_onlytitle =  pd.read_csv('FinalData.csv', encoding = "ISO-8859-1", usecols=col_list)
    df['corpus'] = (pd.Series(df[['authors', 'Genres']].fillna('').values.tolist()).str.join(' '))
    tf_corpus = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix_corpus = tf_corpus.fit_transform(df['corpus'])
    cosine_sim_corpus = linear_kernel(tfidf_matrix_corpus, tfidf_matrix_corpus)
    titles = df['title']
    indices = pd.Series(df.index, index=df['title'])
    def corpus_recommendations(title):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim_corpus[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]
        book_indices = [i[0] for i in sim_scores]
        return titles.iloc[book_indices]
    rec=corpus_recommendations("search")
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
def svd(request):
    df=pd.read_csv(file)
    rec=df.loc[df["Genres"]=="Thriller",["book_id","title","authors"]]
    reindex=rec.reset_index(drop=True)
    return HttpResponse( reindex.to_html())
