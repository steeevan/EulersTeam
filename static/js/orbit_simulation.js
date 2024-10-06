// Set up the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 3000);
const renderer = new THREE.WebGLRenderer({ antialias: true });

// Set renderer to fill the entire window
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x000000); // Black background for space
document.body.appendChild(renderer.domElement); // Append the renderer to the body for fullscreen rendering

// Adjust camera position to provide a full view of the solar system
camera.position.set(0, 200, 800); // Move the camera back and up
camera.lookAt(0, 0, 0); // Make sure the camera is pointed at the center of the solar system (where the Sun is located)

// Create the Sun (central object)
const sunGeometry = new THREE.SphereGeometry(40, 32, 32);
const sunMaterial = new THREE.MeshBasicMaterial({ color: 0xffff00 }); // Yellow color for the Sun
const sun = new THREE.Mesh(sunGeometry, sunMaterial);
scene.add(sun);

// Define realistic planets data with more distinctive colors
const planetsData = [
    { name: 'Mercury', size: 7, color: 0xffd700, distance: 60, orbitalPeriod: 88, diameter: 4879, orbitalSpeed: 47.87, hoursPerDay: 1407.5 },
    { name: 'Venus', size: 10, color: 0xff69b4, distance: 90, orbitalPeriod: 225, diameter: 12104, orbitalSpeed: 35.02, hoursPerDay: 5832.5 },
    { name: 'Earth', size: 12, color: 0x1e90ff, distance: 120, orbitalPeriod: 365, diameter: 12742, orbitalSpeed: 29.78, hoursPerDay: 24 },
    { name: 'Mars', size: 10, color: 0xff4500, distance: 160, orbitalPeriod: 687, diameter: 6779, orbitalSpeed: 24.07, hoursPerDay: 24.6 },
    { name: 'Jupiter', size: 25, color: 0xcd853f, distance: 220, orbitalPeriod: 4333, diameter: 139820, orbitalSpeed: 13.07, hoursPerDay: 9.9 },
    { name: 'Saturn', size: 22, color: 0xf0e68c, distance: 300, orbitalPeriod: 10759, diameter: 116460, orbitalSpeed: 9.69, hoursPerDay: 10.7 },
    { name: 'Uranus', size: 18, color: 0x40e0d0, distance: 400, orbitalPeriod: 30687, diameter: 50724, orbitalSpeed: 6.81, hoursPerDay: 17.2 },
    { name: 'Neptune', size: 18, color: 0x8a2be2, distance: 500, orbitalPeriod: 60190, diameter: 49244, orbitalSpeed: 5.43, hoursPerDay: 16.1 },
];
// Create planet meshes, labels, and add them to the scene
const planets = [];
const labels = [];

planetsData.forEach((data) => {
    // Create planet mesh
    const geometry = new THREE.SphereGeometry(data.size, 32, 32);
    const material = new THREE.MeshBasicMaterial({ color: data.color });
    const planet = new THREE.Mesh(geometry, material);
    scene.add(planet);
    planets.push({ mesh: planet, distance: data.distance, orbitalPeriod: data.orbitalPeriod, ...data });

    // Create an orbital ring for each planet
    const ringPoints = [];
    const segments = 200;
    for (let i = 0; i <= segments; i++) {
        const theta = (i / segments) * 2 * Math.PI;
        ringPoints.push(new THREE.Vector3(data.distance * Math.cos(theta), 0, data.distance * Math.sin(theta)));
    }
    const ringGeometry = new THREE.BufferGeometry().setFromPoints(ringPoints);
    const ringMaterial = new THREE.LineBasicMaterial({ color: data.color, transparent: true, opacity: 0.7 });
    const ring = new THREE.Line(ringGeometry, ringMaterial);
    scene.add(ring);

    // Create a label for the planet
    const label = document.createElement('div');
    label.className = 'planet-label';
    label.innerText = data.name;
    label.style.position = 'absolute';
    label.style.color = 'white';
    label.style.pointerEvents = 'none'; // Make the label non-interactive
    document.body.appendChild(label);
    labels.push({ element: label, planet });
});

// Populate planet attributes table
function populatePlanetAttributesTable() {
    const tableBody = document.getElementById('planetAttributesTable');
    tableBody.innerHTML = ''; // Clear previous content
    planetsData.forEach(planet => {
        const row = document.createElement('tr');
        row.style.backgroundColor = `#${planet.color.toString(16)}`;
        row.innerHTML = `
            <td>${planet.name}</td>
            <td>${planet.size} km</td>
            <td>${(planet.distance * 1000000).toFixed(2)} km</td>
            <td>${planet.orbitalPeriod} days</td>
            <td>${planet.hoursPerDay} hours</td>
        `;
        tableBody.appendChild(row);
    });
}

// Toggle planet attributes overlay
document.getElementById('toggleAttributesButton').addEventListener('click', () => {
    const attributesOverlay = document.getElementById('attributes');
    attributesOverlay.style.display = attributesOverlay.style.display === 'block' ? 'none' : 'block';
    populatePlanetAttributesTable();
});

// Close planet attributes overlay
document.getElementById('closeAttributesButton').addEventListener('click', () => {
    document.getElementById('attributes').style.display = 'none';
});

// Animation variables
let time = 0;
let orbitSpeed = 1;
let scale = 1.0;

// Add an event listener to the orbit speed slider to update the orbit speed
const speedSlider = document.getElementById('speedSlider');
speedSlider.addEventListener('input', (event) => {
    orbitSpeed = parseFloat(event.target.value);
});

// Add an event listener to the scale slider to update the scale of the entire solar system
const scaleSlider = document.getElementById('scaleSlider');
scaleSlider.addEventListener('input', (event) => {
    scale = parseFloat(event.target.value);
    scene.scale.set(scale, scale, scale); // Update the scale of the entire scene
});

// Animation loop function
function animate() {
    requestAnimationFrame(animate);

    // Update each planet's position
    time += orbitSpeed;
    planets.forEach((planetData, index) => {
        const angle = (time / planetData.orbitalPeriod) * 2 * Math.PI;
        const x = planetData.distance * Math.cos(angle);
        const z = planetData.distance * Math.sin(angle);
        planetData.mesh.position.set(x, 0, z);

        // Update the label position
        const vector = new THREE.Vector3(x, planetData.size + 5, z);
        vector.project(camera);

        const xCoord = (vector.x * 0.5 + 0.5) * window.innerWidth;
        const yCoord = (-vector.y * 0.5 + 0.5) * window.innerHeight;
        labels[index].element.style.transform = `translate(-50%, -50%) translate(${xCoord}px, ${yCoord}px)`;
    });

    // Render the scene
    renderer.render(scene, camera);
}

// Start the animation loop
animate();

// Handle window resizing to maintain proper aspect ratio
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
