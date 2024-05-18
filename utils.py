PRIMARY = "#1f65c5"
SECONDARY = "orange"

AREA_CHART = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.17.0.json",
    "mark": {
        "type": "area",
        "line": {"color": PRIMARY},
        "color": {
            "x1": 1,
            "y1": 1,
            "x2": 1,
            "y2": 0,
            "gradient": "linear",
            "stops": [
                {"offset": 0, "color": "white"},
                {"offset": 1, "color": PRIMARY},
            ],
        },
    },
    "encoding": {
        "tooltip": [
            {"field": "annais", "type": "quantitative", "title": "Année"},
            {
                "field": "nombre",
                "type": "quantitative",
                "title": "Naissances",
                "format": "~s",
            },
        ],
        "x": {
            "axis": {"grid": True, "tickMinStep": 1, "format": ".0f"},
            "field": "annais",
            "scale": {},
            "title": "",
            "type": "quantitative",
        },
        "y": {
            "axis": {"grid": True, "tickMinStep": 1, "format": "~s"},
            "field": "nombre",
            "scale": {},
            "title": "",
            "type": "quantitative",
        },
    },
    # "height": 0,
    "width": 700,
    # "autosize": {"type": "fit", "contains": "padding"},
    # "padding": {"bottom": 20},
}

BAR_CHART = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.17.0.json",
    "transform": [
        {"calculate": "datum.sexe == 1 ? 'Garçons' : 'Filles'", "as": "sexe_label"}
    ],
    "mark": {"type": "bar", "color": PRIMARY, "cornerRadiusEnd": 8},
    "encoding": {
        "tooltip": [
            {"field": "preusuel", "type": "nominal", "title": "Prénom"},
            {
                "field": "nombre",
                "type": "quantitative",
                "title": "Naissances",
                "format": "~s",
            },
        ],
        "x": {
            "axis": {"grid": True, "tickMinStep": 1, "labelAngle": 0},
            "field": "position",
            "scale": {},
            "title": "Top",
            "type": "nominal",
            "sort": "-y",
        },
        "y": {
            "axis": {"format": "~s"},
            "field": "nombre",
            "scale": {},
            "title": "",
            "type": "quantitative",
        },
        "xOffset": {"field": "sexe_label"},
        "color": {
            "field": "sexe_label",
            "legend": {"title": "", "direction": "horizontal", "orient": "top"},
        },
    },
    # "height": 400,
    "width": 704,
    # "autosize": {"type": "fit", "contains": "padding"},
    # "autosize": {"type": "fit"},
    "padding": {"bottom": 20},
}
