import solara
import leafmap.maplibregl as leafmap  # ✅ 改成 maplibregl

# 台北捷運線路與出口資料
mrt_line_url = "https://raw.githubusercontent. com/leoluyi/taipei_mrt/master/mrt-line.json"
exits_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/exits.geojson"

def create_map():
    m = leafmap.Map(
        center=[25.0330, 121.5654],
        zoom=12,
        style="dark-matter",       # ✅ MapLibre 的暗色底圖樣式
        height="750px",
        projection="globe",        # ✅ 可選：地球投影
    )

    # 加入兩個圖層
    m.add_geojson(mrt_line_url, layer_name="台北捷運")
    m.add_geojson(exits_url, layer_name="捷運出口")

    return m

@solara.component
def Page():
    m = create_map()
    return m.to_solara()  # ✅ 現在 maplibregl.Map 物件才有此方法
