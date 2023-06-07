from setuptools import setup, find_packages

setup(
    name="Surface analyses",
    version="0.1",
    description="Hydrophobicity analyses based on SASA",
    author="Franz Waibl",
    author_email="franz.waibl@uibk.ac.at",
    packages=["surface_analyses", "surface_analyses.anarci_wrapper"],
    include_package_data=True,
    zip_safe=False,
    install_requires=['numpy', 'scipy', 'pandas', 'scikit-image', 'gisttools @ git+https://github.com/liedllab/gisttools.git', 'plyfile', 'matplotlib>=3.7', 'anarci @ git+https://github.com/oxpig/ANARCI@b22f2ee05f4fc241f558b8ccb0c522d4e7563b30', 'pdb2pqr', 'biopython', 'rdkit'],
    setup_requires=['pytest_runner'],
    tests_require=['pytest'],
    py_modules=[
        "surface_analyses.commandline",
        "surface_analyses.structure",
        "surface_analyses.propensities",
        "surface_analyses.hydrophobic_potential",
        "surface_analyses.pdb",
        "surface_analyses.ele_patches",
    ],
    entry_points={
        'console_scripts': [
            'surfscore=surface_analyses.commandline:main',
            'ele_patches=surface_analyses.ele_patches:main',
        ],
    },
)
