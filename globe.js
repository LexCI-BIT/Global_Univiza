// Initialize High-End Luxury SVG 3D Globe
document.addEventListener('DOMContentLoaded', () => {
  const container = d3.select('#chartdiv');
  const width = 320;
  const height = 320;
  
  // 1. Create SVG
  const svg = container.append('svg')
    .attr('width', width)
    .attr('height', height)
    .style('overflow', 'visible');

  // 2. Define Projection (Orthographic = 3D Sphere)
  const projection = d3.geoOrthographic()
    .scale(155)
    .center([0, 0])
    .rotate([0, -15])
    .translate([width / 2, height / 2]);

  const path = d3.geoPath().projection(projection);

  // 3. Define Gradients (Luxury Realistic Shading)
  const defs = svg.append('defs');
  
  // Ocean Gradient (Vibrant Realistic Blue)
  const oceanGrad = defs.append('radialGradient')
    .attr('id', 'ocean-grad')
    .attr('cx', '40%').attr('cy', '40%');
  oceanGrad.append('stop').attr('offset', '0%').attr('stop-color', '#1e90ff');
  oceanGrad.append('stop').attr('offset', '100%').attr('stop-color', '#004a8d');

  // Realistic Sphere Shading (Depth Layer)
  const sphereShading = defs.append('radialGradient')
    .attr('id', 'sphere-shading')
    .attr('cx', '40%').attr('cy', '40%');
  sphereShading.append('stop').attr('offset', '40%').attr('stop-color', 'rgba(255,255,255,0.15)'); // Light highlight
  sphereShading.append('stop').attr('offset', '100%').attr('stop-color', 'rgba(0,0,0,0.4)'); // Deep shadow at edges

  // Land Material
  const landGrad = defs.append('linearGradient')
    .attr('id', 'land-grad')
    .attr('x1', '0%').attr('y1', '0%').attr('x2', '100%').attr('y2', '100%');
  landGrad.append('stop').attr('offset', '0%').attr('stop-color', '#44B074');
  landGrad.append('stop').attr('offset', '100%').attr('stop-color', '#1B8B4E');

  // 4. Background Sphere (Water)
  svg.append('circle')
    .attr('cx', width / 2)
    .attr('cy', height / 2)
    .attr('r', projection.scale())
    .attr('fill', 'url(#ocean-grad)');
    
  // 3D Highlight Layer
  svg.append('circle')
    .attr('cx', width / 2)
    .attr('cy', height / 2)
    .attr('r', projection.scale())
    .attr('fill', 'url(#sphere-shading)')
    .style('pointer-events', 'none');

  // 5. Fetch and Render Map (Using a reliable public GeoJSON)
  d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json').then(worldData => {
    const countries = topojson.feature(worldData, worldData.objects.countries).features;
    
    // Grid Lines (Sophisticated Map Look)
    const graticule = svg.append('path')
      .datum(d3.geoGraticule())
      .attr('class', 'graticule')
      .attr('d', path)
      .attr('fill', 'none')
      .attr('stroke', 'rgba(255,255,255,0.08)')
      .attr('stroke-width', 0.5);

    // Draw Continents (Individual paths for land)
    const countryPaths = svg.selectAll('.country')
      .data(countries)
      .enter().append('path')
      .attr('class', 'country')
      .attr('d', path)
      .attr('fill', 'url(#land-grad)')
      .attr('stroke', 'rgba(255,255,255,0.1)')
      .attr('stroke-width', 0.5);

    // 6. Animation (Smooth Rotation)
    let rotation = 0;
    d3.timer(() => {
      rotation += 0.45;
      projection.rotate([rotation, -15]);
      
      // Update all layers
      svg.selectAll('path').attr('d', path);
    });
  }).catch(err => {
    console.error('D3 Globe Load Error:', err);
    // Fallback: simple circle if fetch fails
    svg.append('text')
      .attr('x', 20)
      .attr('y', 20)
      .text('Check internet connection for 3D Map');
  });
});
