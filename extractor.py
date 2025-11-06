{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from fastapi import FastAPI, Request\
from newspaper import Article\
import uvicorn\
\
app = FastAPI()\
\
@app.post("/extract")\
async def extract(request: Request):\
    data = await request.json()\
    url = data.get("url")\
\
    try:\
        article = Article(url)\
        article.download()\
        article.parse()\
        return \{\
            "title": article.title,\
            "text": article.text,\
            "authors": article.authors,\
            "date": str(article.publish_date),\
            "image": article.top_image,\
            "summary": article.summary,\
        \}\
    except Exception as e:\
        return \{"error": str(e)\}\
\
if __name__ == "__main__":\
    uvicorn.run(app, host="0.0.0.0", port=8000)\
}