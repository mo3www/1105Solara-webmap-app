import solara
import leafmap.maplibregl as leafmap
import requests
import json


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
        return '#cccccc'  # 預設顏色


def create_map():
    m = leafmap.Map(
        style="dark-matter",
        projection="mercator",  # 平面投影
        height="750px",
        zoom=12,
        sidebar_visible=True,
        center=[25.0330, 121.5654],  # 台北市中心
    )

    # 讀取路線資料
    lines_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    lines_data = requests.get(lines_url).json()

    # line_style 函數
    def line_style(feature):
        return {
            "color": route_color(feature["properties"].get("RouteName", "")),
            "width": 3,
            "opacity": 0.8,
        }

    m.add_geojson(lines_data, name="Lines", line_style=line_style)

    # 讀取站點資料
    stations_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/stations.geojson"
    stations_data = requests.get(stations_url).json()

    # 點資料樣式
    m.add_geojson(stations_data, name="Stations", point_style={"radius": 4, "color": "white", "fillColor": "#666666"})

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
