<template>
  <div>
    <div class="d3"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import * as topojson from "topojson";

export default {
  name: "Home",
  mounted() {
    this.draw();
  },
  methods: {
    draw() {
      const koreaMap = require("../assets/skorea-topo-simple.json");
      const geojson = topojson.feature(
        koreaMap,
        koreaMap.objects.skorea_provinces_2018_geo
      );
      const width = 1800;
      const height = 1800;
      const svg = d3
        .select(".d3")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
      const map = svg.append("g");

      let projection = d3.geoMercator().scale(1).translate([0, 0]);
      const path = d3.geoPath().projection(projection);
      const bounds = path.bounds(geojson);
      const widthScale = (bounds[1][0] - bounds[0][0]) / width;
      const heightScale = (bounds[1][1] - bounds[0][1]) / height;
      const scale = 1 / Math.max(widthScale, heightScale);
      const xoffset =
        width / 2 - (scale * (bounds[1][0] + bounds[0][0])) / 2 + 10;
      const yoffset =
        height / 2 - (scale * (bounds[1][1] + bounds[0][1])) / 2 + 80;
      const offset = [xoffset, yoffset];
      projection.scale(scale).translate(offset);

      map
        .selectAll("path")
        .data(geojson.features)
        .enter()
        .append("path")
        .attr("d", path);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.d3 {
  fill: #ed8b70;
  stroke: #eeeeee;
  stroke-width: 3px;
}

.d3:hover {
  fill: orange;
}
</style>
