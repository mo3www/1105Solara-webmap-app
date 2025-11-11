import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="mercator",  # 使用平面投影
        height="750px",
        zoom=12,  # 設定適合台北市區的縮放級別
        sidebar_visible=True,
        pitch=0,  # 取消傾斜角度
        bearing=0,  # 取消旋轉角度
        center=[25.0330, 121.5654],  # 置中於台北市
    )

    # 設定捷運路線和站點的 GeoJSON 來源
    points_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/stations.geojson"
    lines_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    
    # 添加捷運站點 (Points)
    m.add_geojson(points_url, name="Points", fit_bounds=False)
    
    # 這裡可以為每條線路設置不同顏色
    m.add_geojson(
        lines_url,
        name="Lines",
        style=lambda feature: {
            'color': get_line_color(feature),  # 使用不同顏色來區分每條線路
            'weight': 3,  # 線條粗細
            'opacity': 0.7  # 透明度
        }
    )
    
    return m


def get_line_color(feature):
    """
    根據線路的名稱或者其他屬性返回不同的顏色
    假設 GeoJSON 中有一個屬性叫做 "line_name" 用來標識不同的線路
    """

    line_name = feature['properties'].get('line_name', '').lower()  # 根據線路名稱返回顏色
    
    # 可以根據不同的線路名稱設置不同的顏色
    line_colors = {
        'blue': '#0099FF',  # 藍線
        'red': '#FF3333',   # 紅線
        'green': '#33CC33',  # 綠線
        'brown': '#8B4513',  # 茶色
        'orange': '#FFA500',  # 橙線
        'yellow': '#FFFF00',  # 黃線
    }
    
    # 若線路名稱在字典中，返回對應顏色
    for line, color in line_colors.items():
        if line in line_name:
            return color
    
    return '#CCCCCC'  # 若找不到對應線路名稱，默認為灰色


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
