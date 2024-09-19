from setuptools import setup

def post_install():
    # Uninstall any existing math3d package
    subprocess.call(['pip', 'uninstall', '-y', 'math3d'])
    # Install your fork from GitHub
    subprocess.call(['pip', 'install', 'git+https://github.com/Dozgulbas/pymath3d.git#egg=math3d'])

setup(
    name="urx",
    version="0.11.0",
    description="Python library to control an UR robot",
    author="Doga Ozgulbas",
    author_email="dozgulbas@anl.gov",
    url='https://github.com/Dozgulbas/python-urx',
    packages=["urx"],
    provides=["urx"],
    cmdclass={'install': post_install},  # Hooking into the post-install
    install_requires=[
        "numpy",
        "math3d @ git+https://github.com/Dozgulbas/pymath3d.git@main#egg=math3d"
    ],
    license="GNU Lesser General Public License v3",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
