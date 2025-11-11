import solara
import leafmap.maplibregl as leafmap
import requests

# 路線顏色對應表
def route_color(route_name):
    """ 根據路線名稱返回顏色 """
    if '信義線' in route_name or '淡水線' in route_name:
        return "#f9000f"  # 紅色
    elif '木柵線' in route_name or '內湖線' in route_name:
        return "#ce8d13"  # 橙色
    elif '蘆洲線' in route_name or '新莊線' in route_name or '中和線' in route_name:
        return '#ffb600'  # 黃色
    elif '板橋線' in route_name or '南港線' in route_name:
        return '#006bc2'  # 藍色
    elif '小南門線' in route_name or '松山線' in route_name or '新店線' in route_name:
        return '#008c5a'  # 綠色
    elif '碧潭支線' in route_name:
        return '#d0e300'  # 明綠色
    else:
        return '#cccccc'  # 預設灰色

def create_map():
    m = leafmap.Map(
        style="dark-matter",
        projection="mercator",  # 平面投影
        height="750px",
        zoom=12,
        sidebar_visible=True,
        center=[25.0330, 121.5654],  # 台北市中心
    )

    # 讀取捷運路線
    lines_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    lines_data = requests.get(lines_url).json()
    # 在每個 feature 裡加入 color 屬性
    for feature in lines_data["features"]:
        route_name = feature["properties"].get("RouteName", "")
        feature["properties"]["color"] = route_color(route_name)

    # 加入路線圖層
    m.add_geojson(
        lines_data,
        name="Lines",
        style={"color": "color", "width": 3, "opacity": 0.8}  # 使用 properties 裡的 color
    )

    # 讀取捷運站
    stations_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/stations.geojson"
    stations_data = requests.get(stations_url).json()

    # 加入站點
    m.add_geojson(
        stations_data,
        name="Stations",
        point_style={
            "radius": 4,
            "color": "#666666",
            "fillColor": "white",
            "fillOpacity": 1,
            "weight": 2,
            "opacity": 1,
        },
    )

    # 如果有出口資料
    exits_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/exits.geojson"
    try:
        exits_data = requests.get(exits_url).json()
        m.add_geojson(
            exits_data,
            name="Exits",
            point_style={
                "radius": 3,
                "color": "#666666",
                "fillColor": "yellow",
                "fillOpacity": 1,
                "weight": 1,
                "opacity": 1,
            },
        )
    except Exception:
        print("沒有找到出口資料，跳過")

    return m

@solara.component
def Page():
    m = create_map()
    return m.to_solara()
