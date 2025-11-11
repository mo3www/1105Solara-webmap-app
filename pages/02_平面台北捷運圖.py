import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="mercator",
        height="750px",
        zoom=2.5,
        sidebar_visible=True,
        center=[25.0330, 121.5654],
    )
    points_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/stations.geojson"
    lines_url = (
         "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
     )
    # polygons_url = (
    #     "https://github.com/opengeos/datasets/releases/download/world/countries.geojson"
    # )
    m.add_geojson(points_url, name="Points", fit_bounds=False)
    m.add_geojson(lines_url, name="Lines")
    # m.add_geojson(polygons_url, name="Polygons")

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()