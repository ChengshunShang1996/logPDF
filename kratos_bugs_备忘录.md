1. 

> RuntimeError: Error: Subproperty ID: 0 is not defined on the current Properties ID: 0 creating a new one with ID: 0

Reason：forgot to set properties to SpherePart!["SpheresPart.DEMParts_Body","DEM-DefaultMaterial"]

2. Remember to set the right element type in DEM.mdpa. [SphericParticle3D] or [SphericContinuumParticle3D]

3. Check Material.json, whether you have set properties to every part. ["SpheresPart","DEM-DefaultMaterial"]