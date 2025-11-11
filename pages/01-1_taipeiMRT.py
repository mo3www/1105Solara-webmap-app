import leafmap
import solara

mrt_geojson = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/main/taipei_mrt.geojson"

def create_map():
    m = leafmap.Map(
        location=[25.0330,121.5654],
        zoom=12,
        style="catrodb.darkmatter",
        projection="globe",
        height="750px"
    )

    m.add_geojson(mrt_geojson, layer_name="台北捷運")

    return m

@solara.component
def Page():
    m.create_map()
    return m.to_solara()