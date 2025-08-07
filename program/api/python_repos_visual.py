import requests
import plotly.express as px
#--------グラフを描画（レンダリング）する方法をブラウザ表示に設定----------
import plotly.io as pio
pio.renderers.default = 'browser'
#---------------------------------------------------------------------

# API呼び出しを作成してレスポンスを確認する
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# レスポンスのオブジェクトを辞書に変換する
response_dict = r.json()
print(f"全リポジトリ数: {response_dict['total_count']}")
print(f"完全な結果: {not response_dict['incomplete_results']}")

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    #リポジトリ名を有効なリンクにする
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    #ホバーテキストを構築する
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#可視化を作成する
title = "GitHubで最も多くのスターがついている Python プロジェクト"
labels = {"x": "リポジトリ", "y": "スターの数"}
fig = px.bar(x = repo_links, y = stars, title = title, labels = labels,
             hover_name = hover_texts)

fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20,
                  yaxis_title_font_size = 20)

fig.update_traces(marker_color = "SteelBlue", marker_opacity = 0.6)

fig.show()