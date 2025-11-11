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
        projection="mercator",  # 使用平面投影
        height="750px",
        zoom=12,  # 設定適合台北市區的縮放級別
        sidebar_visible=True,
        pitch=0,  # 取消傾斜角度
        bearing=0,  # 取消旋轉角度
        center=[25.0330, 121.5654],  # 置中於台北市
    )

    # 讀取捷運路線資料
    lines_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    lines_data = requests.get(lines_url).json()

    # 為每條路線設定顏色
    for feature in lines_data['features']:
        line_name = feature['properties'].get('RouteName', '')
        color = route_color(line_name)  # 根據路線名稱決定顏色
        feature['properties']['color'] = color  # 更新顏色

    # 添加路線資料
    m.add_geojson(
        lines_data,
        name="Lines",
        style={
            'color': 'color',  # 使用 'color' 屬性來設置顏色
            'weight': 3,  # 線條粗細
            'opacity': 0.7  # 透明度
        }
    )

    # 讀取捷運站點資料
    stations_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/stations.geojson"
    stations_data = requests.get(stations_url).json()

    # 添加站點資料
    m.add_geojson(stations_data, name="Stations", fit_bounds=True)

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
