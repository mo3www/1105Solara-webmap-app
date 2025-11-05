import solara
from pages import _00_home, _01_globle  # 假設你將這些頁面放在 pages 目錄中

# 設定路由
def app():
    return solara.Router(
        routes={
            "/": _00_home.HomePage,  # 設定首頁
            "/globle": _01_globle.GlobalPage,  # 設定其他頁面
        }
    )

if __name__ == "__main__":
    solara.run(app)