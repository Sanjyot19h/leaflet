import folium

# Create a map centered around a specific location (latitude, longitude)
m = folium.Map(location=[23.79024233862799, 86.43735744994336], zoom_start=15)

# List of coordinates for different polygons
polygons = [
    # Polygon 1
    [
        [23.789455600774247, 86.42845145302238],
        [23.78924943838375, 86.42845145302238],
        [23.78924943838375, 86.42913809852917],
        [23.789455600774247, 86.42913809852917],
        [23.789455600774247, 86.42845145302238]
    ],
    # Polygon 2
    [
        [23.793824203481396, 86.42703524666223],
        [23.793823021697577, 86.42700895635221],
        [23.793819487727408, 86.42698291923368],
        [23.793813635605144, 86.42695738605967],
        [23.793805521690224, 86.4269326027299],
        [23.79379522412451, 86.42690880792244],
        [23.79378284207968, 86.42688623079526],
        [23.793768494802187, 86.42686508877907],
        [23.793752320464776, 86.42684558548345],
        [23.793734474835805, 86.42682790873597],
        [23.793715129779084, 86.42681222877322],
        [23.79369447159873, 86.42679869660137],
        [23.79367269924487, 86.426787442542],
        [23.793650022397685, 86.42677857497692],
        [23.79362665944803, 86.42677217930455],
        [23.793602835394186, 86.4267683171174],
        [23.793578779675002, 86.42676702560915],
        [23.79355472396028, 86.42676831721624],
        [23.79353089991962, 86.4267721794984]
    ],
    # Polygon 3
    [
        [23.793507536991378, 86.42677857525837],
        [23.793484860173017, 86.42678744290019],
        [23.793463087854285, 86.42679869702258],
        [23.79344242971399, 86.42681222924122],
        [23.793423084700752, 86.42682790923281],
        [23.793405239116993, 86.42684558599002],
        [23.793389064824794, 86.4268650892759],
        [23.79337471759078, 86.42688623126328],
        [23.79336233558602, 86.42690880834367],
        [23.793352038055424, 86.4269326030881],
        [23.793343924169328, 86.42695738634113],
        [23.793338072068476, 86.42698291942754],
        [23.7933345381115, 86.42700895645103],
        [23.79333335633213, 86.42703524666223],
        [23.7933345381115, 86.42706153687341]
    ],
    # Polygon 4
    [
        [23.793338072068476, 86.42708757389693],
        [23.793343924169328, 86.42711310698334],
        [23.793352038055424, 86.42713789023637],
        [23.79336233558602, 86.42716168498079],
        [23.79337471759078, 86.42718426206119],
        [23.793389064824794, 86.42720540404856],
        [23.793405239116993, 86.42722490733445],
        [23.793423084700752, 86.42724258409166],
        [23.79344242971399, 86.42725826408324]
    ],
    # Polygon 5
    [
        [23.79344242971399, 86.42725826408324],
        [23.793463087854285, 86.4272717963019],
        [23.793484860173017, 86.42728305042425],
        [23.793507536991378, 86.4272919180661],
        [23.79353089991962, 86.42729831382606],
        [23.79355472396028, 86.42730217610821],
        [23.793578779675002, 86.42730346771532],
        [23.793602835394186, 86.42730217620704],
        [23.79362665944803, 86.42729831401991]
    ],
    # Polygon 6
    [
        [23.791904981293797, 86.42898253040875],
        [23.791659554465213, 86.42942777710545],
        [23.791600651957324, 86.4293741329248],
        [23.791831353293404, 86.42891279297453],
        [23.791900072761877, 86.4290039880803]
    ],
    # Polygon 7
    [
        [23.791448487021043, 86.4272390945489],
        [23.791448487021043, 86.42751804428588],
        [23.791772450863363, 86.42751804428588],
        [23.791772450863363, 86.4272390945489]
    ]
]

# Add CircleMarkers at each coordinate in the polygons for visualization
for polygon in polygons:
    for coord in polygon:
        folium.CircleMarker(
            location=coord,
            radius=5,
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)

# Add Polygons to the map
for polygon in polygons:
    folium.Polygon(
        locations=polygon,
        color='blue',
        weight=2,
        fill=True,
        fill_color='blue',
        fill_opacity=0.3
    ).add_to(m)

# Add a layer control (for multiple layers)
folium.LayerControl().add_to(m)

# Save and display the map
m.save("map_with_polygons_and_circles.html")

from IPython.display import IFrame
IFrame("map_with_polygons_and_circles.html", width=700, height=500)
m
        