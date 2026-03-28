am5.ready(function() {
  let root = am5.Root.new("chartdiv");
  root.setThemes([am5themes_Animated.new(root)]);

  let chart = root.container.children.push(am5map.MapChart.new(root, {
    panX: "rotateX",
    panY: "rotateY",
    projection: am5map.geoOrthographic(),
    paddingBottom: 20,
    paddingTop: 20,
    paddingLeft: 20,
    paddingRight: 20
  }));

  let polygonSeries = chart.series.push(am5map.MapPolygonSeries.new(root, {
    geoJSON: am5geodata_worldLow
  }));

  polygonSeries.mapPolygons.template.setAll({
    tooltipText: "{name}",
    toggleKey: "active",
    interactive: true,
    fill: am5.color(0x5A8BCC),
    stroke: am5.color(0xffffff),
    strokeWidth: 0.5
  });

  polygonSeries.mapPolygons.template.states.create("hover", {
    fill: am5.color(0x3B669E)
  });

  let backgroundSeries = chart.series.push(am5map.MapPolygonSeries.new(root, {}));
  backgroundSeries.mapPolygons.template.setAll({
    fill: am5.color(0xECECEC),
    fillOpacity: 1,
    strokeOpacity: 0
  });
  backgroundSeries.data.push({
    geometry: am5map.getGeoRectangle(90, 180, -90, -180)
  });

  let graticuleSeries = chart.series.push(am5map.GraticuleSeries.new(root, {}));
  graticuleSeries.mapLines.template.setAll({ strokeOpacity: 0.1, stroke: am5.color(0x000000) });

  chart.animate({
    key: "rotationX",
    from: 0,
    to: 360,
    duration: 30000,
    loops: Infinity
  });

  chart.appear(1000, 100);
});
