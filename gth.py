import networkx as nx
from pyvis.network import Network
from IPython.display import HTML, display
import json

#347-cultural scores
#elevations-434

# Create a pyvis Network
net = Network(notebook=True)

# Create an empty graph
G = nx.Graph()

# Add nodes with attributes
places = {
    'Kathmandu': {'altitude': 1400, 'cultural': 'High'},
    'Pokhara': {'altitude': 827, 'cultural': 'High'},
    'Nayapul': {'altitude': 1050, 'cultural': 'Low'},
    'Tirkhedhunga': {'altitude': 1577, 'cultural': 'Low'},
    'Birethanti': {'altitude': 1065, 'cultural': 'Low'},
    'Ghorepani': {'altitude': 2675, 'cultural': 'Medium'},
    'Upper Chistibung': {'altitude': 3000, 'cultural': 'Low'},
    'Khopra Danda': {'altitude': 3640, 'cultural': 'Low'},
    'Khayer Lake': {'altitude': 4660, 'cultural': 'Low'},
    'Dobato': {'altitude': 3438, 'cultural': 'Low'},
    'Kimche village': {'altitude': 1640, 'cultural': 'High'},
    'Ghandruk': {'altitude': 1640, 'cultural': 'High'},
    'Hemja Milanchok': {'altitude': 827, 'cultural': 'Low'},
    'Anante Thati': {'altitude': 1100, 'cultural': 'Low'},
    'Lalka': {'altitude': 2250, 'cultural': 'Low'},
    'Ribhan Village': {'altitude': 1500, 'cultural': 'Low'},
    'Khumai Danda': {'altitude': 3245, 'cultural': 'Low'},
    'Campsite': {'altitude': 3699, 'cultural': 'Low'},
    'Machhapuchhre Base Camp': {'altitude': 4000, 'cultural': 'Medium'},
    'Pilicho Camp': {'altitude': 2900, 'cultural': 'Low'},
    'Karuwa': {'altitude': 1380, 'cultural': 'Low'},
    'Ghachok': {'altitude': 1254, 'cultural': 'Low'},
    'Swayambhunath': {'altitude': 1400, 'cultural': 'High'},
    'Kathmandu Durbar Square': {'altitude': 1400, 'cultural': 'High'},
    'Arughat': {'altitude': 530, 'cultural': 'Low'},
    'Soti Khola': {'altitude': 730, 'cultural': 'Medium'},
    'Machha Khola': {'altitude': 930, 'cultural': 'Low'},
    'Jagat': {'altitude': 1410, 'cultural': 'Low'},
    'Dang': {'altitude': 1800, 'cultural': 'Medium'},
    'Namrung': {'altitude': 2660, 'cultural': 'Low'},
    'Lho': {'altitude': 3180, 'cultural': 'Low'},
    'Samagaon': {'altitude': 3530, 'cultural': 'Low'},
    'Manaslu Basecamp': {'altitude': 4800, 'cultural': 'Low'},
    'Birendra Tal': {'altitude': 3600, 'cultural': 'Low'},
    'Samdo': {'altitude': 3875, 'cultural': 'Low'},
    'Dharamsala': {'altitude': 4460, 'cultural': 'Low'},
    'Larkya La High Pass': {'altitude': 5160, 'cultural': 'Low'},
    'Bimthang': {'altitude': 3590, 'cultural': 'Low'},
    'Dharapani': {'altitude': 1963, 'cultural': 'Low'},
    'Besisahar': {'altitude': 760, 'cultural': 'Medium'},
    'Nepalgunj': {'altitude': 150, 'cultural': 'Medium'},
    'Jumla': {'altitude': 2370, 'cultural': 'Medium'},
    'Uthugaon': {'altitude': 2530, 'cultural': 'Low'},
    'Danphe Lagna': {'altitude': 3500, 'cultural': 'Low'},
    'Chautha': {'altitude': 2770, 'cultural': 'Low'},
    'Dhotu': {'altitude': 2380, 'cultural': 'Low'},
    'Rara Lake': {'altitude': 2990, 'cultural': 'Low'},
    'Gorosingha': {'altitude': 3190, 'cultural': 'Low'},
    'Sinja': {'altitude': 2440, 'cultural': 'Low'},
    'Jaljala Chaur': {'altitude': 3270, 'cultural': 'Low'}
    

}


