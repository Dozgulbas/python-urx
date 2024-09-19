from setuptools import setup
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # Uninstall any existing math3d package
        subprocess.call(['pip', 'uninstall', '-y', 'math3d'])
        # Install your fork from GitHub
        subprocess.call(['pip', 'install', 'git+https://github.com/Dozgulbas/pymath3d.git#egg=math3d'])
        install.run(self)

setup(
    name="urx",
    version="0.11.0",
    description="Python library to control an UR robot",
    author="Doga Ozgulbas",
    author_email="dozgulbas@anl.gov",
    url='https://github.com/Dozgulbas/python-urx',
    packages=["urx"],
    provides=["urx"],
    install_requires=[
        "numpy",
        "math3d @ git+https://github.com/Dozgulbas/pymath3d.git@main#egg=math3d"
    ],
    cmdclass={
        'install': PostInstallCommand,
    }  # Hooking into the post-install
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
