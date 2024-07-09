import pandas as pd
import wordcloud as wc
import matplotlib.pyplot as plt

ausRaw = pd.read_csv("abcnews-date-text.csv")
ausDf = ausRaw[(ausRaw["headline_text"].str.contains("migra"))]

indRaw = pd.read_csv("india-news-headlines.csv")
indDf = indRaw[(indRaw["headline_text"].str.contains("migra"))]

usaRaw = pd.read_csv("dsjVoxArticles.tsv", sep="\t")
usaDf = usaRaw[(usaRaw["title"].str.contains("migra"))]

stopwords = set(wc.STOPWORDS)
stopwords.update([
    "immigration", "immigrant", "immigrants", "immigrate",
    "migration", "migrant", "migrants", "migrate",
    "migratory", "bird", "birds", "migraine",
    "u", "s", "â", "vox", "abc"
])
width = 1920
height = 1080
font = "/Library/Fonts/NewYorkLarge-Medium.otf"

plt.imshow(
    wc.WordCloud(
        width=width, height=height, font_path=font, stopwords=stopwords
    ).generate(" ".join(list(usaDf["title"].fillna("").apply(str.lower)))),
    interpolation="bilinear",
)
plt.title("United States")
plt.axis("off")
plt.savefig("usa.png", dpi=500)

plt.imshow(
    wc.WordCloud(
        width=width, height=height, font_path=font, stopwords=stopwords
    ).generate(" ".join(list(ausDf["headline_text"]))),
    interpolation="bilinear",
)
plt.title("Australia")
plt.axis("off")
plt.savefig("aus.png", dpi=500)

plt.imshow(
    wc.WordCloud(
        width=width, height=height, font_path=font, stopwords=stopwords
    ).generate(" ".join(list(indDf["headline_text"].apply(str.lower)))),
    interpolation="bilinear",
)
plt.title("India")
plt.axis("off")
plt.savefig("ind.png", dpi=500)