# cultural_scores = {'High': 3, 'Medium': 2, 'Low': 1}
cultural_colors = {'High': 'red', 'Medium': 'orange', 'Low': 'green'}

# Sorting places based on altitude
sorted_places = sorted(places.items(), key=lambda x: x[1]['altitude'], reverse=True)

for place, attributes in sorted_places:
    G.add_node(place, **attributes)
    net.add_node(
        place,
        label=place,
        title=f"Altitude: {attributes['altitude']}m\nCultural: {attributes['cultural']}",
        color=cultural_colors[attributes['cultural']],
        shape='circle'
    )

# Add edges (paths between places) with distances
edges = [
    ('Kathmandu', 'Pokhara', 7),
    ('Pokhara', 'Nayapul', 6),  # Estimate for the drive time from Pokhara to Nayapul
    ('Nayapul', 'Tirkhedhunga', 4),
    ('Tirkhedhunga', 'Ghorepani', 6),
    ('Ghorepani', 'Upper Chistibung', 6),
    ('Upper Chistibung', 'Khopra Danda', 4),
    
    ('Khayer Lake', 'Khopra Danda', 8),  # Assuming the return journey takes the same time
    ('Khopra Danda', 'Dobato', 5),
    ('Dobato', 'Kimche village', 6),  # Estimate for the trekking time from Dobato to Kimche village via Ghandruk
    ('Kimche village', 'Pokhara', 7) ,# Estimate for the drive time from Kimche village to Pokhara
    ('Pokhara', 'Hemja Milanchok', 1),  # 20 minutes
    ('Hemja Milanchok', 'Anante Thati', 1),  # Assuming start of trek
    ('Anante Thati', 'Lalka', 6),  # Estimated based on trek duration
    ('Lalka', 'Ribhan Village', 2),  # Part of the route to Lalka
    ('Lalka', 'Khumai Danda', 7),
    ('Khumai Danda', 'Campsite', 6),
    ('Campsite', 'Machhapuchhre Base Camp', 5),
    ('Machhapuchhre Base Camp', 'Pilicho Camp', 6),
    ('Pilicho Camp', 'Karuwa', 4),
    ('Karuwa', 'Ghachok', 5),
    ('Ghachok', 'Hemja Milanchok', 1),  # Assuming similar duration
    
    
    ('Kathmandu', 'Swayambhunath', 0),  # Cultural sightseeing
    ('Swayambhunath', 'Kathmandu Durbar Square', 0),  # Cultural sightseeing
    ('Kathmandu', 'Arughat', 8),  # Drive
    ('Arughat', 'Soti Khola', 0),  # Jeep drive, no specific time mentioned
    ('Soti Khola', 'Machha Khola', 6),
    ('Machha Khola', 'Jagat', 8),
    ('Jagat', 'Dang', 6),
    ('Dang', 'Namrung', 6),
    ('Namrung', 'Lho', 4),
    ('Lho', 'Samagaon', 4),
    ('Samagaon', 'Manaslu Basecamp', 0),  # Acclimatization day, round trip
    ('Samagaon', 'Birendra Tal', 0),  # Acclimatization day, round trip
    ('Samagaon', 'Samdo', 4),
    ('Samdo', 'Dharamsala', 4),
    ('Dharamsala', 'Larkya La High Pass', 0),  # Part of the trek to Bimthang
    ('Larkya La High Pass', 'Bimthang', 11),
    ('Bimthang', 'Dharapani', 9),
    ('Dharapani', 'Besisahar', 0),  # Drive
    ('Besisahar', 'Kathmandu', 10),  # Drive
    ('Kathmandu', 'Nepalgunj', 0.83),  # 50 minutes flight
    ('Nepalgunj', 'Jumla', 0.33),  # 20 minutes flight
    ('Jumla', 'Uthugaon', 6),  # Estimated based on trek duration
    ('Uthugaon', 'Danphe Lagna', 6),  # Estimated based on trek duration
    ('Danphe Lagna', 'Chautha', 6),  # Estimated based on trek duration
    ('Chautha', 'Dhotu', 6),  # Estimated based on trek duration
    ('Dhotu', 'Rara Lake', 6),  # Estimated based on trek duration
    ('Rara Lake', 'Gorosingha', 5),
    ('Gorosingha', 'Sinja', 6),  # Estimated based on trek duration
    ('Sinja', 'Jaljala Chaur', 6),  # Estimated based on trek duration
    ('Jaljala Chaur', 'Jumla', 6),  # Estimated based on trek duration
        
    
    
]


