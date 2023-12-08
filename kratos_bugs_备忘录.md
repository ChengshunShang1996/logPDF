1. 

    > RuntimeError: Error: Subproperty ID: 0 is not defined on the current Properties ID: 0 creating a new one with ID: 0

    Reason：forgot to set properties to SpherePart!["SpheresPart.DEMParts_Body","DEM-DefaultMaterial"]

2. Remember to set the right element type in DEM.mdpa. [SphericParticle3D] or [SphericContinuumParticle3D]

3. Check Material.json, whether you have set properties to every part. ["SpheresPart","DEM-DefaultMaterial"]

4. If your DEM simulation runs much slower than expected

   You can check the [MaxTimeStep], [NeighbourSearchFrequency], and [SearchTolerance].

5. pip 

    > pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

    Try "python -m pip install XXX"

6. NameError: name 'GROUP_ID' is not defined

    Possible reason: add "from KratosMultiphysics.DEMApplication import *" in your running file

7. The structure of Cosimlation: CoSimAnalysis --> CoSimSolver --> FEMAnalysis (FEMSolver) and DEMAnalysis (DEMSolver)

    WeakCouplingSolver --> SubTimeStepSolver