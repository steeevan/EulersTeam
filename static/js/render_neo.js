function createAccurate3DRender(renderContainer, jplData) {
    console.log('Creating 3D render for NEO using JPL data:', jplData);

    // Extract and validate the diameter
    let diameter = 1; // Default value for diameter in meters
    if (jplData.physical_parameters && jplData.physical_parameters.diameter) {
        diameter = parseFloat(jplData.physical_parameters.diameter);
        if (isNaN(diameter) || diameter <= 0) {
            console.warn('Invalid diameter value from JPL data, using default value of 1 meter.');
            diameter = 1;
        } else {
            console.log('Valid diameter extracted:', diameter);
        }
    } else {
        console.warn('Diameter data is missing from JPL data, using default value.');
    }

    // Apply scaling to the diameter for better visibility
    const scaledDiameter = diameter / 50; // Adjust scale to fit the view

    // Log the radius to be used
    const radius = scaledDiameter / 2;
    console.log('Rendering sphere with radius:', radius);

    // Set up the scene, camera, and renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, renderContainer.clientWidth / renderContainer.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(renderContainer.clientWidth, renderContainer.clientHeight);
    renderContainer.appendChild(renderer.domElement);

    // Add a sphere geometry to represent the NEO
    const geometry = new THREE.SphereGeometry(radius, 32, 32);
    const material = new THREE.MeshStandardMaterial({ color: 0xff5733 }); // Orange-red color for visibility
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // Log to confirm geometry creation
    console.log('Sphere geometry added to the scene.');

    // Add ambient and directional lighting
    const ambientLight = new THREE.AmbientLight(0x404040, 2); // Soft white light
    scene.add(ambientLight);
    console.log('Ambient light added.');

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(5, 5, 5).normalize();
    scene.add(directionalLight);
    console.log('Directional light added.');

    // Position the camera to ensure visibility
    camera.position.z = Math.max(10, scaledDiameter * 2);
    console.log('Camera positioned at:', camera.position.z);

    // Create an animation loop to render the scene
    function animate() {
        requestAnimationFrame(animate);

        // Rotate the sphere for a simple animation
        sphere.rotation.y += 0.005;

        renderer.render(scene, camera);
    }

    animate();
    console.log('Animation started.');
}