for u, v, d in edges:
    G.add_edge(u, v, distance=d)
    net.add_edge(u, v, title=f"Distance: {d} km", length=d)

# Save the network to HTML
net.save_graph("great_himalayan_trail.html")

# Create HTML with JavaScript for interactive vertex selection and graph visualization
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Great Himalayan Trail</title>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <h1>Great Himalayan Trail</h1>
    <p>Select two vertices to find the shortest path, the path with the highest cultural significance score, or the path with minimal elevation change:</p>
    <select id="start-node">
        <option value="">Select start node</option>
        %s
    </select>
    <select id="end-node">
        <option value="">Select end node</option>
        %s
    </select>
    <button onclick="findShortestPath()">Find Shortest Path</button>
    <button onclick="findHighestCulturalPath()">Find Path with Highest Cultural Significance</button>
    <button onclick="findMinimalElevationPath()">Find Path with Minimal Elevation Change</button>
    <p id="shortest-path-result"></p>
    <p id="highest-cultural-path-result"></p>
    <p id="minimal-elevation-path-result"></p>
    <div id="mynetwork" style="height: 600px;"></div>
    <script type="text/javascript">
        // JavaScript code for interactive vertex selection

        // Define the nodes data
        var nodes = new vis.DataSet(%s);

        // Define the edges data
        var edges = new vis.DataSet(%s);

        // Create the network
        var container = document.getElementById('mynetwork');
        var data = { nodes: nodes, edges: edges };
        var options = {};
        var network = new vis.Network(container, data, options);

        // Store original edge colors and widths
        var originalEdgeStyles = {};
        edges.forEach(function(edge) {
            originalEdgeStyles[edge.id] = {
                color: edge.color || '#848484',  // Default color in vis.js
                width: edge.width || 1           // Default width in vis.js
            };
        });

        // Find the shortest path function using Dijkstra's algorithm
        function findShortestPath() {
            var startNode = document.getElementById('start-node').value;
            var endNode = document.getElementById('end-node').value;

            if (startNode === "" || endNode === "") {
                alert("Please select both start and end nodes.");
                return;
            }

            var result = dijkstra(startNode, endNode);
            document.getElementById('shortest-path-result').innerText = "Shortest path: " + result.path.join(' -> ') + " (Time: " + result.distance + " hrs)";

            // Reset edge styles to original
            edges.forEach(function(edge) {
                var originalStyle = originalEdgeStyles[edge.id];
                edge.color = originalStyle.color;
                edge.width = originalStyle.width;
                edges.update(edge);
            });

            // Highlight the shortest path on the graph
            var pathEdges = [];
            for (var i = 0; i < result.path.length - 1; i++) {
                var fromNode = result.path[i];
                var toNode = result.path[i + 1];
                var edgeId = edges.getIds({
                    filter: function(item) {
                        return (item.from === fromNode && item.to === toNode) || (item.from === toNode && item.to === fromNode);
                    }
                })[0];
                pathEdges.push(edgeId);
            }

            var selectedEdges = edges.get({
                filter: function(item) {
                    return pathEdges.includes(item.id);
                }
            });

            // Highlight shortest path by changing color and width
            selectedEdges.forEach(function(edge) {
                edge.color = { color: 'blue' };
                edge.width = 3;
                edges.update(edge);
            });
        }

        // Find the path with the highest cultural significance
        function findHighestCulturalPath() {
            var startNode = document.getElementById('start-node').value;
            var endNode = document.getElementById('end-node').value;

            if (startNode === "" || endNode === "") {
                alert("Please select both start and end nodes.");
                return;
            }

            var result = findPathWithHighestCulturalSignificance(startNode, endNode);
            document.getElementById('highest-cultural-path-result').innerText = "Path with highest cultural significance: " + result.path.join(' -> ') + " (Cultural Score: " + result.culturalScore + ")";

            // Reset edge styles to original
            edges.forEach(function(edge) {
                var originalStyle = originalEdgeStyles[edge.id];
                edge.color = originalStyle.color;
                edge.width = originalStyle.width;
                edges.update(edge);
            });

            // Highlight the cultural path on the graph
            var pathEdges = [];
            for (var i = 0; i < result.path.length - 1; i++) {
                var fromNode = result.path[i];
                var toNode = result.path[i + 1];
                var edgeId = edges.getIds({
                    filter: function(item) {
                        return (item.from === fromNode && item.to === toNode) || (item.from === toNode && item.to === fromNode);
                    }
                })[0];
                pathEdges.push(edgeId);
            }

            var selectedEdges = edges.get({
                filter: function(item) {
                    return pathEdges.includes(item.id);
                }
            });

            // Highlight cultural path by changing color and width
            selectedEdges.forEach(function(edge) {
                edge.color = { color: 'black' };
                edge.width = 3;
                edges.update(edge);
            });
        }

        // Find path with minimal elevation change
        function findMinimalElevationPath() {
            var startNode = document.getElementById('start-node').value;
            var endNode = document.getElementById('end-node').value;

            if (startNode === "" || endNode === "") {
                alert("Please select both start and end nodes.");
                return;
            }

            var result = findPathWithMinimalElevationChange(startNode, endNode);
            document.getElementById('minimal-elevation-path-result').innerText = "Path with minimal elevation change: " + result.path.join(' -> ') + " (Distance: " + result.distance + " km)";

            // Reset edge styles to original
            edges.forEach(function(edge) {
                var originalStyle = originalEdgeStyles[edge.id];
                edge.color = originalStyle.color;
                edge.width = originalStyle.width;
                edges.update(edge);
            });

            // Highlight the path with minimal elevation change on the graph
            var pathEdges = [];
            for (var i = 0; i < result.path.length - 1; i++) {
                var fromNode = result.path[i];
                var toNode = result.path[i + 1];
                var edgeId = edges.getIds({
                    filter: function(item) {
                        return (item.from === fromNode && item.to === toNode) || (item.from === toNode && item.to === fromNode);
                    }
                })[0];
                pathEdges.push(edgeId);
            }

            var selectedEdges = edges.get({
                filter: function(item) {
                    return pathEdges.includes(item.id);
                }
            });

            // Highlight path with minimal elevation change by changing color and width
            selectedEdges.forEach(function(edge) {
                edge.color = { color: 'purple' };
                edge.width = 3;
                edges.update(edge);
            });
        }

        // Dijkstra's algorithm implementation
        function dijkstra(startNode, endNode) {
            var distances = {};
            var prev = {};
            var pq = new Set();

            // Initialize distances and previous nodes
            nodes.forEach(function(node) {
                distances[node.id] = Infinity;
                prev[node.id] = null;
                pq.add(node.id);
            });

            distances[startNode] = 0;

            while (pq.size > 0) {
                var minNode = null;
                pq.forEach(function(node) {
                    if (minNode === null || distances[node] < distances[minNode]) {
                        minNode = node;
                    }
                });

                pq.delete(minNode);

                if (minNode === endNode) {
                    break;
                }

                edges.forEach(function(edge) {
                    if (edge.from === minNode && pq.has(edge.to)) {
                        var alt = distances[minNode] + edge.length;
                        if (alt < distances[edge.to]) {
                            distances[edge.to] = alt;
                            prev[edge.to] = minNode;
                        }
                    }
                    if (edge.to === minNode && pq.has(edge.from)) {
                        var alt = distances[minNode] + edge.length;
                        if (alt < distances[edge.from]) {
                            distances[edge.from] = alt;
                            prev[edge.from] = minNode;
                        }
                    }
                });
            }

            var path = [];
            var current = endNode;
            while (current !== null) {
                path.unshift(current);
                current = prev[current];
            }

            return { path: path, distance: distances[endNode] };
        }

        // Find path with the highest cultural significance
        function findPathWithHighestCulturalSignificance(startNode, endNode) {
            culturalScores = {
    'Kathmandu': 4,
    'Pokhara': 4,
    'Nayapul': 1,
    'Tirkhedhunga': 1,
    'Birethanti': 1,
    'Ghorepani': 2,
    'Upper Chistibung': 1,
    'Khopra Danda': 1,
    'Khayer Lake': 1,
    'Dobato': 1,
    'Kimche village': 4,
    'Ghandruk': 4,
    'Hemja Milanchok': 1,
    'Anante Thati': 1,
    'Lalka': 1,
    'Ribhan Village': 1,
    'Khumai Danda': 1,
    'Campsite': 1,
    'Machhapuchhre Base Camp': 2,
    'Pilicho Camp': 1,
    'Karuwa': 1,
    'Ghachok': 1,
    'Swayambhunath': 4,
    'Kathmandu Durbar Square': 4,
    'Arughat': 1,
    'Soti Khola': 2,
    'Machha Khola': 1,
    'Jagat': 1,
    'Dang': 2,
    'Namrung': 1,
    'Lho': 1,
    'Samagaon': 1,
    'Manaslu Basecamp': 1,
    'Birendra Tal': 1,
    'Samdo': 1,
    'Dharamsala': 1,
    'Larkya La High Pass': 1,
    'Bimthang': 1,
    'Dharapani': 1,
    'Besisahar': 2,
    'Nepalgunj': 2, 
    'Jumla': 2,
    'Uthugaon': 1,
    'Danphe Lagna': 1,
    'Chautha': 1,
    'Dhotu': 1,
    'Rara Lake': 1,
    'Gorosingha': 1,
    'Sinja': 1,
    'Jaljala Chaur': 1

    
}


            var distances = {};
            var culturalScoresAcc = {};
            var prev = {};
            var pq = new Set();

            // Initialize distances, cultural scores, and previous nodes
            nodes.forEach(function(node) {
                distances[node.id] = Infinity;
                culturalScoresAcc[node.id] = -Infinity;
                prev[node.id] = null;
                pq.add(node.id);
            });

            distances[startNode] = 0;
            culturalScoresAcc[startNode] = culturalScores[startNode];

            while (pq.size > 0) {
                var maxCulturalNode = null;
                pq.forEach(function(node) {
                    if (maxCulturalNode === null || culturalScoresAcc[node] > culturalScoresAcc[maxCulturalNode]) {
                        maxCulturalNode = node;
                    }
                });

                pq.delete(maxCulturalNode);

                if (maxCulturalNode === endNode) {
                    break;
                }

                edges.forEach(function(edge) {
                    if (edge.from === maxCulturalNode && pq.has(edge.to)) {
                        var altScore = culturalScoresAcc[maxCulturalNode] + culturalScores[edge.to];
                        if (altScore > culturalScoresAcc[edge.to]) {
                            culturalScoresAcc[edge.to] = altScore;
                            prev[edge.to] = maxCulturalNode;
                        }
                    }
                    if (edge.to === maxCulturalNode && pq.has(edge.from)) {
                        var altScore = culturalScoresAcc[maxCulturalNode] + culturalScores[edge.from];
                        if (altScore > culturalScoresAcc[edge.from]) {
                            culturalScoresAcc[edge.from] = altScore;
                            prev[edge.from] = maxCulturalNode;
                        }
                    }
                });
            }

            var path = [];
            var current = endNode;
            while (current !== null) {
                path.unshift(current);
                current = prev[current];
            }

            return { path: path, culturalScore: culturalScoresAcc[endNode] };
        }

        // Find path with minimal elevation change
        function findPathWithMinimalElevationChange(startNode, endNode) {
            elevations = {
    'Kathmandu': 1400,
    'Pokhara': 827,
    'Nayapul': 1050,
    'Tirkhedhunga': 1577,
    'Birethanti': 1065,
    'Ghorepani': 2675,
    'Upper Chistibung': 3000,
    'Khopra Danda': 3640,
    'Khayer Lake': 4660,
    'Dobato': 3438,
    'Kimche village': 1640,
    'Ghandruk': 1640,
    'Hemja Milanchok': 827,  
    'Anante Thati': 1100,
    'Lalka': 2250,
    'Ribhan Village': 1500,  
    'Khumai Danda': 3245,
    'Campsite': 3699,
    'Machhapuchhre Base Camp': 4000,
    'Pilicho Camp': 2900,
    'Karuwa': 1380,
    'Ghachok': 1254,
    'Swayambhunath': 1400, 
    'Kathmandu Durbar Square': 1400,  
    'Arughat': 530,  
    'Soti Khola': 730,
    'Machha Khola': 930,
    'Jagat': 1410,
    'Dang': 1800,
    'Namrung': 2660,
    'Lho': 3180,
    'Samagaon': 3530,
    'Manaslu Basecamp': 4800,
    'Birendra Tal': 3600, 
    'Samdo': 3875,
    'Dharamsala': 4460,
    'Larkya La High Pass': 5160,
    'Bimthang': 3590,
    'Dharapani': 1963,
    'Besisahar': 760,
    'Nepalgunj': 150,  
    'Jumla': 2370,
    'Uthugaon': 2530,
    'Danphe Lagna': 3500,
    'Chautha': 2770,
    'Dhotu': 2380,
    'Rara Lake': 2990,
    'Gorosingha': 3190,
    'Sinja': 2440,
    'Jaljala Chaur': 3270
    
}


            var distances = {};
            var elevationDiffs = {};
            var prev = {};
            var pq = new Set();

            // Initialize distances, elevation differences, and previous nodes
            nodes.forEach(function(node) {
                distances[node.id] = Infinity;
                elevationDiffs[node.id] = Infinity;
                prev[node.id] = null;
                pq.add(node.id);
            });

            distances[startNode] = 0;
            elevationDiffs[startNode] = 0;

            while (pq.size > 0) {
                var minElevationNode = null;
                pq.forEach(function(node) {
                    if (minElevationNode === null || elevationDiffs[node] < elevationDiffs[minElevationNode]) {
                        minElevationNode = node;
                    }
                });

                pq.delete(minElevationNode);

                if (minElevationNode === endNode) {
                    break;
                }

                edges.forEach(function(edge) {
                    if (edge.from === minElevationNode && pq.has(edge.to)) {
                        var alt = distances[minElevationNode] + edge.length;
                        var elevationDiff = Math.abs(elevations[minElevationNode] - elevations[edge.to]);
                        if (alt < distances[edge.to] && elevationDiff < elevationDiffs[edge.to]) {
                            distances[edge.to] = alt;
                            elevationDiffs[edge.to] = elevationDiff;
                            prev[edge.to] = minElevationNode;
                        }
                    }
                    if (edge.to === minElevationNode && pq.has(edge.from)) {
                        var alt = distances[minElevationNode] + edge.length;
                        var elevationDiff = Math.abs(elevations[minElevationNode] - elevations[edge.from]);
                        if (alt < distances[edge.from] && elevationDiff < elevationDiffs[edge.from]) {
                            distances[edge.from] = alt;
                            elevationDiffs[edge.from] = elevationDiff;
                            prev[edge.from] = minElevationNode;
                        }
                    }
                });
            }

            var path = [];
            var current = endNode;
            while (current !== null) {
                path.unshift(current);
                current = prev[current];
            }

            return { path: path, distance: distances[endNode] };
        }
    </script>
</body>
</html>
""" % (
    "".join(f'<option value="{node}">{node}</option>' for node in places.keys()),
    "".join(f'<option value="{node}">{node}</option>' for node in places.keys()),
    json.dumps([{'id': node, 'label': node, 'title': f"Altitude: {places[node]['altitude']}m\nCultural: {places[node]['cultural']}", 'color': cultural_colors[places[node]["cultural"]]} for node in places]),
    json.dumps([{'from': u, 'to': v, 'title': f"Distance: {d} km", 'length': d, 'id': f"{u}-{v}"} for u, v, d in edges])
)

# Write the HTML content to a file
with open("great_himalayan_trail_interactive.html", "w") as f:
    f.write(html_content)

# Display the HTML file in the notebook
display(HTML("great_himalayan_trail_interactive.html"))


                
