import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="mercator",
        height="750px",
        center=[121.5654, 25.0330],  # [lng, lat]
        zoom=13,
        sidebar_visible=True,
    )

    # 使用 raw.githubusercontent.com 的 GeoJSON 連結（不是 blob）
    road_geojson = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

    road_style = {
        "layers": [
            {
                "id": "Roads",
                "type": "line",
                "paint": {
                    "line-color": "#ffffff",
                    "line-width": 2,
                },
            },
        ]
    }

    # 對 GeoJSON 使用 add_geojson（不是 add_pmtiles）
    m.add_geojson(road_geojson, layer_name="Taipei MRT", style=road_style, tooltip=True, fit_bounds=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()